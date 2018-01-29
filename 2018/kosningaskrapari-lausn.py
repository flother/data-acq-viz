import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import chain


def get_urls():
    """
    Skilar lista sem inniheldur slóðir á allar undirsíður
    með kosningaúrslitum
    """
    main_page = requests.get("http://www.kosningastofnun.in/")
    page_soup = bs(main_page.content, "html.parser")

    urls = [title.a.get("href") for title in page_soup.find_all(class_="blog-post-title")]

    return urls


def scrape(urls):
    """
    Tekur inn lista af slóðum og skrapar fyrstu töfluna sem finnst á hverri slóð.
    Skilar lista af dicts þar sem hvert dict er með töfluhausa sem lykla og
    töfluhólf sem gildi
    """
    all_dicts = []

    for url in urls:
        elections_page = requests.get(url)
        elections_soup = bs(elections_page.content, "html.parser")

        # Finnum alla töfluhausa og setjum í lista:
        headers = [header.string.strip() for header in elections_soup.find_all("th")]

        # Förum svo í gegnum hverja röð og setjum gildin í lista:
        for row in elections_soup.find_all("tr"):
            results = [cell.string.strip() for cell in row.find_all("td")]

            # Athugum hvort þetta er gild niðurstöðulína, annars gerum við ekkert:
            if results:
                # Nú getum við sett þessar niðurstöður í dict með hausunum:
                elections = dict(zip(headers, results))

                # Ef dagsetning var ekki með í þessum niðurstöðum þurfum við
                # að skrapa hana úr titlinum og setja inn í dictið:
                if "Dagsetning" not in elections:
                    full_title = elections_soup.h2.a.string
                    # Splittum titlinum á fyrsta bili og tökum seinni hlutann:
                    elections["Dagsetning"] = full_title.split(" ", 1)[1]

                # Og setjum svo dictið í stóra listann:
                all_dicts.append(elections)

    return all_dicts


def save_csv(list_of_dicts):
    """
    Tekur inn lista af dicts og skrifar út í CSV-skrána "kosningar.csv" í möppunni
    sem skriftan er keyrð úr
    """
    with open("kosningar.csv", "w") as csv_file:
        fieldnames = set([key for key in chain(*list_of_dicts)])

        # Röðum dálkaheitunum, fyrst í stafrófsröð og svo aftur til að fá
        # dagsetningu fremst (ekki nauðsynlegt):
        fieldnames = sorted(fieldnames)
        fieldnames = sorted(fieldnames, key=lambda x: x == "Dagsetning", reverse=True)

        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dicts)


# Keyrum heila klabbið:
if __name__ == "__main__":
    save_csv(scrape(get_urls()))
