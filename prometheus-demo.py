#Grabbed from prometheus docs. Example to see if prometheus works on pc.

from prometheus_client import start_http_server, Summary
import random
import time

#create metric to track time spent and requests made
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing requests')

#Decorate function with metric
@REQUEST_TIME.time()
def process_request(t):
    '''A dummy function that takes some time. '''
    time.sleep(t)

if __name__ == '__main__':
    #start the server to expose metrics
    start_http_server(8000)
    #Generate requests
    while True:
        process_request(random.random())

#On web browser: http://localhost:8000/
