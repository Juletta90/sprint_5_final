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

    # наилучшим решением будет использование стека и постоянное удаление
    # элементов в нем, если скобки открывающаяся и закрывающаяся совпадают,
    # то они очищаются из стека и так до тех пор, пока он не окажется пустым.

    open_bracket = ['[']
    close_bracket = [']']
    #bracket = {']': '['}  # или словарь?
    stack = []

    i = 0  # индекс текущего символа

    # для каждого символа строки:
    for i in instructions:
        # проверить, является ли символ числом
        num_list = [int(num) for num in filter(
            lambda num: num.isnumeric(), instructions)]
        if i+1 == open_bracket:

        #if i.isnumeric():   #type(i) == int:
            #pass #if j in open_bracket:
             #   stack.append(i*j)


def main():
    instructions = [i for i in input().split()]  # преобразование строки в список
    print(encrypted_instructions(instructions))


if __name__ == '__main__':
    main()

