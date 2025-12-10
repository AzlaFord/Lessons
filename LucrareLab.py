import random

# completare directă
A = {12, "ziua_15", "luna_04", "anul_2004", 9, 8, 10, "Oracle", "SQL", "DBA"}

# completare random
B = set()
while len(B) < 10:
    B.add(random.randint(1, 20))
B.add(8)
B.add("ziua_15")

# completare de la tastatură
C = set()
n = int(input("Introduceți numărul de elemente pentru C: "))
for i in range(n):
    x = input("Element = ")
    C.add(x)

print("Mulțimea A:", A)
print("Mulțimea B:", B)
print("Mulțimea C:", C)

print("Reuniune A și B:", A.union(B))
print("Intersecție A și B:", A.intersection(B))
print("Diferență A minus B:", A.difference(B))

oracle = {
    "Oracle Database": "sistem de gestiune a bazelor de date",
    "SQL": "limbaj de interogare",
    "PL/SQL": "limbaj procedural Oracle",
    "DBA": "administrator al bazei de date",
    "Schema": "colecție de obiecte",
    "Tablespace": "spațiu de stocare",
    "Instance": "procesarea bazei de date în RAM",
    "Redo Log": "jurnal de modificări",
    "Backup": "copiere de securitate",
    "Recovery": "restaurarea datelor",
}

print("\nDicționar Oracle Database:")
for k, v in oracle.items():
    print(k, "=", v)

oracle["Backup"] = "copiere periodică"
oracle["RAC"] = "cluster Oracle"
del oracle["Redo Log"]

print("\nDicționar modificat:", oracle)
