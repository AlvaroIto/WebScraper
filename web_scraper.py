import requests
from bs4 import BeautifulSoup
import json
import schedule
import time

def fetch_new():
    url = "http://news.ycombinator.com/" #Exemplo de site de noticias
    response = requests.get(url)

    if response.status_code != 200:
        print('Erro ao acessar o site')
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.select(".athing"):
        title = item.select_one(".titleline a").text
        link = item.select_one(".titleline a")["href"]
        articles.append({"title": title, "link": link})
    
    return articles

def save_to_json(data, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def rodar_scraper():
    print("Executando Web Scraper...")
    noticias = fetch_new()  # Chama sua função de scraping
    for item in noticias:
        print(f"{item['title']} - {item['link']}")

# Agenda para rodar a cada 1 hora
schedule.every(5).seconds.do(rodar_scraper)

# Loop infinito para manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(10)  # Aguarda 1 minuto antes de checar novamente

    news_data = fetch_new()
    if news_data:
        save_to_json(news_data)
        print("Dados salvos em news.json")
    else:
        print("Nenhuma notícia encontrada")
