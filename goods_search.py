import mysql.connector
from mysql.connector import errorcode as err
import json

try:
    # passw = input("enter password: ")
    # ruaChie1ie
    con = mysql.connector.connect(user="nekituall", password="ruaChie1ie", host="127.0.0.1", port=3309, database='din')
    # print("connected")
    cur = con.cursor()
    query = """
          SELECT s.id, w.entityId, w.`type`, w.content
          FROM  sites AS s
          JOIN widgets AS w ON s.id = w.siteId
          AND w.`type` = 89 AND w.isDeleted = 0
          WHERE s.isdeleted = 0 AND s.id NOT IN (1025634, 1455224, 1218083, 1297637) AND s.isActive = 1;
          """
    cur.execute(query)
    my_list = []
    for i in cur:
        if len(i[3]) != 0:
            obj = json.loads(i[3].decode(encoding="utf-8"))
            # print(json.dumps(obj["items"], indent=4))
            for item in obj["items"]:
                if "alignment" not in item["desc"]:
                    # print(obj)
                    my_list.append(i[:3])
                    break
    for num, i in enumerate(my_list):
        print(num, i)
except err:
    print(err)
else:
    con.close()
