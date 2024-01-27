# 105912573 - номер успешной посылки

def parse_command(cmd: str) -> str:
    """ Разбор строки на команды """
    full_digit: str = ""
    cmd_pool: list = [["", ""]]
    for char in cmd:
        if char.isdigit():
            full_digit += char

        elif char == "[":
            cmd_pool.append([full_digit, ""])
            full_digit = ""

        elif char == "]":
            multiplier, token = cmd_pool.pop(len(cmd_pool) - 1)
            s = multiplication(int(multiplier), token)
            cmd_pool[len(cmd_pool) - 1][1] += s

        else:
            cmd_pool[len(cmd_pool) - 1][1] += char
    return cmd_pool[0][1]


def multiplication(multiplier: int, token: str) -> str:
    """ Повторитель строк """
    result: str = ""
    for i in range(multiplier):
        result += token
    return result


def main():
    cmd = input()
    print(parse_command(cmd))


if __name__ == '__main__':
    main()
