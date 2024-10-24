with open("iban_lenght.txt", "rt") as file: d = {line[:2]: line[2:].strip() for line in file}
