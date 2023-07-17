from blizzardAPI.world_of_warcraft.game_data.talent import Talent

class TestTalent:

    def test_get_talent_tree_index(self, api_settings : dict):
        """
        This function tests the get_talent_tree_index function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talent_trees'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_talent_tree_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'spec_talent_trees' in result

    def test_get_talent_tree(self, api_settings : dict):
        """
        This function tests the get_talent_tree function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talent_tree_id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_talent_tree(786, 262)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_talent_tree_nodes(self, api_settings : dict):
        """
        This function tests the get_talen_tree_nodes function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talent_nodes'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_talent_tree_nodes(786)

        if not isinstance(result, dict):
            return False
        else:
            assert 'talent_nodes' in result

    def test_get_talents_index(self, api_settings : dict):
        """
        This function tests the get_talents_index function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talents'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_talents_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'talents' in result

    def test_get_talent(self, api_settings : dict):
        """
        This function tests the get_talent function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'talent_id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_talent(117163)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_pvp_talents_index(self, api_settings : dict):
        """
        This function tests the get_pvp_talents_index function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'pvp_talents'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_pvp_talents_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'pvp_talents' in result

    def test_get_pvp_talent(self, api_settings : dict):
        """
        This function tests the get_pvp_talent function from the Talent class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        talent = Talent(api_settings['client_id'], api_settings['client_secret'])
        result = talent.get_pvp_talent(40)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result
