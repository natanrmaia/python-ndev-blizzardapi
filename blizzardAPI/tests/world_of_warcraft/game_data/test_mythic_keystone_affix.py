from blizzardAPI.world_of_warcraft.game_data.mythic_keystone_affix import MythicKeystoneAffix

class TestMythicKeystoneAffix:

    def test_get_mythic_keystone_affixes_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_affixes_index function from the MythicKeystoneAffix class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'affixes'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_affix = MythicKeystoneAffix(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_affix.get_mythic_keystone_affixes_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'affixes' in result

    def test_get_mythic_keystone_affix(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_affix function from the MythicKeystoneAffix class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_affix = MythicKeystoneAffix(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_affix.get_mythic_keystone_affix(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_mythic_keystone_affix_media(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_affix_media function from the MythicKeystoneAffix class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_affix = MythicKeystoneAffix(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_affix.get_mythic_keystone_affix_media(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result