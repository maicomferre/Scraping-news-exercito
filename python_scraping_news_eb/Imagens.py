import os
import time
import requests
import uuid
import dotenv
from utils import Log

log = Log(__name__)
max_tries = 5 #Maximo de tentativas de download
dotenv.load_dotenv()


class Image:
    tries = 0
    broken = False
    def __init__(self, url):
            if len(url) == 0:
                log.error("URL vazia. Não foi possível baixa a imagem")
                self.broken = True
                return

            if os.getenv('DOWNLOAD_IMAGE', 'true').lower() != 'true':
                log.info("Ignorando imagem... DEFINIDO NO ARQUIVO .env NÃO BAIXAR IMAGENS")
                self.broken = True
                return

            self.url = url
            self.save_in = os.getenv('SAVE_IN','images/')
            if self.save_in[-1] != '/':
                self.save_in = self.save_in+'/'

            os.makedirs(self.save_in, exist_ok=True)
            os.makedirs('images/', exist_ok=True)

    def obter_imagem(self) -> None|str:
        """
        Obtém o arquivo de imagem.
        @return: None|nome do arquivo.
        """
        if self.broken:
            return None

        try:
            r = requests.get(self.url)

            if r.status_code != 200:
                log.error(f"[obter_imagem] Erro: Status code: {r.status_code}")
                if self.tries < max_tries:
                    time.sleep(3)
                    self.tries += 1
                    self.obter_imagem()
                    return None
                else:
                    log.error(f"[obter_imagem] Erro: Muitas tentativas imagem {self.url} ignorada")

            self.tries = 0

            try:
                ext = os.path.splitext(self.url)[1]
            except (TypeError, KeyError, AttributeError):
                ext = '.jpg'

            if ext == '' or (ext != '.jpeg' and ext != '.jpg' and ext != '.png' and ext != '.webp'):
                ext = '.jpg'

            filename = uuid.uuid4().hex + ext
            path = self.save_in + filename

            with open(path, 'wb') as f:
                f.write(r.content)

            return filename
        except requests.exceptions.RequestException as e:
            log.error(f"[obter_imagem][requests error]: {e}")
            if self.tries < max_tries:
                time.sleep(3)
                self.tries += 1
                self.obter_imagem()
                return None
        except Exception as e:
            log.error(f"[obter_imagem] Erro: {e}")