from typing import Optional, Dict
from ...api import API

class Item(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_item_classes_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of item classes from the API.

        Requested API:
            /data/wow/item-class/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the item class index.
        """

        api = '/data/wow/item-class/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_item_class(self, region: Optional[str], locale: Optional[str], item_class_id: int) -> Dict:
        """
        This function retrieves information about a specific item class in the World of Warcraft
        game.

        Requested API:
            /data/wow/item-class/{item_class_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_class_id: The ID of the item class.

        Returns:
            A dictionary of the item class.

        Raises:
            ValueError: If item_class_id is not provided.
        """

        if item_class_id is None:
            raise ValueError('item_class_id is required')

        api = '/data/wow/item-class/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_class_id), query_params)

    def get_item_sets_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of item sets from the API.

        Requested API:
            /data/wow/item-set/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the item set index.
        """

        api = '/data/wow/item-set/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_item_set(self, region: Optional[str], locale: Optional[str], item_set_id: int) -> Dict:
        """
        This function retrieves information about a specific item set from the API.

        Requested API:
            /data/wow/item-set/{item_set_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_set_id: The ID of the item set.

        Returns:
            A dictionary of the item set.

        Raises:
            ValueError: If item_set_id is not provided.
        """

        if item_set_id is None:
            raise ValueError('item_set_id is required')

        api = '/data/wow/item-set/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_set_id), query_params)

    def get_item_subclass(self, region: Optional[str], locale: Optional[str], item_class_id: int, item_subclass_id: int) -> Dict:
        """
        This function retrieves information about a specific item subclass from the API.

        Requested API:
            /data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_class_id: The ID of the item class.
            item_subclass_id: The ID of the item subclass.

        Returns:
            A dictionary of the item subclass.

        Raises:
            ValueError: If item_class_id or item_subclass_id is not provided.
        """

        if item_class_id is None:
            raise ValueError('item_class_id is required')
        if item_subclass_id is None:
            raise ValueError('item_subclass_id is required')

        api = '/data/wow/item-class/{}/item-subclass/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_class_id, item_subclass_id), query_params)

    def get_item(self, region: Optional[str], locale: Optional[str], item_id: int) -> Dict:
        """
        This function retrieves information about a specific item from the API.

        Requested API:
            /data/wow/item/{item_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_id: The ID of the item.

        Returns:
            A dictionary of the item.

        Raises:
            ValueError: If item_id is not provided.
        """

        if item_id is None:
            raise ValueError('item_id is required')

        api = '/data/wow/item/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_id), query_params)

    def get_item_media(self, region: Optional[str], locale: Optional[str], item_id: int) -> Dict:
        """
        This function retrieves media information about a specific item from the API.

        Requested API:
            /data/wow/media/item/{item_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_id: The ID of the item.

        Returns:
            A dictionary of the item media.

        Raises:
            ValueError: If item_id is not provided.
        """

        if item_id is None:
            raise ValueError('item_id is required')

        api = '/data/wow/media/item/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_id), query_params)

    def get_item_media(self, region: Optional[str], locale: Optional[str], item_id: int) -> Dict:
        """
        This function retrieves media information about a specific item from the API.

        Requested API:
            /data/wow/media/item/{item_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            item_id: The ID of the item.

        Returns:
            A dictionary of the item media.

        Raises:
            ValueError: If item_id is not provided.
        """

        if item_id is None:
            raise ValueError('item_id is required')

        api = '/data/wow/media/item/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(item_id), query_params)

    def get_item_search(self, region: Optional[str], locale: Optional[str], name_en: Optional[str], order_by: Optional[str], page: Optional[int]) -> Dict:
        """
        This function will perform a search of items from the API.

        Requested API:
            /data/wow/search/item

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            name_en: The name of the item in English.
            order_by: The field to order the results by.

        Returns:
            A dictionary of the item search results.
        """

        api = '/data/wow/search/item'

        query_params = {
            'namespace': 'static',
            'locale': locale,
            'name.en_US': name_en,
            'orderby': order_by,
            'page': page,
        }

        return super().get_api(region, api, query_params)