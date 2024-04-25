from typing import Optional, Dict, Any
from ...api import API

class ModifiedCrafting(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_modified_crafting_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of modified crafting from the API.

        Requested API:
            /data/wow/modified-crafting/index

        Returns:
            A dictionary of the modified crafting index.
        """

        api = '/data/wow/modified-crafting/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_modified_crafting_category_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of modified crafting category from the API.

        Requested API:
            /data/wow/modified-crafting/category/index

        Returns:
            A dictionary of the modified crafting category index.
        """

        api = '/data/wow/modified-crafting/category/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_modified_crafting_category(self, modified_crafting_category_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific modified crafting category in the World of Warcraft
        game.

        Requested API:
            /data/wow/modified-crafting/category/{modified_crafting_category_id}

        Args:
            modified_crafting_category_id: The ID of the modified crafting category.

        Returns:
            A dictionary of the modified crafting category.

        Raises:
            ValueError: If modified_crafting_category_id is not provided.
        """

        if modified_crafting_category_id is None:
            raise ValueError('modified_crafting_category_id is required')

        api = f'/data/wow/modified-crafting/category/{modified_crafting_category_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_modified_crafting_reagent_slot_type_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of modified crafting reagent slot type from the API.

        Requested API:
            /data/wow/modified-crafting/reagent-slot-type/index

        Returns:
            A dictionary of the modified crafting reagent slot type index.
        """

        api = '/data/wow/modified-crafting/reagent-slot-type/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_modified_crafting_reagent_slot_type(self, modified_crafting_reagent_slot_type_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific modified crafting reagent slot type in the World of Warcraft
        game.

        Requested API:
            /data/wow/modified-crafting/reagent-slot-type/{modified_crafting_reagent_slot_type_id}

        Args:
            modified_crafting_reagent_slot_type_id: The ID of the modified crafting reagent slot type.

        Returns:
            A dictionary of the modified crafting reagent slot type.

        Raises:
            ValueError: If modified_crafting_reagent_slot_type_id is not provided.
        """

        if modified_crafting_reagent_slot_type_id is None:
            raise ValueError('modified_crafting_reagent_slot_type_id is required')

        api = f'/data/wow/modified-crafting/reagent-slot-type/{modified_crafting_reagent_slot_type_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)