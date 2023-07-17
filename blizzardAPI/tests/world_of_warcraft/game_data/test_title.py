from blizzardAPI.world_of_warcraft.game_data.title import Title

class TestTitle:

    def test_get_titles_index(self, api_settings : dict):
        """
        This function tests the get_titles_index function from the Title class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'titles'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        title = Title(api_settings['client_id'], api_settings['client_secret'])
        result = title.get_titles_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'titles' in result

    def test_get_title(self, api_settings : dict):
        """
        This function tests the get_title function from the Title class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        title = Title(api_settings['client_id'], api_settings['client_secret'])
        result = title.get_title(4)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result
