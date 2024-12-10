def encode(message, key):
    ende = ""
    for s in message:
        news = ""
        for i in range(0, len(key), 2):
            if s == key[i]:
                news = key[i + 1]
            elif s == key[i+1]:
                news = key[i]
            elif s == key[i].upper():
                news = key[i + 1].upper()
            elif s == key[i + 1].upper():
                news = key[i].upper()
        if news == "":
            news = s
        ende += news
    return ende


def decode(encrypted_message, key):
    dede = ""
    for s in encrypted_message:
        news = ""
        for i in range(0, len(key), 2):
            if s == key[i]:
                news = key[i + 1]
            elif s == key[i+1]:
                news = key[i]
            elif s == key[i].upper():
                news = key[i + 1].upper()
            elif s == key[i + 1].upper():
                news = key[i].upper()
        if news == "":
            news = s
        dede += news
    return dede
    pass



print(encode("ABCD", "agedyropulik"))            # => GBCE
print(encode("Ala has a cat", "gaderypoluki"))    # => Gug hgs g cgt
print(decode("Dkucr pu yhr ykbir","politykarenu")) # => Dance on the table
print(decode("Hmdr nge brres","regulaminowy"))     # => Hide our beers