FROM python:3.9-slim

RUN apt-get update && apt-get install --no-install-recommends -y \
        bash \
        gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry>=1.0,<2.0.0" \
    && poetry config virtualenvs.create false

COPY deployment/entrypoint.sh /entrypoint.sh

WORKDIR /playwright_project/
COPY poetry.lock pyproject.toml ./
RUN poetry install --only main

COPY deployment/test.sh test.sh
COPY ./playwright_project/ .

ENTRYPOINT ["/entrypoint.sh" ]

CMD ./test.sh
