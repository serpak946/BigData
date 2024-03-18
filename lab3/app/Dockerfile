FROM python:3.12
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
CMD ["python", "-u", "main.py"]
LABEL authors="serpak"