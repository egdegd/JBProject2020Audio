FROM python:3.8

RUN apt-get -y update
RUN apt-get install -y ffmpeg

WORKDIR /usr/src/PracticeJB2020Audio

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python3", "src/MusicClient.py"]

