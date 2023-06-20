from typing import Dict, Optional
from ...api import API

class MythicKeystoneAffix(API):
    def get_mythic_keystone_affixes_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mythic keystone affixes from the API.

        Requested API:
            /data/wow/keystone-affix/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone affixes index.
        """

        api = '/data/wow/keystone-affix/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_affix(self, region: Optional[str], locale: Optional[str], keystone_affix_id: int) -> Dict:
        """
        This function will return the details of a specific mythic keystone affix from the API.

        Requested API:
            /data/wow/keystone-affix/{keystoneAffixId}

        Args:
            region: The region of the API you want to access.
            keystone_affix_id: The ID of the mythic keystone affix you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone affix details.
        """

        api = f'/data/wow/keystone-affix/{keystone_affix_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_affix_media(self, region: Optional[str], locale: Optional[str], keystone_affix_id: int) -> Dict:
        """
        This function will return the media of a specific mythic keystone affix from the API.

        Requested API:
            /data/wow/media/keystone-affix/{keystoneAffixId}

        Args:
            region: The region of the API you want to access.
            keystone_affix_id: The ID of the mythic keystone affix you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone affix media.
        """

        api = f'/data/wow/media/keystone-affix/{keystone_affix_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)