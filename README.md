
# API Project New Hire

This project will create a API that displays health, metrics, and basketball statistics from SportRadar.


## Tech Stack


** Items needed to be installed **
python 3,
prometheus,
grafana,
Flask

to install Items

pip3 install python
brew install prometheus
brew install grafana
pip3 install Flask

** Language ** 
python


## Deployment

To deploy this project locally

use as a test to run locally. Make sure your working_local script is not on the same port number as working script. Execute from the folder of same folder the script is saved in

```bash
python working_local.py

```bash
  python working.py
```



## API Reference

#### Get all items

```http
  GET https://api.sportradar.com/nba/trial/v8/en
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. hkj7nnf4rcbez8kpjeubctjn |

#### Get item

```http
  GET /seasons/2022/REG/leaders.json?api_key=hkj7nnf4rcbez8kpjeubctjn'
```



## Installation for docker and grafana



```bash

Complete on docker:
docker build -t bobuckets/hey-python-flask:latest . 

docker container run -d -p 5000:5000 bobuckets/hey-python-flask:latest

docker container ls
  
ADD Prometheus
  docker run -d -p 5000:5000 --bobuckets/hey-python-flask:latest prometheus prom/prometheus

Add Grafana
docker run -d -p 5000:5000 --bobuckets/hey-python-flask:latest grafana grafana/grafana

```
    