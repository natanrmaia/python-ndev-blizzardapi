from blizzardAPI.world_of_warcraft.game_data.tech_talent import TechTalent

class TestTechTalent:

    def test_get_tech_talent_tree_index(self, api_settings : dict):
        """
        This function tests the get_tech_talent_tree_index function from the TechTalent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talent_trees'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        tech_talent = TechTalent(api_settings['client_id'], api_settings['client_secret'])
        result = tech_talent.get_tech_talent_tree_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'talent_trees' in result

    def test_get_tech_talent_tree(self, api_settings : dict):
        """
        This function tests the get_tech_talent_tree function from the TechTalent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talents'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        tech_talent = TechTalent(api_settings['client_id'], api_settings['client_secret'])
        result = tech_talent.get_tech_talent_tree(275)

        if not isinstance(result, dict):
            return False
        else:
            assert 'talents' in result

    def test_get_tech_talent(self, api_settings : dict):
        """
        This function tests the get_tech_talent function from the TechTalent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'spell_tooltip'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        tech_talent = TechTalent(api_settings['client_id'], api_settings['client_secret'])
        result = tech_talent.get_tech_talent(863)

        if not isinstance(result, dict):
            return False
        else:
            assert 'spell_tooltip' in result

    def test_get_tech_talent_index(self, api_settings : dict):
        """
        This function tests the get_tech_talent_index function from the TechTalent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talents'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        tech_talent = TechTalent(api_settings['client_id'], api_settings['client_secret'])
        result = tech_talent.get_tech_talent_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'talents' in result

    def test_get_tech_talent_media(self, api_settings : dict):
        """
        This function tests the get_tech_talent_media function from the TechTalent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        tech_talent = TechTalent(api_settings['client_id'], api_settings['client_secret'])
        result = tech_talent.get_tech_talent_media(863)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result