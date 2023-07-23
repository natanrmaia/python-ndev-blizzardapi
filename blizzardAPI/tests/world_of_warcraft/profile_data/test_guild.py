from blizzardAPI.world_of_warcraft.profile_data.guild import Guild

class TestGuild:

    def test_get_guild(self, api_settings : dict):
        """
        This function tests the get_guild function from the Guild class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'name'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild = Guild(api_settings['client_id'], api_settings['client_secret'])
        result = guild.get_guild(api_settings['realm_slug'], api_settings['guild_slug'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'name' in result

    def test_get_guild_activity(self, api_settings : dict):
        """
        This function tests the get_guild_activity function from the Guild class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'guild'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild = Guild(api_settings['client_id'], api_settings['client_secret'])
        result = guild.get_guild_activity(api_settings['realm_slug'], api_settings['guild_slug'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'guild' in result

    def test_get_guild_achievements(self, api_settings : dict):
        """
        This function tests the get_guild_achievements function from the Guild class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'achievements'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild = Guild(api_settings['client_id'], api_settings['client_secret'])
        result = guild.get_guild_achievements(api_settings['realm_slug'], api_settings['guild_slug'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'achievements' in result

    def test_get_guild_roster(self, api_settings : dict):
        """
        This function tests the get_guild_roster function from the Guild class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'members'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        guild = Guild(api_settings['client_id'], api_settings['client_secret'])
        result = guild.get_guild_roster(api_settings['realm_slug'], api_settings['guild_slug'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'members' in result
