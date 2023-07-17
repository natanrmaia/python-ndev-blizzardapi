from blizzardAPI.world_of_warcraft.game_data.power_type import PowerType

class TestPowerType:

    def test_get_power_type_index(self, api_settings : dict):
        """
        This function tests the get_power_type_index function from the PowerType class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'power_types'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        power_type = PowerType(api_settings['client_id'], api_settings['client_secret'])
        result = power_type.get_power_type_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'power_types' in result

    def test_get_power_type(self, api_settings : dict):
        """
        This function tests the get_power_type function from the PowerType class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        power_type = PowerType(api_settings['client_id'], api_settings['client_secret'])
        result = power_type.get_power_type(2)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result