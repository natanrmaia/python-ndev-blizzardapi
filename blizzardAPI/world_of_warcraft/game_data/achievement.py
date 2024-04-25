from typing import Optional, Dict, Any
from ...api import API


class Achievement(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_achievement_categories_index(self, **kwargs) -> Dict:
        """
        This function will return the index of achievement categories from the API.

        Requested API:
            /data/wow/achievement-category/index

        Returns:
            A dictionary of the achievement category index.
        """

        api = '/data/wow/achievement-category/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_achievement_category(self, achievement_category_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific achievement category in the World of Warcraft
        game.

        Requested API:
            /data/wow/achievement-category/{achievement_category_id}

        Args:
            achievement_category_id: The ID of the achievement category.

        Returns:
            A dictionary of the achievement category.

        Raises:
            ValueError: If achievement_category_id is not provided.
        """

        if achievement_category_id is None:
            raise ValueError('achievement_category_id is required')

        api = f'/data/wow/achievement-category/{achievement_category_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_achievement_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of achievements from the API.

        Requested API:
            /data/wow/achievement/index

        Returns:
            A dictionary of the achievement index.
        """

        api = '/data/wow/achievement/index'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_achievement(self, achievement_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific achievement in the World of Warcraft game.

        Requested API:
            /data/wow/achievement/{achievement_id}

        Args:
            achievement_id: The ID of the achievement.

        Returns:
            A dictionary of the achievement.

        Raises:
            ValueError: If achievement_id is not provided.
        """

        if achievement_id is None:
            raise ValueError('achievement_id is required')

        api = f'/data/wow/achievement/{achievement_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_achievement_media(self, achievement_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves the media for a specific achievement in the API.

        Requested API:
            /data/wow/media/achievement/{achievement_id}

        Args:
            achievement_id: The ID of the achievement.

        Returns:
            A dictionary of the achievement media.

        Raises:
            ValueError: If achievement_id is not provided.
        """

        if achievement_id is None:
            raise ValueError('achievement_id is required')

        api = f'/data/wow/media/achievement/{achievement_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)