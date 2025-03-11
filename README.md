# Web Scraper de Notícias

Este é um simples Web Scraper em Python que coleta as últimas notícias do [Hacker News](https://news.ycombinator.com/) e salva os dados em um arquivo JSON. O scraper é executado periodicamente a cada 5 segundos e armazena as notícias em um arquivo `news.json`.

## Funcionalidades

- Coleta as últimas notícias de Hacker News.
- Exibe os títulos e links das notícias no terminal.
- Salva os dados coletados em um arquivo `news.json`.
- Executa periodicamente a cada 5 segundos.

## Tecnologias Utilizadas

- **Python 3.x**
- **Requests** - Para fazer requisições HTTP.
- **BeautifulSoup** - Para fazer parsing do HTML e extrair os dados.
- **JSON** - Para salvar os dados em um formato estruturado.
- **Schedule** - Para agendar a execução periódica do scraper.

## Requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Para instalar as dependências necessárias, execute:

```bash
pip install requests beautifulsoup4 schedule
```

## Como Usar
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/web-scraper-noticias.git
cd web-scraper-noticias
```
2. Execute o script:
```bash
python scraper.py
```
3. O scraper começará a rodar a cada 5 segundos, exibindo as notícias no terminal e salvando os dados em news.json.
```bash
[
  {
    "title": "Título da Notícia",
    "link": "https://link-da-noticia.com"
  },
  ...
]
```
4. Execução Periódica: O schedule é usado para rodar o scraper a cada 5 segundos, podendo ser ajustado conforme necessário.
