FROM python:3-alpine3.14
#RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3-dev 
#RUN pip3 install --upgrade pip
#RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir prometheus_client
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
#RUN pip3 --no-cache-dir install -r requirements.txt
expose 5000
#CMD python ./working.py
CMD ["python3", "working.py"]