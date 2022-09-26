combs = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print (combs)




# Puedo realizar ese código en una única línea.
# Asigno a una variable el siguiente código: [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y].
