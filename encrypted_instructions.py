# 105625664 - номер успешной посылки

def get_first_command(cmd: str) -> str:
    count_opn = 0
    count_cls = 0
    index_opn = 0
    index_cls = 0
    for i in range(len(cmd)):
        if cmd[i] == "[":
            if index_opn == 0:
                index_opn = i + 1
            count_opn += 1
        elif cmd[i] == "]":
            count_cls += 1
            index_cls = i

        if count_opn == count_cls and count_cls != 0:
            return cmd[index_opn: index_cls]

    raise Exception("corrupted command format")


def parse_command(cmd: str) -> str:
    """
        Функция расшифровывает сжатые сообщения и возвращает строку с командами.
        Параметры:
            cmd (str): строка. В строке могут быть буквы, числа и квадратные скобки.
        Возвращаемое значение:
            result (str): строка без квадратных скобок
    """

    result: str = ""
    i: int = 0
    while i < len(cmd):
        if cmd[i].isdigit():
            multiplier = get_full_digit(cmd[i: len(cmd)])
            inner_command = get_first_command(cmd[i: len(cmd)])
            result += multiply_string(int(multiplier), inner_command)
            i += len(inner_command) + len(multiplier) + 2
        elif cmd[i] == "[":
            inner_command = get_first_command(cmd[i: len(cmd)])
            result += parse_command(inner_command)
            i += len(inner_command) + 2
        else:
            result += cmd[i]
            i += 1
    return result


def multiply_string(multiplier: int, cmd: str) -> str:
    result: str = ""
    cmd = parse_command(cmd)
    for i in range(multiplier):
        result += cmd
    return result


def get_full_digit(cmd: str) -> str:
    result = ""

    for i in range(len(cmd)):
        if cmd[i].isdigit():
            result += cmd[i]
        else:
            break
    return result


def main():
    command = [i for i in input()]
    print(parse_command(command))


if __name__ == '__main__':
    main()

