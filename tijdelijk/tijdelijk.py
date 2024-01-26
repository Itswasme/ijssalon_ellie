from algemene_functies.helper import decoreer

def print_aanbieding():
    prijzen ={
        "aardbei":3,
        "vanille":4,
        "chocolade":5
    } 
    huidige_prijs= prijzen["aardbei"]
    aanbieding1=huidige_prijs*0.8
    reclame_tekst=f"vandaag in de aabieding: vanille-ijs, 1 liter - slechts € {aanbieding1}"

    reclame_tekst2=reclame_tekst[:62]

    reclame_tekst3=reclame_tekst2.upper()

    reclame_tekst4=reclame_tekst3.split()


    for el in reclame_tekst4:
        if len(el) < 4:
            print(el.lower())
        else:
            print(el.upper())
            
decoreer("Aanbieding")
print_aanbieding()
decoreer("Aanbieding")