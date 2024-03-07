from flask import Flask, jsonify
from prometheus_client import start_http_server, Counter
import creds

app = Flask(__name__)

#Initialize Prometheus metrics registry
REQUEST_COUNT = Counter('request_count', 'App Request Count', ['method', 'endpoint', 'http_status'])


# Define your metrics
#health_check_metric = Counter('app_healthcheck', 'App Healthcheck Metrics', ['status'], registry=registry)
#custom_metric = Counter('custom_metric', 'Custom Metric', ['endpoint'], registry=registry)

@app.route('/')
def index():
    return jsonify(message="You are on the index page. Use /health /metrics /nbastats"), 200

@app.route('/health')
#def health_check():
   #health_check_metric.labels(status='OK').inc()
   #return ('I am healthy 200'), 200
def health():
    return jsonify(message="I'm healthy"), 200

@app.route('/metrics')
def metrics():
    #return generate_latest(registry), 200
    REQUEST_COUNT.labels(method='GET', endpoint='/metrics', http_status='200').inc()
    return str(REQUEST_COUNT)

# was not sure if you wanted an actual app so i made nba stats
@app.route('/nbastats')
def trigger():
    
    custom_metric.labels(endpoint='trigger').inc()

    #nba api 
   
    response = requests.get('https://api.sportradar.com/nba/trial/v8/en/league/injuries.json?{creds.api_key}')
    

    return response.json(), response.status_code
    print(api_key)

if __name__ == '__main__':
    # Start Prometheus metrics endpoint
    start_http_server(8000)
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
