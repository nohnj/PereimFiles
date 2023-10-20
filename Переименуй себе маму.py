import os
import re
import sys
import shutil
import random
from pathlib import Path
from PIL import Image

ext = ["jpg","webp","jpeg"]

parent_dir = Path("C:/Серьёзное дело/Переименовываем")
new_dir_name = "Бубис"

if not parent_dir.exists():
    raise FileNotFoundError(f"{parent_dir} не существует, идиот")

path = parent_dir / new_dir_name

if path.exists():
    shutil.rmtree(str(path))

path.mkdir()

print(f"Папка {new_dir_name} создана в {parent_dir}")

i = 0

for file in os.listdir(parent_dir):
    if file.endswith(ext[0]):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/Бубис/{i}.png')
        print(file)
        i += 1
    elif file.endswith(ext[1]):
        os.rename(fr'{parent_dir}/{file}', fr'{os.listdir()}/Бубис/{i}.png')
        print(file)
        i += 1
    elif file.endswith(ext[2]):
        os.rename(fr'{parent_dir}/{file}', fr'{os.listdir()}/Бубис/{i}.png')
        print(file)
        i += 1
    else:
        os.rename(fr'{parent_dir}/{file}', fr'{os.listdir()}/Бубис/{i}.{os.path.splitext(file)[1][1:]}')
        print(file)
        i += 1


for file in os.listdir(parent_dir):
    if file.endswith(ext[0]):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{i}.png')
        print(file)
        i += 1
    elif file.endswith(ext[1]):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{i}.png')
        print(file)
        i += 1
    elif file.endswith(ext[2]):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{i}.png')
        print(file)
        i += 1
    else:
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{i}.png')
        print(file)
        i += 1


shufflee = 0
shuffle_ls = []
Shuffle = input('Would you like to shuffle files?(y/n) \n\n ')
if Shuffle.lower == 'yes' or 'y':
    for y in range(i):
        shuffle_ls.append("shuffle"+str(y))
        random.shuffle(shuffle_ls)
    for file in os.listdir(parent_dir):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{shuffle_ls[shufflee]}.{os.path.splitext(file)[1][1:]}')
        print(file)
        shufflee += 1
    shufflee = 0
    shuffle_ls = []
    for y in range(i):
        shuffle_ls.append(y)
        random.shuffle(shuffle_ls)
    for file in os.listdir(parent_dir):
        os.rename(fr'{parent_dir}/{file}', fr'{parent_dir}/{shuffle_ls[shufflee]}.{os.path.splitext(file)[1][1:]}')
        print(file)
        shufflee += 1
    print("Thanks for using dis shit yo. Ima like puttd ma soul init")
elif Shuffle.lower == 'no' or 'n':
    print("GO FUCK YOURSELF")
    breakpoint()
else:
    print("https://support.microsoft.com/ru-ru/windows/использование-клавиатуры-18b2efc1-9e32-ba5a-0896-676f9f3b994f")
    breakpoint()