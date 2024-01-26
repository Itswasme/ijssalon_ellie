from boekhouding import *

mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}


def presenteer(inkomsten, totaal_inkomsten):
    for item, waarde in inkomsten.items():
        print(f"{item} : {waarde} euro")

presenteer(inkomsten, totaal_inkomsten)

print("===========================")

print(f"totaal: {totaal_inkomsten} euro")



