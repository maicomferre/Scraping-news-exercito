from bs4 import BeautifulSoup
from processaBancoDeDados import Database
import datetime

SCAPING_ROOT_DIV = 'noticiario'
SCRAPING_LI_DIV = 'list-group-item'

def processar_noticias(noticias) -> None:
    """
    Responsável por tratar os dados da lista de notícias.
    :param noticias: Texto html de notícias
    :return: None
    """
    noticias = BeautifulSoup(noticias, 'html.parser')

    noticias = noticias.find('div',class_=SCAPING_ROOT_DIV)

    noticias = noticias.find_all('li', class_=SCRAPING_LI_DIV)

    if noticias is None:
        print("[processarNoticias]: Nenhuma noticia encontrada.")
        return None

    db = Database()
    for noticia in noticias:
        category = noticia.select_one('div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)').text
        print("Category: ",category)


        link_title = noticia.select_one('div.row div.col-lg.d-flex.flex-column a.d-block.mb-2')
        link = link_title['href']

        print("Link: ",link)
        title = link_title.find('h4').text
        print("Title: ", title)

        text = noticia.select_one('div:nth-child(1) > div:nth-child(1) > p:nth-child(3)').text
        print("Text: ", text.replace('\n',''))

        date = noticia.select_one('div.row div.col-lg.d-flex.flex-column p.mt-auto.font-weight-semi-bold.mb-0').text
        print("Date: ",date)

        image_url = noticia.select_one('div.row div.col-lg-3.d-flex img.w-100.mt-3.my-md-auto')['src']
        print("Image URL: ", image_url)

        date = datetime.datetime.strptime(date, "%d/%m/%Y %Hh%M")

        date = date.strftime("%Y-%m-%d %H:%M:%S")


        if db.update_news(title, category, link, text, date):
            print("[processarNoticias]: \tNoticia adicionada com sucesso.")

        print('--------------------')


