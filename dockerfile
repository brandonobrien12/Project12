FROM python:3.10-slim


WORKDIR /app
COPY . /app/Project12-main
RUN pip install --no-cache-dir -r /app/Project12-main/requirements.txt
#RUN prometheus --config.file=prometheus.yml




EXPOSE 5000 9090
#CMD python ./working.py
CMD ["--config.file=/Project12-main/prometheus.yml"]
CMD ["python", "Project12-main/working.py"]




#RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3-dev 
#RUN pip3 install --upgrade pip
#RUN pip3 install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir prometheus_client
#RUN pip install flask
#RUN pip install prometheus_client