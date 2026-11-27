FROM python:3.15-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
LABEL authors="Nikita Selivanov"

COPY ./uv.lock ./pyproject.toml ./README.md /app/
RUN uv sync --locked --no-install-project

COPY ./src/ /app/src/
RUN uv sync --locked --no-editable

WORKDIR /app/src
CMD python3 -m service_a
