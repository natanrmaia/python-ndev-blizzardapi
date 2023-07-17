from blizzardAPI.world_of_warcraft.game_data.covenant import Covenant

class TestCovenant:

    def test_get_covenant_index(self, api_settings : dict):
        """
        This function tests the get_covenant_index function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'covenants'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_covenant_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'covenants' in result

    def test_get_covenant(self, api_settings : dict):
        """
        This function tests the get_covenant function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_covenant(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_covenant_media(self, api_settings : dict):
        """
        This function tests the get_covenant_media function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_covenant_media(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_soulbinds_index(self, api_settings : dict):
        """
        This function tests the get_covenant_soulbinds_index function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'soulbinds'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_soulbind_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'soulbinds' in result

    def test_get_soulbind(self, api_settings : dict):
        """
        This function tests the get_covenant_soulbind function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_soulbind(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_conduit_index(self, api_settings : dict):
        """
        This function tests the get_covenant_conduit_index function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'conduits'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_conduit_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'conduits' in result

    def test_get_conduit(self, api_settings : dict):
        """
        This function tests the get_covenant_conduit function from the Covenant class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        covenant = Covenant(api_settings['client_id'], api_settings['client_secret'])
        result = covenant.get_conduit(50)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result