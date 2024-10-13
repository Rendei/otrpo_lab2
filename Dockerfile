FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y python3-opencv && \
    apt-get clean

COPY face_detection.py /app/face_detection.py
COPY photo_1.jpg /app/photo_1.jpg

WORKDIR /app

CMD ["python", "face_detection.py"]
