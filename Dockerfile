FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN adduser -D Yousa
RUN chown -R Yousa:Yousa /usr/src/app
USER Yousa

EXPOSE 5000
CMD ["python","app.py"]
