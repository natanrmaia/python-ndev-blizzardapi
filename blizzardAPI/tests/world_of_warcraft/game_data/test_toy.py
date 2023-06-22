from blizzardAPI.world_of_warcraft.game_data.toy import Toy

class TestToy:

    def test_get_toy_index(self, api_settings : dict):
        """
        This function tests the get_toy_index function from the Toy class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        toy = Toy(api_settings['client_id'], api_settings['client_secret'])
        result = toy.get_toy_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result['toys'][0]

    def test_get_toy(self, api_settings : dict):
        """
        This function tests the get_toy function from the Toy class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        toy = Toy(api_settings['client_id'], api_settings['client_secret'])
        result = toy.get_toy(30)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result