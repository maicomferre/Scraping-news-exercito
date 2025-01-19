import requests

#Exercito Page
URL_EB_NEWS = 'https://www.eb.mil.br/noticiario-do-exercito?sort=displayDate-'


def obter_noticias():
    """
    Obtém a lista das notícias mais recentes do site do EB
    :param: None
    :return: None, set
    """
    request = requests.get(URL_EB_NEWS)

    if request.status_code != 200 or request.text is None:
        print('Falha na requisição [Status Code Error] ou None ', request.status_code)
        return None


    return request.text