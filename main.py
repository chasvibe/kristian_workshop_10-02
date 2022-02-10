from pathlib import Path

this_list = []
path = Path.cwd() / "input.txt"
with path.open(mode="r", encoding="utf-8") as file:
    input_line = file.readlines()
    for line in input_line:
        this_list.append(line.replace("\n", ""))


def input_list(in_list):
    for item in in_list:
        for new in in_list:
            if int(item) + int(new) == 2020:
                return f"{item} : {new} : {int(item) * int(new)}"


if __name__ == '__main__':
    result = input_list(this_list)
    print(result)