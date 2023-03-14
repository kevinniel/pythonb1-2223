print("hello world")

toto = 3

print(toto)

if (toto < 1):
    print("if")
else:
    print("else")

print("en dehors du ifelse")

# 3 types de tableaux
# liste
tab1 = [
    1,
    2,
    3
]
# dictionnaire
tab2 = {
    1: "a",
    2: "b",
    3: "c"
}
# tuple
tab3 = (
    1,
    2,
    3
)
print(tab1)
print(tab2)
print(tab3)

# boucle liste (meme pour tuple)
for i in tab1:
    print(i)

# boucle dictionnaire
for cle, valeur in tab2.items():
    print(cle, valeur)