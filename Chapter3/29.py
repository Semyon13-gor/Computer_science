string = "AGCTGTATCGGGTTAACCTA"
c = 0
p = ((string.count("G") + string.count("C")) / len(string)) * 100
print(p)

d = {
    "T": "A",
    "C": "G",
    "A": "T",
    "G": "C"
}
p = "TGGATCCA"
pk = ""
for i in p:
    pk += d[i]
print(pk)
if p == "".join(reversed(pk)):
    print("является палиндромом")
else:
    print("не является палиндромом")
