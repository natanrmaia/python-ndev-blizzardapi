from blizzardAPI.world_of_warcraft.game_data.azerite_essence import AzeriteEssence

class TestAzeriteEssence:

    def test_get_azerite_essences_index(self, api_settings : dict):
        """
        This function tests the get_azerite_essences_index function from the AzeriteEssence class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'essences'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        azerite_essence = AzeriteEssence(api_settings['client_id'], api_settings['client_secret'])
        result = azerite_essence.get_azerite_essences_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'azerite_essences' in result

    def test_get_azerite_essence(self, api_settings : dict):
        """
        This function tests the get_azerite_essence function from the AzeriteEssence class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        azerite_essence = AzeriteEssence(api_settings['client_id'], api_settings['client_secret'])
        result = azerite_essence.get_azerite_essence(4)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_azerite_essence_search(self, api_settings : dict):
        """
        This function tests the get_azerite_essence_search function from the AzeriteEssence class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        azerite_essence = AzeriteEssence(api_settings['client_id'], api_settings['client_secret'])
        result = azerite_essence.get_azerite_essence_search()

        if not isinstance (result, dict):
            return False
        
        else:
            assert 'results' in result

    def test_get_azerite_essence_media(self, api_settings : dict):
        """
        This funcion tests the get_azerite_essence_media function from the AzeriteEssence class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        azerite_essence = AzeriteEssence(api_settings['client_id'], api_settings['client_secret'])
        result = azerite_essence.get_azerite_essence_media(4)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result