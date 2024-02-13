FROM python:3.12

WORKDIR /app

#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#ENV DD_ENV=dev
#ENV DD_SERVICE=app
#ENV DD_VERSION=0.1
#ENV FLASK_APP=app
#ENV FLASK_ENV=development
#ENV LOCAL_DATABASE_URI=postgresql://postgres:teste123@localhost:5432/postgres
#ENV DATABASE_URI=postgresql://mbl_teste_p7d1_user:t0bg7ICs6cXbRLZawFmHU9vuPwriZ9R5@dpg-cn4j21ol6cac73apga0g-a.oregon-postgres.render.com/mbl_teste_p7d1
#ENV SECRET_KEY=ac1a8b322f381c9fbcc99356f129d4296cc3bf400b52832d7a7af9c3268e55ae

COPY . /app
#COPY requirements.txt /app

RUN export SECRET_KEY=ac1a8b322f381c9fbcc99356f129d4296cc3bf400b52832d7a7af9c3268e55ae 
RUN python3 -m pip install --upgrade pip && \
    pip install -r app/requirements.txt && \
    pip install -U python-dotenv\
    pip install -u Flask-Cors

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
