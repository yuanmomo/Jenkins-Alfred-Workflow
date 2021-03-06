import os
import urllib

class Job(object):
    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        return urllib.unquote(self._data.get('name', ''))

    @property
    def url(self):
        return self._data.get('url')

    @property
    def status(self):
        return self._data.get('color')

    @property
    def image(self):
        return "{}/images/{}.png".format(os.getcwdu(), self.status)

    @property
    def description(self):
        return self._data.get('description', "")
