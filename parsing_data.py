import bs4
import requests

url = "https://www.borismusler.com/"
response = requests.get(url)


def get_data(response):
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup

def parse_data(soup):
    data = soup.find_all("p")
    return soup

def write_to_file(data):
    with open("test.txt", "w") as file:
        file.write(str(data))

def main():
    soup = get_data(response)
    data = parse_data(soup)
    write_to_file(data)