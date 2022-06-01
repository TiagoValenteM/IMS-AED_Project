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
