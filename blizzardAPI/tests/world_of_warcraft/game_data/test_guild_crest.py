from blizzardAPI.world_of_warcraft.game_data.guild_crest import GuildCrest

class TestGuildCrest:
    
    def test_get_guild_crest_components_index(self, api_settings : dict):
        """
        This function tests the get_guild_crest_components_index function from the GuildCrest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'emblems'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild_crest = GuildCrest(api_settings['client_id'], api_settings['client_secret'])
        result = guild_crest.get_guild_crest_components_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'emblems' in result

    def test_get_guild_crest_border_media(self, api_settings : dict):
        """
        This function tests the get_guild_crest_border_media function from the GuildCrest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild_crest = GuildCrest(api_settings['client_id'], api_settings['client_secret'])
        result = guild_crest.get_guild_crest_border_media(0)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_guild_crest_emblem_media(self, api_settings : dict):
        """
        This function tests the get_guild_crest_emblem_media function from the GuildCrest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild_crest = GuildCrest(api_settings['client_id'], api_settings['client_secret'])
        result = guild_crest.get_guild_crest_emblem_media(0)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result