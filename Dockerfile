FROM python:3.12.3-alpine3.20

WORKDIR /app
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir requests \
    && pip3 install --no-cache-dir mysql-connector-python \
    && pip3 install --no-cache-dir bs4 \
    && pip3 install --no-cache-dir python-dotenv

COPY ./ ./

WORKDIR /app/python_scraping_news_eb

COPY python_scraping_news_eb/ ./

CMD ["python3.12", "__main__.py"]
