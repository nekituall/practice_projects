import time


def menu():
    """manin menu func"""

    var = int(input("List of available commands: \n 1.add \n 2.list all "
                    "\n 3.list by date \n 4.list by category \n "
                "5.exit\n\n Enter command number (e.g. 2):  "))
    while True:
        if var == 1:
            add()
            break
        elif var == 2:
            list_all()
            break
        elif var == 3:
            list_by_date()
            break
        elif var == 4:
            list_by_type()
            break
        elif var == 5:
            break
        else:
            print("Command not found!")
            case()


def add():
    """Good addition func
    partnumber -->string
    price --> float
    quantity --> int
    """

    cat = int(input("\nList of available categories: \n 1.Truck \n 2.Industrial "
                    "\n 3.Marine \n\n Enter category number:  "))

    if cat == 1:
        cat1 = "Truck"
    elif cat == 2:
        cat1 = "Industrial"
    elif cat == 3:
        cat1 = "Marine"
    else:
        print("Invalid category!!!")
        add()

    var0 = str(input("Enter partnumber:  "))
    var1 = float(input("Enter price:  "))
    var2 = int(input("Enter available quantity:  "))
    var3 = time.strftime('%Y/%m/%d')
    line = str(f"{var0},{cat1},{var1},{var2},{var3}")
    write(line)
    menu()


def list_all():
    """List all lines func"""
    try:
        with open("goodsprojectdata.csv", mode="r") as f:
            for row in f:
                print(row.strip().split(","))
        case()
    except FileNotFoundError:
        print("Corresponding datafile not found! Must add goods to create!")
    finally:
        menu()


def list_by_date():
    """List rows by date func"""
    var = input("Enter date like YYYY/MM/DD:  ")
    with open("goodsprojectdata.csv", mode="r") as f:
        for row in f:
            x = row.strip().split(",")
            if var in x[4]:
                 print(x)
            else:
                print(f"No data for date {var}")
                break
    case()


def list_by_type():
    """List rows by goods category func"""

    var = int(input("List of available categories:\n 1.Truck \n 2.Industrial \n 3.Marine \n Enter category number:  "))
    if var == 1:
        cat = "Truck"
    elif var == 2:
        cat = "Industrial"
    elif var == 3:
        cat = "Marine"
    else:
        print("Invalid input!")
        case()


    with open("goodsprojectdata.csv", mode="r") as f:
        for row in f:
            x = row.strip().split(",")

            if cat in x[1]:
                print(x)
            else:
                print("Invalid category!")

    case()


def write(line):
    with open("goodsprojectdata.csv", mode="a") as f:
        f.writelines(line)
    print("Data has been written")
    time.sleep(2)


def case():
    case = input("Exit program? : yes/no   ")
    if case == "yes" or case == "y":
        exit()
    else:
        menu()


if __name__ == "main":
    print("Hello user!")
    menu()