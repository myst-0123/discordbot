import json

class Settings():
    def __init__(self):
        self.admin_list = []
        with open('../config.json', 'r') as f:
            config = json.load(f)
            self.TOKEN = config['settings']['token']
            self.CHANNEL_ID = config['settings']['channel_id']
            self.VOICE_CHANNEL_ID = config['settings']['voice_channel_id']
            self.MY_CHANNEL_ID = config['settings']['my_channel_id']
            for x in config['administrator']:
                self.admin_list.append(x['id'])
