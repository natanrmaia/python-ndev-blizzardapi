from blizzardAPI.world_of_warcraft.game_data.achievement import Achievement

class TestAchievement:

    def test_get_achievement_categories_index(self, api_settings : dict):
        """
        This function tests the get_achievement_categories_index function from the Achievement class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'categories'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        achievement = Achievement(api_settings['client_id'], api_settings['client_secret'])
        result = achievement.get_achievement_categories_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result

    def test_get_achievement_category(self, api_settings : dict):
        """
        This function tests the get_achievement_category function from the Achievement class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        achievement = Achievement(api_settings['client_id'], api_settings['client_secret'])
        result = achievement.get_achievement_category(92)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_achievements_index(self, api_settings : dict):
        """
        This function tests the get_achievements_index function from the Achievement class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'achievements'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        achievement = Achievement(api_settings['client_id'], api_settings['client_secret'])
        result = achievement.get_achievement_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'achievements' in result

    def test_get_achievement(self, api_settings : dict):
        """
        This function tests the get_achievement function from the Achievement class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        achievement = Achievement(api_settings['client_id'], api_settings['client_secret'])
        result = achievement.get_achievement(2144)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_achievement_media(self, api_settings : dict):
        """
        This function tests the get_achievement_media function from the Achievement class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        achievement = Achievement(api_settings['client_id'], api_settings['client_secret'])
        result = achievement.get_achievement_media(2144)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result