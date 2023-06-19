from typing import Optional, Dict
from ...api import API


class Achievement(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_achievement_categories_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of achievement categories from the API.

        Requested API:
            /data/wow/achievement-category/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the achievement category index.
        """

        api = '/data/wow/achievement-category/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_achievement_category(self, region: Optional[str], locale: Optional[str], achievement_category_id: int) -> Dict:
        """
        This function retrieves information about a specific achievement category in the World of Warcraft
        game.
        
        Requested API:
            /data/wow/achievement-category/{achievement_category_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            achievement_category_id: The ID of the achievement category.
        
        Returns:
            A dictionary of the achievement category.

        Raises:
            ValueError: If achievement_category_id is not provided.
        """

        if achievement_category_id is None:
            raise ValueError('achievement_category_id is required')

        api = '/data/wow/achievement-category/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(achievement_category_id), query_params)
    
    def get_achievement_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of achievements from the API.

        Requested API:
            /data/wow/achievement/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
        
        Returns:
            A dictionary of the achievement index.
        """

        api = '/data/wow/achievement/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_achievement(self, region: Optional[str], locale: Optional[str], achievement_id: int) -> Dict:
        """
        This function retrieves information about a specific achievement in the World of Warcraft game.

        Requested API:
            /data/wow/achievement/{achievement_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            achievement_id: The ID of the achievement.

        Returns:
            A dictionary of the achievement.

        Raises:
            ValueError: If achievement_id is not provided.
        """

        if achievement_id is None:
            raise ValueError('achievement_id is required')

        api = '/data/wow/achievement/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(achievement_id), query_params)
    
    def get_achievement_media(self, region: Optional[str], locale: Optional[str], achievement_id: int) -> Dict:
        """
        This function retrieves the media for a specific achievement in the API.

        Requested API:
            /data/wow/media/achievement/{achievement_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            achievement_id: The ID of the achievement.

        Returns:
            A dictionary of the achievement media.

        Raises:
            ValueError: If achievement_id is not provided.
        """

        if achievement_id is None:
            raise ValueError('achievement_id is required')

        api = '/data/wow/media/achievement/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(achievement_id), query_params)