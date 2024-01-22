# ___________________________ - номер успешной посылки

def build_string(str_char: str, str_digit: str) -> str:
    result = ''
    for number in range(int(str_digit)):
        result += str_char
    print(result)




def unpacker(stack: str) -> str:
    str_digit = ''
    str_char = ''
    result = ''
    digit_flag = 0

    for idx in range(len(stack)-1, -1, -1):
        if not stack[idx].isdigit():
            if digit_flag == 1:
                build_string("".join(reversed(str_char)), "".join(reversed(str_digit)))
                digit_flag = 0
                str_char = ''
                str_digit = ''
            str_char += stack[idx]
        else:
            str_digit += stack[idx]
            digit_flag = 1
    print(str_char, str_digit)



def encrypted_instructions(instructions: list) -> list:
    """
    Функция расшифровывает сжатые сообщения и возвращает строку с командами.

        Параметры:
            instructions (list): строка. В строке могут быть только
            буквы, числа и квадратные скобки.

        Возвращаемое значение:
            decrypted_message (list): строка. Полная форма команды
    """
    open_bracket = '['
    close_bracket = ']'
    cnt_open_br = 0
    cnt_close_br = 0
    stack = []

    for idx in range(len(instructions)):
        if instructions[idx] == open_bracket:
            cnt_open_br += 1
        elif instructions[idx] == close_bracket:
            cnt_close_br += 1
        else:
            stack.append(instructions[idx])
            print(instructions[idx], end='')
        if cnt_open_br == cnt_close_br != 0:
            result = unpacker(stack)
            print(result)

def main():
    instructions = [str(i) for i in input()]
    encrypted_instructions(instructions)


if __name__ == '__main__':
    main()

