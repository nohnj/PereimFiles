import os
import shutil
import random
from pathlib import Path
from PIL import Image

new_dir_name = "Бубис"
name_generator = 0
debug_dir = Path("C:/Серьёзное дело/Переименовываем/" + str(new_dir_name))
parent_dir = Path("C:/Серьёзное дело/Переименовываем")
path = parent_dir / new_dir_name

def is_directory_empty(directory):
    for file in os.listdir(directory):
        if not os.path.islink(file) and not os.path.isdir(file):
            return False
    return True

if not parent_dir.exists():
    raise FileNotFoundError(f"{parent_dir} не существует, идиот")
if path.exists():
    shutil.rmtree(str(path))
try:
    path.mkdir()
    print(f"Папка {new_dir_name} создана в {parent_dir}")
except FileExistsError:
    if is_directory_empty(debug_dir) == True:
        print(f"Папка {new_dir_name} из {debug_dir }пуста. Начинаю работу\n")
    else:
        while is_directory_empty == False:
            new_dir_name = "Бубис" + str(name_generator)
            path.mkdir()

i = 0
ext = ["jpg","webp","jpeg"]

try:
    for file in os.listdir(parent_dir):
        if file.endswith(ext[0]):
            os.rename(fr'{parent_dir}/{file}', fr'{debug_dir}/{i}.png')
            print(fr'{file} moved form {parent_dir} to {debug_dir} as {i}.png')
            i += 1
        elif file.endswith(ext[1]):
            os.rename(fr'{parent_dir}/{file}', fr'{debug_dir}/{i}.png')
            print(fr'{file} moved form {parent_dir} to {debug_dir} as {i}.png')
            i += 1
        elif file.endswith(ext[2]):
            os.rename(fr'{parent_dir}/{file}', fr'{debug_dir}/{i}.png')
            print(fr'{file} moved form {parent_dir} to {debug_dir} as {i}.png')
            i += 1
        else:
            os.rename(fr'{parent_dir}/{file}', fr'{debug_dir}/{i}.{os.path.splitext(file)[1][1:]}')
            print(fr'{file} moved form {parent_dir} to {debug_dir} as {i}.png')
            i += 1
except OSError:
    print('\nSomething went wrong')

shufflee = 0
shuffle_ls = []
Shuffle = input('Would you like to shuffle files?(y/n) \n ')
if Shuffle.lower == 'yes' or 'y':
    for y in range(i):
        shuffle_ls.append(y)
        random.shuffle(shuffle_ls)
    for file in os.listdir(debug_dir):
        # try:
        os.rename(fr'{parent_dir}/Бубис/{i}.{os.path.splitext(file)[1][1:]}', fr'{parent_dir}/{shuffle_ls[shufflee]}.{os.path.splitext(file)[1][1:]}')
        print(fr'{file} moved form {parent_dir} to {debug_dir} as {i}.png')
        # except OSError:
        #     print('\nSomething went wrong\n')
        shufflee += 1
    # shutil.rmtree(debug_dir)
    print("Thanks for using dis shit yo. Ima like puttd ma soul init")
elif Shuffle.lower == 'no' or 'n':
    print("GO FUCK YOURSELF")
    breakpoint()
else:
    print("https://support.microsoft.com/ru-ru/windows/использование-клавиатуры-18b2efc1-9e32-ba5a-0896-676f9f3b994f")
    breakpoint()
