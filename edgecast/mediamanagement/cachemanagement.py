from edgecast.mediamanagement import MediaManagement


class CacheManagement(MediaManagement):
    def __init__(self, token):
        super(CacheManagement, self).__init__(token)

    def get_load_purge_regions(self, platform_ids=None):
        """Retrieves a list of platform-specific load/purge regions"""
        platform_ids = ','.join(
            [str(platform_id) for platform_id in platform_ids]
        )
        url = '/lpqregions?mediaTypes={platform_ids}'.format(
            platform_ids=platform_ids
        )
        res = self.request('GET', url)
        return res

    def get_purge_request(self, account_number=None, purge_id=None):
        """Retrieves information about a purge request"""
        url = '/customers/{account_number}/edge/purge/{purge_id}'.format(
            account_number=account_number,
            purge_id=purge_id
        )
        res = self.request('GET', url)
        return res

    def load_content(self, account_number=None, data=None):
        """Loads an asset on our edge servers"""
        url = '/customers/{account_number}/edge/load'.format(
            account_number=account_number
        )
        res = self.request('PUT', url, data=data)
        return res

    def purge_content(self, account_number=None, data=None):
        """Purges the cached version of an asset from our edge servers"""
        url = '/customers/{account_number}/edge/purge'.format(
            account_number=account_number
        )
        res = self.request('PUT', url, data=data)
        return res
