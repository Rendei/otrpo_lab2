FROM jupyter/scipy-notebook:latest

# RUN apt-get update && \
#     apt-get install -y build-essential \
#     && apt-get clean



RUN pip install --no-cache-dir opencv-python-headless opencv-python

COPY face_detection.py /app/face_detection.py
COPY photo_1.jpg /app/photo_1.jpg

WORKDIR /app

ENV DISPLAY=:0

ENTRYPOINT ["python", "face_detection.py"]
