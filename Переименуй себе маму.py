import os
import shutil
import random
from pathlib import Path

def is_directory_empty(directory):
    for file in os.listdir(directory):
        if not os.path.islink(file) and not os.path.isdir(file):
            return False
    return True

i = 0
ext = ["jpg","webp","jpeg"]
dir_name = "Бубис"
name_generator = 0
debug_dir = Path("C:/Серьёзное дело/Переименовываем/" + str(dir_name))
parent_dir = Path("C:/Серьёзное дело/Переименовываем")
path = parent_dir / dir_name

if debug_dir.exists():
    shutil.rmtree(debug_dir)
    debug_dir.mkdir()

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
    print('\nSuccess')

i = 0
shufflee = 0
shuffle_ls = []
Shuffle = input('Would you like to shuffle files?(y/n) \n ')

if Shuffle.lower() == 'y':
    for file in os.listdir(debug_dir):
        shuffle_ls.append(os.path.splitext(file)[0])
    random.shuffle(shuffle_ls)
    for file in os.listdir(debug_dir):
        try:
            os.rename(fr'{debug_dir}/{file}', fr'{parent_dir}/{shuffle_ls[shufflee]}.{os.path.splitext(file)[1][1:]}')
            print(f'{file} moved from {debug_dir} back to {parent_dir} as {shuffle_ls[shufflee]}.{os.path.splitext(file)[1][1:]}')
            i += 1
        except FileNotFoundError:
            print('\nSomething went wrong\n')
        shufflee += 1
    shutil.rmtree(debug_dir)
    print("Thanks for using dis shit yo. Ima like puttd ma soul init")

elif Shuffle.lower() == 'n':
    for file in os.listdir(debug_dir):
        try:
            fael = file
            os.rename(fr'{debug_dir}/{fael}', fr'{parent_dir}/{fael}')
            print(f'{fael} moved from {debug_dir} back to {parent_dir} as {fael}')
        except FileNotFoundError:
                print('\nI couldnt find the thing')
    shutil.rmtree(debug_dir)
    print("Its not perfectly the same BUT ITS ONLY YOUR FAULT\nGO FUCK YOURSELF")

else:
    print("https://support.microsoft.com/ru-ru/windows/использование-клавиатуры-18b2efc1-9e32-ba5a-0896-676f9f3b994f")
