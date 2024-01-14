FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app


RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt

RUN mkdir logs
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]