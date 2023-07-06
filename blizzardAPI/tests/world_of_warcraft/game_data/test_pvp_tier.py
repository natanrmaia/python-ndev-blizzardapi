from blizzardAPI.world_of_warcraft.game_data.pvp_tier import PvPTier

class TestPvPTier:

    def test_get_pvp_tiers_index(self, api_settings : dict):
        """
        This function tests the get_pvp_tiers_index function from the PvPTier class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'tiers'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_tier = PvPTier(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_tier.get_pvp_tiers_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'tiers' in result

    def test_get_pvp_tier(self, api_settings : dict):
        """
        This function tests the get_pvp_tier function from the PvPTier class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_tier = PvPTier(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_tier.get_pvp_tier(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_pvp_tier_media(self, api_settings : dict):
        """
        This function tests the get_pvp_tier_media function from the PvPTier class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_tier = PvPTier(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_tier.get_pvp_tier_media(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result