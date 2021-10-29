#Mertcan Yildirim. Het moet een team worden van helden boven de 16, die allemaal flexibel, positief en doorzettend zijn. Verzin hiervoor 4 criteria met minimaal 4 vragen.
#Het eerste teamlid is de beer. Dus beresterk en doet het zware werk. (verzin 2 criteria met bijbehorende vragen, geen ja/nee vragen).
#Het tweede teamlid  is de vos. Dus erg slim in het oplossen van praktische problemen en in het vangen van dieren. (verzin 2 criteria met bijbehorende vragen, geen ja/nee vragen)
#Het derde teamlid is de bever. Dus erg handig in het bewerken van materialen en het construeren en bouwen van hutten en andere hulpmiddelen. (verzin 2 criteria met bijbehorende vragen, geen ja/nee vragen)
#Het vierde teamlid is de uil. Dus heeft veel kennis van de bruikbaarheid van natuurlijke materialen voor eten, drinken, genezen, verwarmen en beschermen. Ook de kennis van water zuiveren heeft hij/zij. (verzin 4 criteria met bijbehorende vragen, geen ja/nee vragen)
Leeftijd = int(input('Hoe oud bent u? '))
flex = input('Bent u flexibel? j/n ')
positief = input('Bent u positief? j/n ')
doorzettend = input('Bent u doorzettend persoon? j/n ')
if Leeftijd <16 or flex == 'n' or positief == 'n' or doorzettend == 'n':
    print('U bent niet geschikt, Helaas!')
else:
    sterk = int(input('Hoeveel kilo kunt u drukken? '))
    sterkk = sterk >100
    zwaar = input('Wat voor werk houdt u van? zwaar of licht: ')
    zwaark = zwaar == 'zwaar'
    slim = input('Hoe bent in oplossen van problemen? G of S: ')
    slimk = slim == 'G'
    vangen = input('Hoe bent u in het vangen van dieren? G of S: ')
    vangenk = vangen == 'G'
    bewerken = input('Hoe bent u in het bewerken van materialen? G of S: ')
    bewerkenk = bewerken == 'G'
    bouwen = input('Hoe bent u in bouwen van hutten of andere hulpmiddelen? G of S: ')
    bouwenk = bouwen == 'G'
    kennis = input('Wat is uw kennis in bruikbaarheid van natuurlijke materialen? G of S: ')
    kennisk = kennis == 'G'
    genezen = input('Wat is uw kennis in genezen en verwarmen? G of S? ')
    genezenk = genezen == 'G'
    beschermen = input('Wat is uw kennis in beschermen? G of S: ')
    beschermenk = beschermen == 'G'
    zuiveren = input('Wat is uw kennis van water zuivering? G of S: ')
    zuiverenk = zuiveren == 'G'

if sterk and zwaark and slimk and vangenk and bewerkenk and bouwenk and kennisk and genezenk and beschermenk and zuiverenk == True:
    print('Gefeliciteerd! u bent een beer, vos, bever en een uil!')
elif sterkk and zwaark == True:
    print('Gefeliciteerd! u bent een beer!')
elif slimk and vangenk == True:
    print('Gefeliciteerd! u bent een vos!')
elif bewerkenk and bouwenk == True:
    print('Gefeliciteerd! u bent een bever!')
elif kennisk and genezenk and beschermenk and zuiverenk == True:
    print('Gefeliciteerd! u bent een uil!')
if sterkk and zwaark and slimk and vangenk == True:
    print('Gefeliciteerd! u bent een beer en een vos!')
if sterkk and zwaark and bewerkenk and bouwenk == True:
    print('Gefeliciteerd! u bent een beer en een bever!')
if sterkk and zwaark and kennisk and genezenk and beschermenk and zuiverenk == True:
    print('Gefeliciteerd! u bent een beer en een uil!')
if slimk and vangenk and bewerkenk and bouwenk == True:
    print('Gefeliciteerd! u bent een vos en een bever!')
if slimk and vangenk and kennisk and genezenk and beschermenk and zuiverenk == True:
    print('Gefeliciteerd! u bent een vos en een uil!')
if bewerkenk and bouwenk and kennisk and genezenk and beschermenk and zuiverenk == True:
    print('Gefeliciteerd! u bent een bever en een uil!')

