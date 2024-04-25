from typing import Optional, Dict, Any
from ...api import API


class TechTalent(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_tech_talent_tree_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of Tech Talent Tree from the API.

        Requested API:
            /data/wow/tech-talent-tree/index

        Returns:
            A dictionary of the Tech Talent Tree index.
        """

        api = '/data/wow/tech-talent-tree/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_tech_talent_tree(self, tech_talent_tree_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific Tech Talent Tree from the API.

        Requested API:
            /data/wow/tech-talent-tree/{tech_talent_tree_id}

        Args:
            tech_talent_tree_id: The ID of the Tech Talent Tree.

        Returns:
            A dictionary of the Tech Talent Tree.

        Raises:
            ValueError: If tech_talent_tree_id is not provided.
        """

        if tech_talent_tree_id is None:
            raise ValueError('tech_talent_tree_id is required')

        api = f'/data/wow/tech-talent-tree/{tech_talent_tree_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_tech_talent_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of Tech Talent from the API.

        Requested API:
            /data/wow/tech-talent/index

        Returns:
            A dictionary of the Tech Talent index.
        """

        api = '/data/wow/tech-talent/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_tech_talent(self, tech_talent_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific Tech Talent from the API.

        Requested API:
            /data/wow/tech-talent/{tech_talent_id}

        Args:
            tech_talent_id: The ID of the Tech Talent.

        Returns:
            A dictionary of the Tech Talent.

        Raises:
            ValueError: If tech_talent_id is not provided.
        """

        if tech_talent_id is None:
            raise ValueError('tech_talent_id is required')

        api = f'/data/wow/tech-talent/{tech_talent_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_tech_talent_media(self, tech_talent_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves media information about a specific Tech Talent from the API.

        Requested API:
            /data/wow/media/tech-talent/{tech_talent_id}

        Args:
            tech_talent_id: The ID of the Tech Talent.

        Returns:
            A dictionary of the Tech Talent media.

        Raises:
            ValueError: If tech_talent_id is not provided.
        """

        if tech_talent_id is None:
            raise ValueError('tech_talent_id is required')

        api = f'/data/wow/media/tech-talent/{tech_talent_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)