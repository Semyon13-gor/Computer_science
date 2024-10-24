meme = dict()
def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n > 2:
        if n in meme:
            return meme[n]
        else:
            meme[n] = f(n - 1) + f(n - 2)
            return meme[n]
print(f(60))
