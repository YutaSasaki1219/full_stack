# python3.12のイメージをダウンロード
FROM python:3.12.1-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# pipを使ってpoetryをインストール
RUN pip install poetry

RUN poetry config virtualenvs.in-project true

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi
