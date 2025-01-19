from bs4 import BeautifulSoup
from processaBancoDeDados import db_update_news

SCAPING_ROOT_DIV = 'noticiario'
SCRAPING_LI_DIV = 'list-group-item'

def processar_noticias(noticias) -> None:
    """
    Responsável por tratar os dados da lista de noticias.
    :param noticias: texto html de noticias
    :return: None
    """
    noticias = BeautifulSoup(noticias, 'html.parser')

    noticias = noticias.find('div',class_=SCAPING_ROOT_DIV)

    noticias = noticias.find_all('li', class_=SCRAPING_LI_DIV)

    if noticias is None:
        print("[processarNoticias]: Nenhuma noticia encontrada.")
        return None

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

        category = noticia.select_one('div.row div.col-lg.d-flex.flex-column p.mt-auto.font-weight-semi-bold.mb-0').text
        print("Date: ",category)

        image_url = noticia.select_one('div.row div.col-lg-3.d-flex img.w-100.mt-3.my-md-auto')['src']
        print("Image URL: ", image_url)
        print('-----------------')


        db_update_news(title, category, link, text)

