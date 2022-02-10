from pathlib import Path

this_list = []
path = Path.cwd() / "input.txt"
with path.open(mode="r", encoding="utf-8") as file:
    input_line = file.readlines()
    for line in input_line:
        this_list.append(line.replace("\n", ""))


def input_list(in_list):
    for item1 in in_list:
        for item2 in in_list:
            for item3 in in_list:
                if int(item1) + int(item2) + int(item3) == 2020:
                    return f"{item1} : {item2} : {item3} : {int(item1) * int(item2) * int(item3)}"


if __name__ == '__main__':
    result = input_list(this_list)
    print(result)