sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

fish = []
n = []
for j in sea_fish:
    fish.append(j.capitalize())
for i in freshwater_fish:
    fish.append(i.capitalize())
fish = sorted(fish)
for i in range(0, len(fish)):
    for j in range(0, len(sea_fish)):
        if fish[i] == sea_fish[j].capitalize():
            fish[i] = sea_fish[j]
print(fish)