from typing import Optional, Dict, Any
from ...api import API


class Quest(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_quests_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of quests from the API.

        Requested API:
            /data/wow/quest/index

        Returns:
            A dictionary of the quests index.
        """

        api = '/data/wow/quest/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest(self, quest_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific quest from the API.

        Requested API:
            /data/wow/quest/{quest_id}

        Args:
            quest_id: The ID of the quest.

        Returns:
            A dictionary of the quest.

        Raises:
            ValueError: If quest_id is not provided.
        """

        if quest_id is None:
            raise ValueError('quest_id is required')

        api = f'/data/wow/quest/{quest_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_categories_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of quest categories from the API.

        Requested API:
            /data/wow/quest/category/index

        Returns:
            A dictionary of the quest categories index.
        """

        api = '/data/wow/quest/category/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_category(self, quest_category_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific quest category from the API.

        Requested API:
            /data/wow/quest/category/{quest_category_id}

        Args:
            quest_category_id: The ID of the quest category.

        Returns:
            A dictionary of the quest category.

        Raises:
            ValueError: If quest_category_id is not provided.
        """

        if quest_category_id is None:
            raise ValueError('quest_category_id is required')

        api = f'/data/wow/quest/category/{quest_category_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_areas_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of quest areas from the API.

        Requested API:
            /data/wow/quest/area/index


        Returns:
            A dictionary of the quest areas index.
        """

        api = '/data/wow/quest/area/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_area(self, quest_area_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific quest area from the API.

        Requested API:
            /data/wow/quest/area/{quest_area_id}

        Args:
            quest_area_id: The ID of the quest area.

        Returns:
            A dictionary of the quest area.

        Raises:
            ValueError: If quest_area_id is not provided.
        """

        if quest_area_id is None:
            raise ValueError('quest_area_id is required')

        api = f'/data/wow/quest/area/{quest_area_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_types_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of quest types from the API.

        Requested API:
            /data/wow/quest/type/index

        Returns:
            A dictionary of the quest types index.
        """

        api = '/data/wow/quest/type/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_quest_type(self, quest_type_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific quest type from the API.

        Requested API:
            /data/wow/quest/type/{quest_type_id}

        Args:
            quest_type_id: The ID of the quest type.

        Returns:
            A dictionary of the quest type.

        Raises:
            ValueError: If quest_type_id is not provided.
        """

        if quest_type_id is None:
            raise ValueError('quest_type_id is required')

        api = f'/data/wow/quest/type/{quest_type_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)