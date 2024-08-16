import asyncio
from dict.lexicon_ru import lexicon

from config_reader import config


def open_file(path: str, number: int = 1) -> list:
    if number == 1:
        number = 0
    else:
        number = 10*(number-1)
    path = f"{config.path}{path}.txt"
    with open(path, "r") as file:
        d = file.readlines()
    s = ""
    for i in range(number, min(number+10, len(d))):
        s += str(i+1)+") "+d[i]
    if s == "" or s.isspace():
        return lexicon["quote_1"]
    else:
        return s

def len_file(path: str, number: int | None = None) -> bool | int:
    path = f"{config.path}{path}.txt"
    with open(path, "r") as file:
        d = file.readlines()
    if number == 0 or number:
        return abs(-len(d)//10) > number > 0
    else:
        return len(d)

def delete_lines(path: str, numbers: str) -> int:
    try:
        path = f"{config.path}{path}.txt"
        if numbers.strip()[0] == "-":
            return 0
        numbers = list(map(lambda x: int(x), numbers.split("-")))
        with open(path, "r") as file:
            d = file.readlines()
            if len(numbers) == 1:
                a = numbers[0]
                if a == 0:
                    a = 0
                else:
                    a -= 1
                d.pop(a)
            else:
                a, b = min(numbers), max(numbers)
                if a == 0:
                    a = 1
                else:
                    a -= 1
                for i in range(a, b):
                    d.pop(a)
        with open(path, 'w') as file:
            file.writelines(d)
        return 1
    except ValueError:
        return 2
    except IndexError:
        return 3

def append_lines(path: str, line: str) -> bool:
    path = f"{config.path}{path}.txt"
    line = f"{line}\n"
    try:
        with open(path, "a") as file:
            file.write(line)
        return True
    except:
        return False