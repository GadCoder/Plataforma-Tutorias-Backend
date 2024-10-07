FROM python:3.11

WORKDIR /code

COPY requirements.txt .
ADD ./app /code/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
