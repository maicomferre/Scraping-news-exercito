FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    python3-poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock README.md ./
COPY python_scraping_news_eb/ ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["poetry", "run", "python3", "__main__.py"]
