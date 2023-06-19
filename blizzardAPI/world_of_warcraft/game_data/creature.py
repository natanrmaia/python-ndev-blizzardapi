from typing import Optional, Dict
from ...api import API

class Creature(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_creature_families_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of creature families from the API.

        Requested API:
            /data/wow/creature-family/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the creature family index.
        """

        api = '/data/wow/creature-family/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_creature_family(self, region: Optional[str], locale: Optional[str], creature_family_id: int) -> Dict:
        """
        This function retrieves information about a specific creature family in the World of Warcraft
        game.
        
        Requested API:
            /data/wow/creature-family/{creature_family_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            creature_family_id: The ID of the creature family.
        
        Returns:
            A dictionary of the creature family.

        Raises:
            ValueError: If creature_family_id is not provided.
        """

        if creature_family_id is None:
            raise ValueError('creature_family_id is required')

        api = '/data/wow/creature-family/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(creature_family_id), query_params)
    
    def get_creature_types_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of creature types from the API.

        Requested API:
            /data/wow/creature-type/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the creature type index.
        """

        api = '/data/wow/creature-type/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_creature_type(self, region: Optional[str], locale: Optional[str], creature_type_id: int) -> Dict:
        """
        This function retrieves information about a specific creature type in the World of Warcraft
        game.
        
        Requested API:
            /data/wow/creature-type/{creature_type_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            creature_type_id: The ID of the creature type.
        
        Returns:
            A dictionary of the creature type.

        Raises:
            ValueError: If creature_type_id is not provided.
        """

        if creature_type_id is None:
            raise ValueError('creature_type_id is required')

        api = '/data/wow/creature-type/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(creature_type_id), query_params)
    
    def get_creature(self, region: Optional[str], locale: Optional[str], creature_id: int) -> Dict:
        """
        This function retrieves information about a specific creature in the World of Warcraft game.

        Requested API:
            /data/wow/creature/{creature_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            creature_id: The ID of the creature.

        Returns:
            A dictionary of the creature.

        Raises:
            ValueError: If creature_id is not provided.
        """

        if creature_id is None:
            raise ValueError('creature_id is required')

        api = '/data/wow/creature/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(creature_id), query_params)
    
    def get_creature_search(self, region: Optional[str], locale: Optional[str], name_en: Optional[str], order_by: Optional[str], page: Optional[int]) -> Dict:
        """
        This function searches for creatures with the given search parameters.

        Requested API:
            /data/wow/search/creature

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            name_en: The English name of the creature.
            order_by: How to order the results.
            page: The page number to get.

        Returns:
            A dictionary of the creature search results.
        """

        api = '/data/wow/search/creature'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        if name_en is not None:
            query_params['name.en_US'] = name_en

        if order_by is not None:
            query_params['orderby'] = order_by

        if page is not None:
            query_params['page'] = page

        return super().get_api(region, api, query_params)
    
    def get_creature_display_media(self, region: Optional[str], locale: Optional[str], creature_display_id: int) -> Dict:
        """
        This function retrieves the media for a specific creature display.

        Requested API:
            /data/wow/media/creature-display/{creature_display_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            creature_display_id: The ID of the creature display media.

        Returns:
            A dictionary of the creature display media.

        Raises:
            ValueError: If creature_display_id is not provided.
        """

        if creature_display_id is None:
            raise ValueError('creature_display_id is required')

        api = '/data/wow/media/creature-display/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(creature_display_id), query_params)
    
    def get_creature_family_media(self, region: Optional[str], locale: Optional[str], creature_family_id: int) -> Dict:
        """
        This function retrieves the media for a specific creature family.

        Requested API:
            /data/wow/media/creature-family/{creature_family_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            creature_family_id: The ID of the creature family media.

        Returns:
            A dictionary of the creature family media.

        Raises:
            ValueError: If creature_family_id is not provided.
        """

        if creature_family_id is None:
            raise ValueError('creature_family_id is required')

        api = '/data/wow/media/creature-family/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(creature_family_id), query_params)