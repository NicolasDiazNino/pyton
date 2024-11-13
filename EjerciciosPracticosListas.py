nombres = ["Pedro", "Juan", "Mar", "lopez", "Andrea"]

nombres.append("Alejandro")
nombres.insert(2, "Lucas")

print(nombres)

nombres[1] = "Carlos"
print(nombres)

nombres.pop()
print(nombres)

for nombre in nombres:
    print("Tengo un amigo que se llama", nombre)