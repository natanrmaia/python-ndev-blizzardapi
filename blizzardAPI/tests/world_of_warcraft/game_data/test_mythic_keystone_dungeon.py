from blizzardAPI.world_of_warcraft.game_data.mythic_keystone_dungeon import MythicKeystoneDungeon

class TestMythicKeystoneDungeon:

    def test_get_mythic_keystone_dungeons_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_dungeons_index function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'dungeons'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_dungeons_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'dungeons' in result

    def test_get_mythic_keystone_dungeon(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_dungeon function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_dungeon(197)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_mythic_keystone_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_index function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'seasons'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'seasons' in result

    def test_get_mythic_keystone_period_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_period_index function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'current_period'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_period_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'periods' in result

    def test_get_mythic_keystone_period(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_period function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_period(641)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_mythic_keystone_seasons_index(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_season_index function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'current_season'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_seasons_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'seasons' in result

    def test_get_mythic_keystone_season(self, api_settings : dict):
        """
        This function tests the get_mythic_keystone_season function from the MythicKeystoneDungeon class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mythic_keystone_dungeon = MythicKeystoneDungeon(api_settings['client_id'], api_settings['client_secret'])
        result = mythic_keystone_dungeon.get_mythic_keystone_season(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result