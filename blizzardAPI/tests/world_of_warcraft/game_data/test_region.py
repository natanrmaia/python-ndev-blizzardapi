from blizzardAPI.world_of_warcraft.game_data.region import Region

class TestRegion:

    def test_get_regions_index(self, api_settings : dict):
        """
        This function tests the get_regions_index function from the Region class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'regions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        region = Region(api_settings['client_id'], api_settings['client_secret'])
        result = region.get_regions_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'regions' in result

    def test_get_region(self, api_settings : dict):
        """
        This function tests the get_region function from the Region class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        region = Region(api_settings['client_id'], api_settings['client_secret'])
        result = region.get_region(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result