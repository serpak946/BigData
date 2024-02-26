FROM python:3.12
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py app.py
CMD ["python", "-u", "app.py"]
LABEL authors="serpak"