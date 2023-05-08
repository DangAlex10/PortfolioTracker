FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY . /code/ 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]