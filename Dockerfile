FROM python:3-slim as python
ENV PYTHONUNBUFFERED=true
WORKDIR /app

FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==1.3.2
COPY . ./
COPY template_secrets.json secrets.json
RUN poetry install --only main --no-interaction --no-ansi -vvv

FROM python as runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=poetry /app /app
EXPOSE 8000
CMD python manage.py db upgrade && python run.py debug
