def calculate_information(input_info):
    alphabet_length = input_info[0]
    lines_on_page = input_info[1]
    symbols_in_line = input_info[2]
    power = 1
    while 2**power < alphabet_length:
        power += 1
    bits_per_character = power
    symbol_amount = lines_on_page * symbols_in_line * 2
    information_on_page = symbol_amount * bits_per_character
    result = f"{information_on_page} бит"
    return result


print(calculate_information((int(input("Кол-во букв в алфавите: ")), int(input("Кол-во строк на странице: ")),
                             int(input("Кол-во символов в строке: ")))))
