from random import randint

def iteration_add(ini, inc, ite):
    for i in range(ite):
        if i == 0:
            ini = ini
        else:
            inc = i*inc
            ini.append(inc)
    return ini

def list_initial (ini_size):
    ini_size= str(ini_size)
    ini_size = ini_size.upper()
    for i in ini_size:
        if i == "K":
            ini_size = ini_size.replace("K","000")
        elif i == "M":
            ini_size = ini_size.replace("M", "000000")
        elif i == "B":
            ini_size = ini_size.replace("B","000000000")
    ini_size = int(ini_size)
    random_list = [randint(0,1000) for i in range(ini_size)]
    return random_list

def list_iti (inc_size):
    inc_size= str(inc_size)
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
