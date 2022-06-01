from random import randint


def iteration_add(ini, inc, ite):
    new_el_count = inc * ite

    for i in range(new_el_count):
        if i == 0:
            ini = ini
        else:
            new_element = ite * inc
            for number in new_element:
                ini.append(number)
    return ini


def user_input(ini_size):
    ini_size = str(ini_size)
    ini_size = ini_size.upper()
    for i in ini_size:
        if i == "K":
            ini_size = ini_size.replace("K", "000")
        elif i == "M":
            ini_size = ini_size.replace("M", "000000")
        elif i == "B":
            ini_size = ini_size.replace("B", "000000000")
    ini_size = int(ini_size)
    return ini_size


def list_iti(inc_size):
    inc_size = str(inc_size)
    inc_size = inc_size.upper()
    for i in inc_size:
        if i == "K":
            inc_size = inc_size.replace("K", "000")
        elif i == "M":
            inc_size = inc_size.replace("M", "000000")
        elif i == "B":
            inc_size = inc_size.replace("B", "000000000")
    inc_size = int(inc_size)
    return inc_size
