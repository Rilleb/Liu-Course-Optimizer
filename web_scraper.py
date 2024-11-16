import requests
import re
from bs4 import BeautifulSoup



def main():
    base_url = "https://studieinfo.liu.se/program/"
    program = "6CDDD"
    admission_year_code = "4971"
    url = base_url + program + "/" + admission_year_code + "#curriculum"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    term_list = soup.find_all("section", class_=re.compile(r"accordion.*semester.*js-semester.*show-focus"))[6:9]

    period_list = []
    for term in term_list:
        period_list.append(term.find_all("tbody", class_="period"))






main()