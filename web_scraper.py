import requests
from bs4 import BeautifulSoup



def main():
    base_url = "https://studieinfo.liu.se/program/"
    program = "6CDDD"
    admission_year_code = "4971"
    url = base_url + program + "/" + admission_year_code + "#curriculum"

    page = requests.get(url)
    #print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    term_list = soup.find_all("section", class_="accordion semester js-semester show-focus")
    for term in term_list:
        print(term.prettify())






main()