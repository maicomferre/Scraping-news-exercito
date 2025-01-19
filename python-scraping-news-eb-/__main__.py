"""
    @Author: <Maicom Ferreira>
    @Date: 19/01/2025
    @Description: Realiza scraping da pagina que lista artigos da pagina www.eb.mil.br
"""

from obterNoticias import obter_noticias
from processarNoticias import processar_noticias
import time
import datetime

def main() -> None:
    """
        Responsável por executar o scraping.
        Faz as requisições todos os dias de segunda à sexta
        Das 8 às 18

    :return: None
    """
    while True:
        now = datetime.datetime.now()
        if now.weekday() < 6 or True: #Segunda->Sexta
            if 7 < now.hour < 19 or True:

                news = None
                while news is None:
                    #Enquanto a conexão não for realizada continua tentandos
                    news = obter_noticias()
                    if news is not None:
                        processar_noticias(news)
                        print("Script de captura de noticias executado.")

                    time.sleep(60)

        time.sleep(3600)

if __name__ == '__main__':
    main()