from edgecast import MediaService
from edgecast import Service


class MediaManagement(MediaService):
    def __init__(self, token):
        super(MediaManagement, self).__init__(token)
        self.service = Service('mcc')
