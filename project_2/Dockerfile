#**************STAGE 1*********
FROM python:3.9 as base-image

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

#************STAGE 2***********
FROM python:3.9-slim

WORKDIR /app

COPY --from=base-image /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

COPY --from=base-image /app /app

CMD ["python", "todo_app.py"]


