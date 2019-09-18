import xml.etree.ElementTree as etree
import lxml.etree

tree = etree.parse('../../../diveintopython3/examples/feed.xml')
# fce parse zpracuje cely soubor naraz, ale existuji zpusoby, jak ho zpracovavat po castech
# fce parse vraci objekt, ktery reprezentuje cely dokument
root = tree.getroot()  # korenovy element; reprezentace jako {prostor_jmen}lokalni_jmeno
print(root)

# elementy jsou seznamy; polozkami seznamu jsou elementy potomku
print(root.tag)
print(len(root))  # pocet potomku
for child in root:
    print(child)
"""
title, subtitle, id, updated, link jsou metadata patrici k feed
3 elementy entry maji vlastni potomky, ti ale v tomto seznamu nejsou
"""

# elementy maji atributy - kdyz mam odkaz na element, jeho atributy ziskan jako slovnik
print(root.attrib)
print(root[4])
print(root[4].attrib)
print()
print(root[3])
print(root[3].attrib) # nema zadne atributy

# hledani uzlu
print(root.findall('{http://www.w3.org/2005/Atom}entry'))  # najde vsechny detske elementy
print(root.tag)
print(root.findall('{http://www.w3.org/2005/Atom}feed'))  # prohledava jen elementy potomku a tam zadny jmenem feed neni
print(root.findall('{http://www.w3.org/2005/Atom}author'))
# element author se v dokumentu vyskytuje 3x, ale ne v pozici potomka korenoveho elementu

# objekt tree ma nekolik metod korenoveho elementu
print(tree.findall('{http://www.w3.org/2005/Atom}entry'))
print(tree.findall('{http://www.w3.org/2005/Atom}author'))
# vysledky stejne jako s tree.getroot().findall()

entries = tree.findall('{http://www.w3.org/2005/Atom}entry')
print(len(entries))
title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')  # find vraci prvni vyhovujici element
print(title_element.text)

foo_element = entries[0].find('{http://www.w3.org/2005/Atom}foo')  # element foo tam neni
print(foo_element)
print(type(foo_element))

# hledani hloubeji v potomcich
all_links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
# lisi se pocatecnima // + pocatecni . tam musim mit kvuli svoji verzi knihovny
print(all_links)
print(all_links[0].attrib)  # toto je primy potomek korenoveho elementu; alternativni odkaz z urovne celeho obsahu feed
print(all_links[1].attrib)
print(all_links[2].attrib)
print(all_links[3].attrib)


# KNIHOVNA lxml
tree = lxml.etree.parse('../../../diveintopython3/examples/feed.xml')  # funguje stejne
root = tree.getroot()  # funguje stejne
print(root.findall('{http://www.w3.org/2005/Atom}entry'))  # funguje stejne

# findall podporuje komplikovanejsi vyrazy
print(tree.findall('//{http://www.w3.org/2005/Atom}*[@href]'))
"""
// elementy nachazejici se kdekoliv; elementy z prostoru jmen Atom; * elementy s libovolnym lokalnim jmenem; majici 
atribut @href
"""
print(tree.findall('//{http://www.w3.org/2005/Atom}*[@href="http://diveintomark.org/"]'))
# najde elementy, ktere maji href teto hodnoty
NS = '{http://www.w3.org/2005/Atom}'  # pomucka pro formatovani retezce, aby dotaz nebyl moc dlouhy
print(tree.findall('//{NS}author[{NS}uri]'.format(NS=NS)))
# hleda elementy author, ktere maji mezi svymi potomky uri - jeden z prvniho a jeden z druheho elementu entry

# podpora pro vyrazy XPATH 1.0
tree = lxml.etree.parse('../../../diveintopython3/examples/feed.xml')
NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}
entries = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=NSMAP)
"""
dotaz x XPATH: hledej elementy category v prostoru jmen Atom, ktere obsahuji atribut term s hodnotou accessibility
/.. znamena vrat k tomuto nalezenemu elementu rodicovsky element

vysledkem dotazy je seznam uzlu - ty mohou reprezentovat elementy, atributy nebo textovy obsah
"""
print(entries)
entry = entries[0]
print(entry.xpath('./atom:title/text()', namespaces=NSMAP))
"""
vraci seznam textovych uzlu - textovy obsah text() elementu title, ktery je potomkem aktualniho elementu ./
"""

# GENEROVANI XML
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', attrib={"{http://www.w3.org/XML/1998/namespace}lang":
                                                                          'en'})
"""
tvorba noveho elementu: vytvoreni instance tridy Element, 1. arg: jmeno elementu, tj. prostor jmen + lokalni jmeno
atributy musi byt ve tvaru {prostor_jmen}lokalni_jmeno
vytvori se element feed v prostoru jmen Atom a to bude korenovy element
"""
print(etree.tostring(new_feed))  # prevedeni na retezec pomoci fce tostring()


# a generovani pomoci lxml
NSMAP = {None: 'http://www.w3.org/2005/Atom'}
"""
definice zobrazeni prostoru jmen: klici jsou prefixy, hodnotami jsou prostory jmen. 
klic None vyjadruje vychozi prostor jmen 
"""
new_feed = lxml.etree.Element('feed', nsmap=NSMAP)
print(lxml.etree.tounicode(new_feed))  # definuje prostor jmen Atom a deklaruje element feed
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')  # atribut se da tvorit metodou set()
print(lxml.etree.tounicode(new_feed))

print()
# tvorba potomka
title = lxml.etree.SubElement(new_feed, 'title', attrib={'type': 'html'})  # detsky element dedi prostor jmen rodice
print(lxml.etree.tounicode(new_feed))
title.text = 'dive into &hellip;'  # nastaveni textoveho obsahu
print(lxml.etree.tounicode(new_feed))  # serializace i s textovym obsahem
"""
text, ktery obsahuje znaky <= & je pri serializaci preveden na specialni posloupnosti
"""
print(lxml.etree.tounicode(new_feed, pretty_print=True))

# poruseny dokument XML
# tree = lxml.etree.parse('../../../diveintopython3/examples/feed-broken.xml') vyvola XMLSyntaxError
"""
obecne je zpracovani XML dokumentu strasne citlive na spravny format, protoze se kdysi prijala koncepce, ze kdyz
nekde spravny format neni, tak program proste havaruje

da se to obejit - pro zpracovani je treba vytvorit vlastni XML parser
"""
parser = lxml.etree.XMLParser(recover=True)
"""
pri nastaveni recover=True parser udela vsechno mozne, aby na chybach proti korektnimu formatu nezhavaroval
"""
tree = lxml.etree.parse('../../../diveintopython3/examples/feed-broken.xml', parser)
print(parser.error_log)  # syntakticky analyzator chyby proti formatu zaznamenava
print(tree.findall('{http://www.w3.org/2005/Atom}title'))
title = tree.findall('{http://www.w3.org/2005/Atom}title')[0]  # nedefinovanou entitu &hellip; jen vypustil
print(title.text)
print(lxml.etree.tounicode(tree.getroot()))


