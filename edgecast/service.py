import httplib
import json

from exception import MediaServiceResponseError


class Service(object):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.type


class MediaService(object):
    Host = 'api.edgecast.com'
    Version = 'v2'
    ResponseError = MediaServiceResponseError

    def __init__(self, token):
        self.token = token

    def set_token(self, token):
        self.token = token

    def request(self, method, url, data=None):
        format_spec = 'application/json'
        headers = {
            'Authorization': 'tok: {token}'.format(token=self.token),
            'Accept': format_spec,
            'Host': self.Host,
        }
        url = ('/{version}/{service}' + url).format(
            version=self.Version,
            service=self.service
        )
        if data:
            data = json.dumps(data)
            headers['Content-Type'] = format_spec
        conn = httplib.HTTPSConnection(self.Host)
        conn.request(method, url, body=data, headers=headers)
        res = conn.getresponse()
        if res.status != httplib.OK:
            raise self.ResponseError(res.status, res.reason)
        if int(res.getheader('Content-Length')):
            # Contains a response body
            res = json.loads(res.read())
        else:
            # Does not contain a response body
            res = None
        return res
