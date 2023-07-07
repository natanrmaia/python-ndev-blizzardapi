from blizzardAPI.world_of_warcraft.game_data.spell import Spell

class TestSpell:

    def test_get_spell(self, api_settings : dict):
        """
        This function tests the get_spell function from the Spell class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        spell = Spell(api_settings['client_id'], api_settings['client_secret'])
        result = spell.get_spell(196607)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_spell_media(self, api_settings : dict):
        """
        This function tests the get_spell_media function from the Spell class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        spell = Spell(api_settings['client_id'], api_settings['client_secret'])
        result = spell.get_spell_media(196607)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_spell_search(self, api_settings : dict):
        """
        This function tests the get_spell_search function from the Spell class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        spell = Spell(api_settings['client_id'], api_settings['client_secret'])

        args = {
            'name.en_US': 'fire'
        }

        result = spell.get_spell_search(kwargs=args)

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result