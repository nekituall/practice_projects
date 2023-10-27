import requests
from requests import RequestException

def check_active(addr):
    """Check active write indexes"""
    try:
        r = requests.get(f"http://{addr}:9200/*_deflector/_alias")
        res = dict(r.json())
        lst = []        #list for active indexes
        for i in res:
            if "_" in i:
                lst.append(i)
        print(f"Current write indexes on {addr} are: ")
        return lst
    except RequestException as e:
        return e

def update_template(addr):
    try:
        r = requests.get(f"http://{addr}:9000/api/system/indexer/indices/templates/update", headers={"X-Requested-By": ""},
                         auth=("admin", "admin"))
        print(r.text)
        return r.text, r.status_code
    except RequestException as e:
        return e


def get_indexes(addr):
    """get all indexes except active write"""
    try:
        r = requests.get(f"http://{addr}:9200/_cat/indices?format=json")
        lst_2 = []
        # print(r.json())
        check = check_active(addr)
        print(check)
        for i in r.json():
            if i["index"] not in check:
                lst_2.append(i["index"])
        print(f"Current indexes, except write, on {addr} are: ")
        print(sorted(lst_2))
        return sorted(lst_2)
    except RequestException as e:
        return e


def auto_increment(old_list: list):
    new_list = []
    for i in old_list:
        # print(i)
        i = i.split("_")
        num = i[1]
        # print(type(num))
        num = 1 + int(num)
        index = i[0] + "_" + str(num)
        # print(index)
        new_list.append(index)
    # print(new_list)
    print("Incremented indexes will be: ")
    return new_list

def create_index_targets(addr, index):
    """create locally target indexes as on remote machine
    TESTED
    """
    try:
        r = requests.put(f"http://{addr}:9200/{index}", json={"settings": {"number_of_shards": 1, "number_of_replicas": 0}})
        if r.status_code == 200:
            print(f"{index} was successfully created")
            return r.status_code, r.text
        else:
            print(f"{index} creation has failed")
    except RequestException as e:
        return e


def delete_index(addr, index):
    """delete locally target indexes on machine
    TESTED
    """
    r = requests.delete(f"http://{addr}:9200/{index}")
    if r.status_code == 200:
        print(f"{index} was successfully deleted")
        return r.status_code, r.text
    else:
        print(f"{index} deletion has failed")

def compare_index(addr1, addr2, index):
    """Compare index on remote and host
    TESTED
    """
    r = requests.get(f"http://{addr1}:9200/{index}/_count")
    if r.status_code == 200:
        print(f"---{index} on {addr1} have following struct----")
        print(r.json())
        print("------------------------------------------------")
    else:
        print("--------------------FAILED-----------------------")

    t = requests.get(f"http://{addr2}:9200/{index}/_count")
    if t.status_code == 200:
        print(f"----{index} on {addr2} have following struct----")
        print(t.json())
        print("-------------------------------------------------")
    else:
        print("---------------------FAILED----------------------")


def reindex_from_remote(addr1, addr2, index):
    """Reindex from remote"""
    session = requests.session()
    session.verify = True
    print(f"Reindexing {index} from remote {addr2} to local {addr1}")
    r = session.post(f"http://{addr1}:9200/_reindex?wait_for_completion=true", headers={"Content-Type": "application/json"},
                     json={"source": {"remote": {"host": f'http://{addr2}:9200'}, "index": f"{index}",
                      "size": 1000}, "dest": {"index": f"{index}"}})
    # r = requests.post(f"http://{addr1}:9200/_reindex?wait_for_completion=true", headers={"Content-Type": "application/json"},
    #                   timeout=300, json={"source": {"remote": {"host": f'http://{addr2}:9200'}, "index": f"{index}",
    #                   "size": 1000}, "dest": {"index": f"{index}"}})
    print(r.json())
    return r.json()


def update_index_range(addr, index):
    """Update index range for reindexed index"""
    try:
        r = requests.post(f"http://{addr}:9000/api/system/indices/ranges/{index}/rebuild", headers={"X-Requested-By": ""},
                         auth=("admin", "admin"))
        print(r.text)
        print(r.status_code)
    except RequestException as e:
        print(e)


if __name__ == "__main__":
    print("TASK LOOP STARTED!")

    remote_AWI = check_active("172.16.100.200")
    host = check_active("centos4")
    remote_new_AWI = auto_increment(remote_AWI)

    list_on_remote = get_indexes("172.16.100.200")
    # list_to_reindex = get_indexes("centos4")

    ans1 = input("IF proceed, indexes will be rotated on local host, yes/no:    ")
    if ans1 == "yes""":
        for i in remote_new_AWI:
            print(i)
            create_index_targets("centos4", i)

        update_template("centos4")  #обновляется шаблон, только если выполнялся апгрейд Грейлог версии
        ans2 = input("Following indexes will be created on local host and reindexed, yes/no:    ")
        print(list_on_remote)
        if ans2 == "yes":
            for i in list_on_remote:
                if "gl-events" in i or "gl-system-events" in i or "graylog" in i:
                    print(i)
                    create_index_targets("centos4", i)
                    reindex_from_remote("centos4", "172.16.100.200", i)
                    update_index_range("centos4", i)
                else:
                    print(f"This index is no from set {i}")
    else:
        print("Exiting..")
    print("TASK LOOP FINISHED!")
