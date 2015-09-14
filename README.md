### Sample endpoint request

    >>> from edgecast.mediamanagement.cachemanagement import CacheManagement
    >>> cache_management = CacheManagement('e32be1e1-a594-4a98-a374-a5880f313d65')
    >>> load_purge_regions = cache_management.get_load_purge_regions(platform_ids=[2, 3, 8, 14])
    >>> print load_purge_regions[0]
    {"Name": "North America", "Id": 1, "EdgeNodes": [{"Code": "DCA", "Id": 2}, {"Code": "LAX", "Id": 3}, {"Code": "SEA", "Id": 4}, {"Code": "DFW", "Id": 5}, {"Code": "ORD", "Id": 6}, {"Code": "ATL", "Id": 7}, {"Code": "MIA", "Id": 22}, {"Code": "SJC", "Id": 25}, {"Code": "CPM", "Id": 122}, {"Code": "EWR", "Id": 123}, {"Code": "MDW", "Id": 127}, {"Code": "FTW", "Id": 129}, {"Code": "IAD", "Id": 131}, {"Code": "FLL", "Id": 139}, {"Code": "LGA", "Id": 149}, {"Code": "FTY", "Id": 153}, {"Code": "PAE", "Id": 160}, {"Code": "RHV", "Id": 161}, {"Code": "OXR", "Id": 164}, {"Code": "PHL", "Id": 188}, {"Code": "BOS", "Id": 202}]}
