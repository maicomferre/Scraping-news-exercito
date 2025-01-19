# Programa de Captura de notícias
Este programa deve atuar como daemon para manter um banco de dados mySQL
atualizado com as notícias mais recentes da página www.eb.mil.br
Realizando requisições a cada hora das 8 às 16 de segunda a sexta.

### Funcionamento:
O programa obtém a lista de notícias e ao encontrar uma nova atualiza
no banco de dados e se configurado baixa a imagem principal e redimensiona
se for o caso.

- Funciona em background com docker.
- Utiliza _poetry_ para gerenciar dependências.


### Utilização:
- Crie o arquivo .env dentro da subpasta python-scraping-news-eb-

*Modelo arquivo .env*:
````env
#MYSQL CONNECTION
DB_HOST = 'localhost'
DB_PORT = 3306
DB_DB = <database>
TABLE = <table_name>
DB_USER = <database user>
DB_PASSWORD = <database password>
````


