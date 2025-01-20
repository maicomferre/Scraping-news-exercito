"""
    @Author: <Maicom Ferreira>
    @Date: 19/01/2025
    @Description: Realiza scraping da pagina que lista artigos da pagina www.eb.mil.br
"""

from obterNoticias import obter_noticias
from processarNoticias import processar_noticias
from processaBancoDeDados import create_db_if_not_exist
from utils import Log
import time
import datetime

log = Log(__name__)

def main() -> None:
    """
        Responsável por executar o scraping.
        Faz as requisições todos os dias de segunda à sexta
        Das 8 às 18

    :return: None
    """
    create_db_if_not_exist()
    log.debug('Iniciando Programa...')

    while True:
        now = datetime.datetime.now()
        if now.weekday() < 6 or True: #Segunda->Sexta
            log.info('Não é final de semana.')
            if 7 < now.hour < 19 or True:
                log.info('Iniciando captura das noticias.')
                news = None
                while news is None:
                    #Enquanto a conexão não for realizada continua tentados
                    news = obter_noticias()
                    if news is not None:
                        processar_noticias(news)
                        print("Script de captura de noticias executado.")
                    else:
                        log.warning('retorno de obter_noticias(): None. Tentando novamente')
                    time.sleep(60)
            else:
                log.info("Fora do horário de captura.")
        time.sleep(3600)

if __name__ == '__main__':
    main()