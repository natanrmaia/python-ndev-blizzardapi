from blizzardAPI.world_of_warcraft.game_data.pvp_season import PvPSeason

class TestPvPSeason:

    def test_get_pvp_seasons_index(self, api_settings : dict):
        """
        This function tests the get_pvp_seasons_index function from the PvPSeason class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'seasons'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_season = PvPSeason(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_season.get_pvp_seasons_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'seasons' in result

    def test_get_pvp_season(self, api_settings : dict):
        """
        This function tests the get_pvp_season function from the PvPSeason class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_season = PvPSeason(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_season.get_pvp_season(27)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_pvp_leaderboards_index(self, api_settings : dict):
        """
        This function tests the get_pvp_leaderboards_index function from the PvPSeason class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'leaderboards'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_season = PvPSeason(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_season.get_pvp_leaderboards_index(33)

        if not isinstance(result, dict):
            return False
        else:
            assert 'leaderboards' in result

    def test_get_pvp_leaderboard(self, api_settings : dict):
        """
        This function tests the get_pvp_leaderboard function from the PvPSeason class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'entries'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_season = PvPSeason(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_season.get_pvp_leaderboard(33, '3v3')

        if not isinstance(result, dict):
            return False
        else:
            assert 'entries' in result

    def test_get_pvp_rewards_index(self, api_settings : dict):
        """
        This function tests the get_pvp_rewards_index function from the PvPSeason class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'rewards'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pvp_season = PvPSeason(api_settings['client_id'], api_settings['client_secret'])
        result = pvp_season.get_pvp_rewards_index(27)

        if not isinstance(result, dict):
            return False
        else:
            assert 'rewards' in result