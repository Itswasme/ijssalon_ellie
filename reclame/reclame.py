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

