FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY requirements.txt requirements.txt
RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./src /app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]