from typing import Optional, Dict, Any
from ...api import API


class Talent(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_talent_tree_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of talent trees from the API.

        Requested API:
            /data/wow/talent-tree/index

        Returns:
            A dictionary of the talent trees index.
        """

        api = '/data/wow/talent-tree/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_talent_tree(self, talent_tree_id: int, spec_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific talent tree from the API.

        Requested API:
            /data/wow/talent-tree/{talent_tree_id}/playable-specialization/{spec_id}

        Args:
            talent_tree_id: The ID of the talent tree.
            spec_id: The ID of the specialization.

        Returns:
            A dictionary of the talent tree.

        Raises:
            ValueError: If talent_tree_id or spec_id is not provided.
        """

        if talent_tree_id is None:
            raise ValueError('talent_tree_id is required')
        if spec_id is None:
            raise ValueError('spec_id is required')

        api = f'/data/wow/talent-tree/{talent_tree_id}/playable-specialization/{spec_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_talent_tree_nodes(self, talent_tree_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific talent tree nodes from the API.

        Requested API:
            /data/wow/talent-tree/{talent_tree_id}

        Args:
            talent_tree_id: The ID of the talent tree.

        Returns:
            A dictionary of the talent tree nodes.

        Raises:
            ValueError: If talent_tree_id is not provided.
        """

        if talent_tree_id is None:
            raise ValueError('talent_tree_id is required')

        api = f'/data/wow/talent-tree/{talent_tree_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_talents_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of talents from the API.

        Requested API:
            /data/wow/talent/index

        Returns:
            A dictionary of the talents index.
        """

        api = '/data/wow/talent/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_talent(self, talent_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific talent from the API.

        Requested API:
            /data/wow/talent/{talent_id}

        Args:
            talent_id: The ID of the talent.

        Returns:
            A dictionary of the talent.

        Raises:
            ValueError: If talent_id is not provided.
        """

        if talent_id is None:
            raise ValueError('talent_id is required')

        api = f'/data/wow/talent/{talent_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_talents_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of PvP talents from the API.

        Requested API:
            /data/wow/pvp-talent/index

        Returns:
            A dictionary of the PvP talents index.
        """

        api = '/data/wow/pvp-talent/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_talent(self, pvp_talent_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific PvP talent from the API.

        Requested API:
            /data/wow/pvp-talent/{pvp_talent_id}

        Args:
            pvp_talent_id: The ID of the PvP talent.

        Returns:
            A dictionary of the PvP talent.

        Raises:
            ValueError: If pvp_talent_id is not provided.
        """

        if pvp_talent_id is None:
            raise ValueError('pvp_talent_id is required')

        api = f'/data/wow/pvp-talent/{pvp_talent_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)