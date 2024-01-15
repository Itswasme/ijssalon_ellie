
from algemene_functies import mijn_functie_2


aanbieding_1={
"smaak":"aardbei",
"prijs":4 , 
"korting":0.1
} 

print(f"Vandaag in de aanbieding : emmertje ijs (1 liter) in de smaak {aanbieding_1['smaak']}, van {aanbieding_1['prijs']} euro voor {(aanbieding_1['prijs']*(1-aanbieding_1['korting'] ))} euro.")


inkomsten_totaal={
"inkomsten":[220,430,125,160,205,90,345]
}
inkomsten_totaal.update({
"inkomsten":[220,430,125,160,205,90,345],
"btw":0.09
})
totaal=(sum(inkomsten_totaal["inkomsten"]))

print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*inkomsten_totaal["btw"]} euro btw betaald dient te worden")


laag_hoog={
"mijn_lijst":[220, 430, 125, 160, 205, 90, 345]
}

maxi=max(laag_hoog["mijn_lijst"])
mini=min(laag_hoog["mijn_lijst"])

print(str(maxi)+","+str(mini))

mean=sum(laag_hoog["mijn_lijst"])/len(laag_hoog["mijn_lijst"])
print(mean)

print(f"De gemiddelde inkomsten deze week zijn {int(mean)} euro.")


'''mijn_functie_2={
12.3:[15,9,36,4],
12.2:[14, 10, 24, 6],
10.5:[15, 5, 50, 2],
100.20:[120, 80, 2000, 5]
}'''


meervoudig={
"invoer_lijst":[10,5,3,2,1,2,9]
}

def laag_hoog(mijn_lijst):
    return max("mijn_lijst"), min("mijn_lijst")

def meervoudig(invoer_lijst):
    return laag_hoog("mijn_lijst")


def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig("invoer_lijst")
    return mijn_functie_2(korte_lijst)

