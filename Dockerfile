FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    python3-dotenv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip \
    && pip3 install requests \
    && pip3 install mysql-connector \
    && pip3 install bs4 \
    && pip3 install python-dotenv


COPY ./ ./

WORKDIR /app/python_scraping_news_eb

COPY python_scraping_news_eb/ ./

CMD ["python3.12", "__main__.py"]
