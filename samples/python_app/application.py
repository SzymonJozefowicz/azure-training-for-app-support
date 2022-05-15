from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
from datetime import datetime
import requests

app = Flask(__name__)
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string="InstrumentationKey=<Instrumentation_key>"),
    sampler=ProbabilitySampler(rate=1.0),
)


@app.route('/time')
def hello():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Current time {current_time}')
    return f'current_time: {current_time}'


@app.route('/')
def google():
    x = requests.get('https://google.com/search?q=Azure Application Insights Documentation')
    return x.text



if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=True)