def Sc(pos, orien, word):
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    if orien == "v":
        if len(word) <= len(d) - d.index(pos[0]):
            return True
        else:
            return False
    if orien == "h":
        p = list(pos)
        del p[0]
        p = "".join(p)
        if len(word) <= 16 - int(p):
            return True
        else:
            return False
print(Sc("G7", "v", "gosdfghjk"))
