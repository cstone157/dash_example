#Using python
FROM python:3.9-slim

RUN pip install dash pandas plotly numpy

RUN mkdir /app
COPY ./app /app

EXPOSE 8050

CMD python /app/app.py