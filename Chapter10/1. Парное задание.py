def DeSh(shifr):
    message = ""
    for i in range(1, 27):
        for ch in shifr:
            message += chr(ord(ch) - i)
        print(message, i)
        message = ""
sh = "pqlb"
DeSh(sh)