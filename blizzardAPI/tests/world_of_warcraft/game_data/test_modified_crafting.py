from blizzardAPI.world_of_warcraft.game_data.modified_crafting import ModifiedCrafting

class TestModifiedCrafting:

    def test_get_modified_crafting_index(self, api_settings : dict):
        """
        This function tests the get_modified_crafting_index function from the ModifiedCrafting class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'categories'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        modified_crafting = ModifiedCrafting(api_settings['client_id'], api_settings['client_secret'])
        result = modified_crafting.get_modified_crafting_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result

    def test_get_modified_crafting_category_index(self, api_settings : dict):
        """
        This function tests the get_modified_crafting_category_index function from the ModifiedCrafting class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'categories'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        modified_crafting = ModifiedCrafting(api_settings['client_id'], api_settings['client_secret'])
        result = modified_crafting.get_modified_crafting_category_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result

    def test_get_modified_crafting_category(self, api_settings : dict):
        """
        This function tests the get_modified_crafting_category function from the ModifiedCrafting class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        modified_crafting = ModifiedCrafting(api_settings['client_id'], api_settings['client_secret'])
        result = modified_crafting.get_modified_crafting_category(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_modified_crafting_reagent_slot_type_index(self, api_settings : dict):
        """
        This function tests the get_modified_crafting_reagent_slot_type_index function from the ModifiedCrafting class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'reagent_slot_types'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        modified_crafting = ModifiedCrafting(api_settings['client_id'], api_settings['client_secret'])
        result = modified_crafting.get_modified_crafting_reagent_slot_type_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'slot_types' in result

    def test_get_modified_crafting_reagent_slot_type(self, api_settings : dict):
        """
        This function tests the get_modified_crafting_reagent_slot_type function from the ModifiedCrafting class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        modified_crafting = ModifiedCrafting(api_settings['client_id'], api_settings['client_secret'])
        result = modified_crafting.get_modified_crafting_reagent_slot_type(16)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result