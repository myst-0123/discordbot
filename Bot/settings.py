import configparser

class Settings():
    def __init__(self):
        config_file = configparser.ConfigParser()
        config_file.read('../config.ini')
        self.TOKEN = config_file.get('setting', 'token')
        self.CHANNEL_ID = int(config_file.get('setting', 'channel_id'))
        self.VOICE_CHANNEL_ID = int(config_file.get('setting', 'voice_channel_id'))
        self.MY_CHANNEL_ID = int(config_file.get('setting', 'my_channel_id'))
