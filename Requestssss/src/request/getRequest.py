import requests

class dataFromWeb:
    def getData(self,Route):
        r = requests.get('https://jsonplaceholder.typicode.com' + Route)
        statuscode = r.status_code

        return statuscode