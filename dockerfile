FROM ubuntu

WORKDIR /app

COPY requirements.txt /app/requirements.txt
#COPY stress/stressdetection/app /app/stress/stressdetection/app
COPY stress/app /app/stress/app


RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \
    cd stress/stressdetection

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

