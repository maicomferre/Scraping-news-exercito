import mysql.connector as mysql
import dotenv
import os

from utils import Log

log = Log(__name__)

dotenv.load_dotenv()

def create_db_if_not_exist():
    print("Tentando Criar banco de dados caso não exista")
    if os.path.exists('template.sql'):
        try:
            file = open('template.sql', 'r')
            sql = file.read()
            sql = sql.format(table_name=os.getenv('TABLE'))

            myl = mysql_connect()
            cursor = myl.cursor()
            cursor.execute(sql)
            log.info('create_db_if_not_exist tentando criar tabela de banco de dados caso não exista')

        except PermissionError as e:
            log.error(f"Erro de permissão ao acessar o arquivo template.sql [{e}]")
    else:
        log.error('processaBancoDeDados[create_db_if_not_exists] template.sql não existe.')

def mysql_connect():
    """
    Realiza conexão mysql para o banco de dados
    :return: Instância mySQL
    """
    try:

        return mysql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT",3306),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DB"),
            auth_plugin="caching_sha2_password",
            connection_timeout=10,
        )
    except mysql.Error as e:
        log.error(f"Erro ao realiza a conexão com o banco de dados. [{e}]")
        return None
    except Exception as e:
        log.error(f"Erro[mysql_connect]: [{e}]")
        return None



class Database:
    myl = None
    def __init__(self):
        self.myl = mysql_connect()

    def update_news(self,title, category, link, text, date,image_url,img_name) -> bool:
        if self.myl is None or self.myl.is_connected() is False:
            self.myl = mysql_connect()

        if self.myl is None or self.myl.is_connected() is False:
            log.error('Conexão mysql. Não foi possível realizar conexão.')
            return False

        cursor = self.myl.cursor()

        cursor.execute("SELECT * FROM {table} WHERE title = %s AND category = %s".format(table=os.getenv('TABLE')),
                                                                                                  (title, category))
        if cursor.fetchone():
            return False

        #image_url -> ainda falta adicionar
        cursor.execute("INSERT INTO {table}(title,category,url,description,publish_date,image_url,local_image) VALUES (%s,%s,%s,%s,%s,%s,%s)".format(table=os.getenv('TABLE')),
                            (title,category,link,text,date,image_url,img_name)
                       )
        self.myl.commit()

        return True