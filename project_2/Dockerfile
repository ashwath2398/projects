#**************STAGE 1*********
FROM python:3.9 as base_builder

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "todo_app.py"]

#*************STAGE 2**********
