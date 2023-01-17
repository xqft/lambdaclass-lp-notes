FROM python:3.9-slim AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS builder

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

COPY --from=builder /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR /app
COPY src/ src/
ENTRYPOINT [ "python", "src/app.py" ]
