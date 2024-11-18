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


def main(url, output_data ):
    data = main_data(url)
    write_to_csv(data, output_data)


def response_url(url):
    # odpoved ze serveru 
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def extract_detail_data(detail_url):
    # function for registred users, valid votes and envelopes and the candidate parties 

    soup = response_url(detail_url)

    try: 
        registered_users = int(soup.find("td", {"class": "cislo", "headers": "sa2"}).get_text(strip=True).replace('\xa0', ''))
    except AttributeError:
        registered_users = None

    try:
        envelopes = int(soup.find("td", {"class": "cislo", "headers": "sa3"}).get_text(strip=True).replace('\xa0', ''))
    except AttributeError:
        envelopes = None

    try:
        valid_votes = int(soup.find("td", {"class": "cislo", "headers": "sa6"}).get_text(strip=True).replace('\xa0', ''))
    except AttributeError:
        valid_votes = None

    candidate_parties = {}

    tables = soup.find_all("div", {"class": "t2_470"})

    for table in tables:
        rows = table.find_all("tr")

        for row in rows: 
            cells = row.find_all("td")

            if len(cells) >= 3:
                candidate_name = cells[1].get_text(strip=True)
                try:
                    votes = int(cells[2].get_text(strip=True).replace('\xa0', ''))
                except ValueError:
                    votes = 0   # 0 if invalid data
                
                candidate_parties[candidate_name] = votes

    if not candidate_parties:           # simple error handling
        print(f"No candidate parties found for: {detail_url}")

    return{
        "registered_users": registered_users,
        "envelopes": envelopes,
        "valid_votes": valid_votes,
        "candidate_parties": candidate_parties,
    }

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

        if full_detail_link:
            detail_data = extract_detail_data(full_detail_link)
        else:
            detail_data = {
                "registered_users": None,
                "envelopes": None,
                "valid_votes": None,
                "candidate_parties": {},
            }
        
        results.append({
            "indentifier": identifier,
            "detail_link": full_detail_link,
            "name": name,
            "registered_users": detail_data["registered_users"],
            "envelopes": detail_data["envelopes"],
            "valid_votes": detail_data["valid_votes"],
            "candidate_parties": detail_data["candidate_parties"],
        })

    return results

def write_to_csv(results, output_data):
    with open(output_data, mode="w", newline="", encoding="UTF-8") as file: 
        writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_MINIMAL)

        header = ["indentifier", "Name", "Registered Users", "Envelopes", "Valid Votes"] + list(results[0]["candidate_parties"].keys())
        writer.writerow(header)

        for row in results:
            row_data = [
                row["indentifier"],
                row["name"],
                row["registered_users"],
                row["envelopes"],
                row["valid_votes"],
            ]
            row_data.extend(row["candidate_parties"].values())
            writer.writerow(row_data)
    
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape election data and save it to CSV file.")
    parser.add_argument("url", type=str, help="The URL of the unit to scrape.")
    parser.add_argument("output_data", type=str, help="The name of the output CSV file.")
    args = parser.parse_args()

    results = main_data(args.url)
    write_to_csv(results, args.output_data)
    print(f"Results have been written to {args.output_data}.")


    main(args.url, args.output_data)
    







 
    

