import requests
import json

URL_API = "https://blaze.com"

class Browser(object):

    def __init__(self):
        self.response = None
        self.headers = self.get_headers()
        self.session = requests.Session()

    def get_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36"
        }
        return self.headers

    def send_request(self, method, url, **kwargs):
        response = self.session.request(method, url, **kwargs)
        if response.status_code == 200:
            return response
        return None


class BlazeAPI(Browser):

    def __init__(self):
        super().__init__()

    def get_last_doubles(self):
        self.response = self.send_request("GET",
                                          f"{URL_API}/api/roulette_games/recent",
                                          headers=self.headers)
        if self.response:
            result = {"items": [{"color": "branco" if i["color"] == 0 else "vermelho" if i["color"] == 1 else "verde",
                                 "value": i["roll"]} for i in self.response.json()]}
            return json.dumps(result, indent=4)
        return False

    def get_last_crashs(self):
        self.response = self.send_request("GET",
                                          f"{URL_API}/api/crash_games/recent",
                                          headers=self.headers)
        if self.response:
            result = {"items": [{"color": "preto" if float(i["crash_point"]) < 2 else "verde", "value": i["crash_point"]}
                                for i in self.response.json()]}
            return json.dumps(result, indent=4)
        return False


if __name__ == '__main__':
    ba = BlazeAPI()
    last_doubles = ba.get_last_doubles()
    print(last_doubles)

    last_crashs = ba.get_last_crashs()
    print(last_crashs)

