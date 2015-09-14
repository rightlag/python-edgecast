class MediaServiceResponseError(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason

    def __str__(self):
        return '{} {}'.format(self.status, self.reason)
