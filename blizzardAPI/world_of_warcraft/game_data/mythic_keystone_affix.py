from typing import Dict, Optional, Any
from ...api import API

class MythicKeystoneAffix(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mythic_keystone_affixes_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystone affixes from the API.

        Requested API:
            /data/wow/keystone-affix/index

        Returns:
            A dictionary of the mythic keystone affixes index.
        """

        api = '/data/wow/keystone-affix/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_affix(self, keystone_affix_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic keystone affix from the API.

        Requested API:
            /data/wow/keystone-affix/{keystoneAffixId}

        Args:
            keystone_affix_id: The ID of the mythic keystone affix you want to retrieve.

        Returns:
            A dictionary of the mythic keystone affix details.
        """

        api = f'/data/wow/keystone-affix/{keystone_affix_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_affix_media(self, keystone_affix_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific mythic keystone affix from the API.

        Requested API:
            /data/wow/media/keystone-affix/{keystoneAffixId}

        Args:
            keystone_affix_id: The ID of the mythic keystone affix you want to retrieve.

        Returns:
            A dictionary of the mythic keystone affix media.
        """

        api = f'/data/wow/media/keystone-affix/{keystone_affix_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)