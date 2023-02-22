FROM python:3.10.5-slim-buster

WORKDIR .
COPY . .
RUN apt-get install -y ffmpeg
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
