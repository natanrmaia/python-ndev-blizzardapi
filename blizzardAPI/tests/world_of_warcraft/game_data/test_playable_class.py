from blizzardAPI.world_of_warcraft.game_data.playable_class import PlayableClass

class TestPlayableClass:

    def test_get_playable_classes_index(self, api_settings : dict):
        """
        This function tests the get_playable_classes_index function from the PlayableClass class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'classes'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_class = PlayableClass(api_settings['client_id'], api_settings['client_secret'])
        result = playable_class.get_playable_classes_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'classes' in result

    def test_get_playable_class(self, api_settings : dict):
        """
        This function tests the get_playable_class function from the PlayableClass class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_class = PlayableClass(api_settings['client_id'], api_settings['client_secret'])
        result = playable_class.get_playable_class(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_playable_class_media(self, api_settings : dict):
        """
        This function tests the get_playable_class_media function from the PlayableClass class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_class = PlayableClass(api_settings['client_id'], api_settings['client_secret'])
        result = playable_class.get_playable_class_media(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_playable_class_pvp_talent_slots(self, api_settings : dict):
        """
        This function tests the get_playable_class_pvp_talent_slots function from the PlayableClass class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'slots'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        playable_class = PlayableClass(api_settings['client_id'], api_settings['client_secret'])
        result = playable_class.get_pvp_talent_slots(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'talent_slots' in result