from blizzardAPI.world_of_warcraft.game_data.heirloom import Heirloom

class TestHeirloom:

    def test_get_heirlooms_index(self, api_settings : dict):
        """
        This function tests the get_heirlooms_index function from the Heirloom class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'heirlooms'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        heirloom = Heirloom(api_settings['client_id'], api_settings['client_secret'])
        result = heirloom.get_heirloom_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'heirlooms' in result

    def test_get_heirloom(self, api_settings : dict):
        """
        This function tests the get_heirloom function from the Heirloom class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        heirloom = Heirloom(api_settings['client_id'], api_settings['client_secret'])
        result = heirloom.get_heirloom(4)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result