import time



def insert():
        files = []
        mark = True
        while mark:
                x = input("Продолжить ввод файлов?? yes/no   ")
                if x == "yes" or x == "y":
                        file = input("Введите имя файла с расширением csv:  ")  #тут код дальше по добавлению
                        if ".csv" in file:
                                files.append(file)
                                print(f"файл {file} добавлен в очередь")
                        else:
                                print("Неверный формат")
                elif x == "no" or x == "n":
                    mark = False #тут выход из цикла
                else:
                    print("Повторите ввод, неверный вариант") #это сообщение об ошибке
                    
        print("Итого добавлены файлы: ", files)
        return files

def copy(n):
        """ функция открывает файл для копирования"""
        with open(n, mode="r") as f:
                print(f"Файл {n} найден")
                read_data = f.read()
        return read_data

def write(m):
        """ функция записывает в выходной файл """
        with open("output.csv", mode ="a") as v:
                output_data = v.write(str(m))
        
def logtxt(k):
        """функция пишет в журнал инфу"""
        with open("log.txt", mode = "a") as lg:
                x = f"{k} был скопирован в {time.ctime()}"
                log_data = lg.writelines(x + "\n")
                print("запись в журнал сделана")


##вызовы ниже
files = insert()
state = input("Выполняем запись ?? yes/no  ")
if state == "yes" or state == "y":
        for i in files:
                try:
                        a = copy(i)
                        write(a)
                        logtxt(i)                               

                except FileNotFoundError:
                        print(f"Файл {i} не найден")
                        logtxt(i)                                                                                            
else:
        print("Запись не выполняется")

        


                
