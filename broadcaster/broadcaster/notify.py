"""
"""
import pushnotify

class Client():

    apikey = '01b175b9e47a92f1bd2a199268266fa648abacac77a439f1'
    client = None
    priority = 0

    def __init__(self, developerkey, application):
        self.client = pushnotify.get_client('nma', application=application)
        self.client.add_key(self.apikey)

    def alert(self, desc, event = None):
        self.priority = 2
        self.pushnotify_msg(desc, event)

    def notify(self, desc, event = None):
        self.priority = 0
        self.pushnotify_msg(desc, event)

    def whisper(self, desc, event = None):
        self.priority = -2
        self.pushnotify_msg(desc, event)

    def pushnotify_msg(self, desc, event):
        if event is None:
            event = ''
        #kwargs = { 'priority': self.priority}
        # an exception will be raised because the API Key is invalid
        try:
            self.client.notify(desc, event, split=True)
        except pushnotify.exceptions.ApiKeyError:
            pass
