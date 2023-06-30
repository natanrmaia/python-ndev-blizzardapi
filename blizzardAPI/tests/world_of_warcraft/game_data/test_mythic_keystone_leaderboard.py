from blizzardAPI.world_of_warcraft.game_data.mythic_keystone_leaderboard import MythicKeystoneLeaderboard

class TestMythicKeystoneLeaderboard:

    def test_get_mythic_keystone_leaderboards_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_leaderboards_index function from the MythicKeystoneLeaderboard class.

        This function will test the following:
            - If the function returns a dict.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_leaderboard = MythicKeystoneLeaderboard(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_leaderboard.get_mythic_keystone_leaderboards_index(11)

        if not isinstance(result, dict):
            return False
        else:
            assert 'current_leaderboards' in result
        
    def test_get_mythic_keystone_leaderboard(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_leaderboard function from the MythicKeystoneLeaderboard class.

        This function will test the following:
            - If the function returns a dict.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_leaderboard = MythicKeystoneLeaderboard(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_leaderboard.get_mythic_keystone_leaderboard(11, 197, 197)

        if not isinstance(result, dict):
            return False
        else:
            assert 'map' in result