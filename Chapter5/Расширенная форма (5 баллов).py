
def expandedForm(num):
    lenght = len(str(num)) - 1
    resl = []
    for i in range(lenght + 1):
        nus = num
        nus = nus // 10**lenght
        resl.append(str(nus) + "0" * lenght)
        num = num % 10**lenght
        lenght -= 1
    res = ""
    for i in range(len(resl)):
        if i == len(resl) - 1:
            res += resl[i]
            continue
        if int(resl[i]) != 0:
            res += resl[i] + " + "
    return res
print(expandedForm(12)) # "10 + 2"
print(expandedForm(42)) # "40 + 2"
print(expandedForm(70304)) # "70000 + 300 + 4"
