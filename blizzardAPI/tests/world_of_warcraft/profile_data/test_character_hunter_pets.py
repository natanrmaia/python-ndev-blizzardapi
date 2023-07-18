from blizzardAPI.world_of_warcraft.profile_data.character_hunter_pets import CharacterHunterPets

class TestCharacterHunterPets:

    def test_get_character_hunter_pets_summary(self, api_settings : dict):
        """
        This function tests the get_character_hunter_pets_summary function from the CharacterHunterPets class.
        
        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_hunter_pets = CharacterHunterPets(api_settings['client_id'], api_settings['client_secret'])
        result = character_hunter_pets.get_character_hunter_pets_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result