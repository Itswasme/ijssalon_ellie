def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

'''
mijn_string=("waterijsje")
mijn_string1=mijn_string.replace("a","")
mijn_string2=mijn_string1.replace("t","")
for l in mijn_string2:
    print(l)'''


'''b = 2
def mijn_functie():
    global b  
    b = b + 10  
    print("binnen: ", b)
print("buiten: ", b)
mijn_functie()
mijn_functie()
print("buiten: ",b)
print("buiten: ",b)'''


'''def fooi_pp(bedrag, persoon):
    bedrag_pp=bedrag/persoon
    return f"het bedrag per persoon is {bedrag_pp} euro"

b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))

print(fooi_pp(b,p))'''

mijn_functie_2={
12.3:[15,9,36,4],
12.2:[14, 10, 24, 6],
10.5:[15, 5, 50, 2],
100.20:[120, 80, 2000, 5]
}