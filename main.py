"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

autor: Vícha Dominik
email: dominik.vicha@gmail.com 
discord: Dominik V

POPIS PROJEKTU: 
Napiš takový skript, který vybere jakýkoliv územní celek z tohoto odkazu (https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) Např. X u Benešov odkazuje sem (https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101). Z tohoto odkazu chcete vyscrapovat výsledky hlasování pro všechny obce.

Můžeš stahovat výsledky hlasování:

1. Pomocí odkazů ve sloupci číslo, např. 529303,
2. pomocí odkazů ve sloupci Výběr okrsku, tedy sloupec se symbolem X.
3. Je na tobě, který sloupec použiješ, ale dobře si jednotlivé odkazy prohlédni, jestli tě opravdu odkážou na výsledky obce.

JAK POSTUPOVAT:

1. Na svém počítači si vytvoříte vlastní virtuální prostředí (speciálně pro tento úkol)
2. Do nově vytvořeného prostředí si přes IDE (nebo příkazový řádek) nainstalujete potřebné knihovny třetích stran
3. Vygenerujete soubor requirements.txt, který obsahuje soupis všech knihoven a jejich verzí (nevypisovat ručně!)
4. Výsledný soubor budete spouštět pomocí 2 argumentů (ne pomocí funkce input). První argument obsahuje odkaz, který územní celek chcete scrapovat (př. územní celek Prostějov ), druhý argument obsahuje jméno výstupního souboru (př. vysledky_prostejov.csv)
5. Pokud uživatel nezadá oba argumenty (ať už nesprávné pořadí, nebo argument, který neobsahuje správný odkaz), program jej upozorní a nepokračuje.
6. Následně dopište README.md soubor, který uživatele seznámíte se svým projektem. Jak nainstalovat potřebné knihovny ze souboru requirements.txt, jak spustit váš soubor, příp. doplnit ukázku, kde demonstrujete váš kód na konkrétním odkaze s konkrétním výpisem.

PROJEKT MUSÍ SPLŇOVAT TYTO BODY: 
1. Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit (zejména zaslání zpětné vazby na Discord).
2. Soubor s programem (..nebo také skript) s příponou .py, který pro správný běh potřebuje 2 argumenty pro spuštění,
spuštění probíhá přes - odkaz který se zadá do terminálu  
a jako druhý argument je výstupní soubor -> musí končit jako .csv



3. soubor se seznamem pouze relevantních knihoven a jejich verzí k projektu (requirements.txt),
4. stručnou dokumentaci (popis, instalace knihoven, ukázka) (README.md)
5. soubor s uloženým výstupem (.csv),
6. zápis organizovaný do krátkých a přehledných funkcí.

VÝSTUP BUDE OBSAHOVAT: 
Ve výstupu (soubor .csv) každý řádek obsahuje informace pro konkrétní obec. Tedy podobu:0

1. kód obce
2. název obce
3. voliči v seznamu
4. vydané obálky
5. platné hlasy
6. kandidující strany (co sloupec, to počet hlasů pro stranu pro všechny strany).

"""


import requests
from bs4 import BeautifulSoup
import csv
import argparse
from pprint import pprint

url_1 = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

"""
def main():
    main_data(url_1)
"""

def response_url(url):
    # odpoved ze serveru 
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def main_data(url):
    #funkce na to dostat hlavni data 
    soup = response_url(url)
    table_tag = soup.find("div", {"id": "core"})
    rows = table_tag.find_all("tr")

    
    results = []

    for row in rows[2:]:
        cells = row.find_all("td")

        if not cells:
            continue
        
    
        identifier = cells[0].get_text(strip=True)
        name = cells[1].get_text(strip=True)

        a_tag = cells[0].find("a")
        if a_tag and a_tag.get("href"):
            detail_link = a_tag.get("href")
            full_detail_link = f"https://www.volby.cz/pls/ps2017nss/{detail_link}"
        else:
            full_detail_link = None
        
        results.append({
            "indentifier": identifier,
            "detail_link": full_detail_link,
            "name": name,
        })

    return results

        
if __name__ == "__main__":
    #print(response_url(url_1))
    results = main_data(url_1)
    pprint(results)
    
    







    # nachystam aby kod fungoval pres jeden arg. 
    # parser = argparse.ArgumentParser(description="")
    

