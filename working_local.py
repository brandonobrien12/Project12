from flask import Flask
import creds

app = Flask(__name__)

@app.route('/')
def index():
    return 'API check status'

@app.route('/health')
def health():
    return 'I am healthy', 200

@app.route('/metrics')
def metrics():
    # Logic to gather and format metrics data goes here
    return 'Metrics data', 200

@app.route('/nbastats')
def trigger():
    
    custom_metric.labels(endpoint='trigger').inc()

    #nba api 
    response = requests.get('https://api.sportradar.com/nba/trial/v8/en/league/injuries.json?{creds.api_key}')
    
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
