import os


def nameclear():
    """Очищает название фото от первых случайных символов,
позволяя затем легко сортировать в папке по дате.
1) Использовать только для файлов напрямую с устройства.
2) Переименование jpg файлов с длиной названия 59 или 64 символа
например: "72oEmodg_20221206_110340_551_C16_main_panorama_FakeBelt.jpg" делает "20221206_110340_551_C16_main_panorama_FakeBelt.jpg"
"""
    ans = input("Убедитесь, что ваши файлы формата '72oEmodg_20221206_110340_551_C16_main_panorama_FakeBelt.jpg' !!! длиной или 59 или 64 символов:   yes/?")
    if ans == "yes" or "y":
        print("Выполнение операции")
        mylist = os.listdir()
        for i in mylist:
            if ".jpg" in i and ( len(i) == 59 or len(i) == 64):
                x = i.split("_")[1:]
                y = "_".join(x)
                os.rename(i, y)
            else:
                print(f"Проверка файла на условие провалилась!")
    else:
        print("Отмена операции")        


try:
    direct = input("Скопируйте сюда из проводника путь директории с файлами jpg:  ")
    os.chdir(direct)
    print("Директория найдена:  ", os.getcwd())
    nameclear()

except FileNotFoundError:
    print("Директория не найдена")
    
