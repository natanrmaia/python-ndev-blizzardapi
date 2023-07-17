from blizzardAPI.world_of_warcraft.game_data.playable_race import PlayableRace

class TestPlayableRace:

    def test_get_playable_races_index(self, api_settings : dict):
        """
        This function tests the get_playable_races_index function from the PlayableRace class.

        This function will test the following:
            - If the function returns a dict.
            - If the fic contains the key 'races'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_race = PlayableRace(api_settings['client_id'], api_settings['client_secret'])
        result = playable_race.get_playable_races_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'races' in result

    def test_get_playable_race(self, api_settings : dict):
        """
        This function tests the get_playable_race function from the PlayableRace class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_race = PlayableRace(api_settings['client_id'], api_settings['client_secret'])
        result = playable_race.get_playable_race(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result