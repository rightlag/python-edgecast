from edgecast import service


class MediaManagement(service.MediaService):
    def __init__(self, token):
        super(MediaManagement, self).__init__(token)
        self.service = service.Service('mcc')
