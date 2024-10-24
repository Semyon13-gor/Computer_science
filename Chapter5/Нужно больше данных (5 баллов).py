def can_download(per, data):
    if "*_deny" in per:
        return False
    if "*_allow" in per and f"{data}_deny" not in per:
        return True
    if f"{data}_allow" in per and f"{data}_deny" not in per:
        return True
    if f"{data}_deny" in per:
        return False



permissions = { "books_allow", "movies_deny" }
print(can_download(permissions, "movies"))  # => False
print(can_download(permissions, "books"))   # => True

permissions = { "*_allow", "books_allow", "movies_deny" }
print(can_download(permissions, "games"))    # => True

permissions = { "*_allow", "*_deny" }
print(can_download(permissions, "movies"))    # => False


