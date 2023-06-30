from blizzardAPI.world_of_warcraft.game_data.playable_specialization import PlayableSpecialization

class TestPlayableSpecialization:

    def test_get_playable_specializations_index(self, api_settings : dict):
        """
        This function tests the get_playable_specializations_index function from the PlayableSpecialization class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'specializations'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_specialization = PlayableSpecialization(api_settings['client_id'], api_settings['client_secret'])
        result = playable_specialization.get_playable_specializations_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'character_specializations' in result

    def test_get_playable_specialization(self, api_settings : dict):
        """
        This function tests the get_playable_specialization function from the PlayableSpecialization class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_specialization = PlayableSpecialization(api_settings['client_id'], api_settings['client_secret'])
        result = playable_specialization.get_playable_specialization(262)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_playable_specialization_media(self, api_settings : dict):
        """
        This function tests the get_playable_specialization_media function from the PlayableSpecialization class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_specialization = PlayableSpecialization(api_settings['client_id'], api_settings['client_secret'])
        result = playable_specialization.get_playable_specialization_media(262)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result