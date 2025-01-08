import requests
from bs4 import BeautifulSoup
import re


def scrape_url(url,keywords):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()

        results={}

        for keyword in keywords:
            matches = re.findall(rf'\b{re.escape(keyword)}\b', text_content, re.IGNORECASE)
            results[keyword] = len(matches)
        return results
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None
    

def main():

    url = input("enter url :")
    a= int(input("enter number of keywords :"))
    keywords=[]

    for i in range(a):
        keyword =input("enter keyword :")
        keywords.append(keyword)
    
    results = scrape_url(url, keywords)
    print(results)

if __name__ == "__main__":
    main()