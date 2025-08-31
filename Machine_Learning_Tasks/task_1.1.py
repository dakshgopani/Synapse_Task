from itertools import combinations

pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

k = int(input("Enter the value of k : "))
count = 0
l = list(pokedex.items())
best_team = []
best_types = []

for i in combinations(l, k):
    types = set()
    names = []
    for n, t in i:
        names.append(n)
        types.update(t if isinstance(t, tuple) else (t,))
        #print(names)
        #print(types)

    if len(types) > (len(best_types[0]) if best_types else 0):
        best_team = [names]
        best_types = [types]
        count = 1
    elif len(types) == (len(best_types[0]) if best_types else 0):
        best_team.append(names)
        best_types.append(types)
        count += 1

print("One of the Strongest team:", best_team[0])
print("Types covered by that team:", best_types[0])
print("Total unique types of that team:", len(best_types[0]))
print(f"Total strongest teams for k = {k} are :", count)
