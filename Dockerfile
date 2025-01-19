FROM python:3.13-slim as builder
WORKDIR /app
COPY setup.py README.md /app/
RUN pip install --no-cache-dir .

FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY . /app
ENV PYTHONUNBUFFERED=1
CMD ["python", "src/bot.py"]
