FROM python:3.8

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5000

ENTRYPOINT [ "flask", "--app","main", "run", "--host=0.0.0.0"]
