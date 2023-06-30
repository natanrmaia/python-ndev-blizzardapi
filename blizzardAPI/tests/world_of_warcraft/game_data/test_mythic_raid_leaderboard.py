from blizzardAPI.world_of_warcraft.game_data.mythic_raid_leaderboard import MythicRaidLeaderboard

class TestMythicRaidLeaderboard:

    def test_get_mythic_raid_leaderboard(self, api_settings : dict):
        """
        This function tests the get_mythic_raid_leaderboard function from the MythicRaidLeaderboard class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_raid_leaderboard = MythicRaidLeaderboard(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_raid_leaderboard.get_mythic_raid_leaderboard('uldir', 'alliance')

        if not isinstance(result, dict):
            return False
        else:
            assert 'slug' in result