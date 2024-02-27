from flask import Flask
from prometheus_client import Counter, generate_latest
from prometheus_client.core import CollectorRegistry


app = Flask(__name__)
registry = CollectorRegistry()

# Define your metrics
health_check_metric = Counter('app_healthcheck', 'App Healthcheck Metrics', ['status'], registry=registry)
custom_metric = Counter('custom_metric', 'Custom Metric', ['endpoint'], registry=registry)

@app.route('/')
def index():
    return 'API check status'

@app.route('/health')
def health_check():
   health_check_metric.labels(status='OK').inc()
   return ('I am healthy 200'), 200

@app.route('/metrics')
def metrics():
    return generate_latest(registry), 200

# was not sure if you wanted an actual app so i made nba stats
@app.route('/nbastats')
def trigger():
    
    custom_metric.labels(endpoint='trigger').inc()

    #nba api 
    response = requests.get('https://api.sportradar.com/nba/trial/v8/en/seasons/2022/REG/leaders.json?api_key=hkj7nnf4rcbez8kpjeubctjn')

    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
