FROM python:3.10-slim
#RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3-dev 
#RUN pip3 install --upgrade pip
#RUN pip3 install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir prometheus_client
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install prometheus_client
RUN pip install -r requirements.txt
#RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000 9090
#CMD python ./working.py
CMD ["python3", "working.py"]