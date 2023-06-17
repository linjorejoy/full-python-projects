  
import requests
import json

class telegram_chatbot():

    def __init__(self):
        self.token = self.read_token_from_config_file()
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self):
        token_json = None
        with open("config.json", 'r') as json_file:
            token_json = json.load(json_file)
        
        return token_json['token']


