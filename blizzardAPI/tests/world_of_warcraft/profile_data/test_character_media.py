from blizzardAPI.world_of_warcraft.profile_data.character_media import CharacterMedia

class TestCharacterMedia:

    def test_get_character_media_summary(self, api_settings : dict):
        """
        This function tests the get_character_media_summary function from the CharacterMedia class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_media = CharacterMedia(api_settings['client_id'], api_settings['client_secret'])
        result = character_media.get_character_media_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result