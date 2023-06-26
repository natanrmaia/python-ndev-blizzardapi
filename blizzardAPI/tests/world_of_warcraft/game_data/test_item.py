from blizzardAPI.world_of_warcraft.game_data.item import Item

class TestItem:

    def test_get_item_classes_index(self, api_settings : dict):
        """
        This function tests the get_item_classes_index function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'item_classes'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_classes_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'item_classes' in result

    def test_get_item_class(self, api_settings : dict):
        """
        This function tests the get_item_class function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'item_subclasses'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_class(2)

        if not isinstance(result, dict):
            return False
        else:
            assert 'item_subclasses' in result

    def test_get_item_subclass(self, api_settings : dict):
        """
        This function tests the get_item_subclass function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'display_name'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_subclass(2, 4)

        if not isinstance(result, dict):
            return False
        else:
            assert 'display_name' in result

    def test_get_item(self, api_settings : dict):
        """
        This function tests the get_item function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item(19019)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_item_media(self, api_settings : dict):
        """
        This function tests the get_item_media function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_media(19019)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_item_set_index(self, api_settings : dict):
        """
        This function tests the get_item_set_index function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'item_sets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_sets_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'item_sets' in result

    def test_get_item_set(self, api_settings : dict):
        """
        This function tests the get_item_set function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_set(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_item_search(self, api_settings : dict):
        """
        This function tests the get_item_search function from the Item class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
        
        item = Item(api_settings['client_id'], api_settings['client_secret'])
        result = item.get_item_search()

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result