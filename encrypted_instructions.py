# ___________________________ - номер успешной посылки

def encrypted_instructions(instructions: list) -> list:
    """
    Функция расшифровывает сжатые сообщения и возвращает строку с командами.

        Параметры:
            instructions (list): строка. В строке могут быть только
            буквы, числа и квадратные скобки.

        Возвращаемое значение:
            decrypted_message (list): строка. Полная форма команды
    """





def main():
    instructions = [str(i) for i in input().split()]
    print(encrypted_instructions(instructions))


if __name__ == '__main__':
    main()

