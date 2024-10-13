FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y build-essential \
    && apt-get clean



RUN pip install --no-cache-dir opencv-python-headless   

COPY face_detection.py /app/face_detection.py
COPY photo_1.jpg /app/photo_1.jpg

WORKDIR /app

CMD ["python", "face_detection.py"]
