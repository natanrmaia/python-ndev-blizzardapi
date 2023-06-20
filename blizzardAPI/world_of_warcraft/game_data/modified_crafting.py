from typing import Optional, Dict
from ...api import API

class ModifiedCrafting(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_modified_crafting_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of modified crafting from the API.

        Requested API:
            /data/wow/modified-crafting/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the modified crafting index.
        """

        api = '/data/wow/modified-crafting/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_modified_crafting_category_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of modified crafting category from the API.

        Requested API:
            /data/wow/modified-crafting/category/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the modified crafting category index.
        """

        api = '/data/wow/modified-crafting/category/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_modified_crafting_category(self, region: Optional[str], locale: Optional[str], modified_crafting_category_id: int) -> Dict:
        """
        This function retrieves information about a specific modified crafting category in the World of Warcraft
        game.

        Requested API:
            /data/wow/modified-crafting/category/{modified_crafting_category_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            modified_crafting_category_id: The ID of the modified crafting category.

        Returns:
            A dictionary of the modified crafting category.

        Raises:
            ValueError: If modified_crafting_category_id is not provided.
        """

        if modified_crafting_category_id is None:
            raise ValueError('modified_crafting_category_id is required')

        api = '/data/wow/modified-crafting/category/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(modified_crafting_category_id), query_params)
    
    def get_modified_crafting_reagent_slot_type_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of modified crafting reagent slot type from the API.

        Requested API:
            /data/wow/modified-crafting/reagent-slot-type/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the modified crafting reagent slot type index.
        """

        api = '/data/wow/modified-crafting/reagent-slot-type/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_modified_crafting_reagent_slot_type(self, region: Optional[str], locale: Optional[str], modified_crafting_reagent_slot_type_id: int) -> Dict:
        """
        This function retrieves information about a specific modified crafting reagent slot type in the World of Warcraft
        game.

        Requested API:
            /data/wow/modified-crafting/reagent-slot-type/{modified_crafting_reagent_slot_type_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            modified_crafting_reagent_slot_type_id: The ID of the modified crafting reagent slot type.

        Returns:
            A dictionary of the modified crafting reagent slot type.

        Raises:
            ValueError: If modified_crafting_reagent_slot_type_id is not provided.
        """

        if modified_crafting_reagent_slot_type_id is None:
            raise ValueError('modified_crafting_reagent_slot_type_id is required')

        api = '/data/wow/modified-crafting/reagent-slot-type/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(modified_crafting_reagent_slot_type_id), query_params)