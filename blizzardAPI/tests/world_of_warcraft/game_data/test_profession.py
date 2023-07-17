from blizzardAPI.world_of_warcraft.game_data.profession import Profession

class TestProfession:

    def test_get_professions_index(self, api_settings : dict):
        """
        This function tests the get_professions_index function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'professions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_professions_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'professions' in result

    def test_get_profession(self, api_settings : dict):
        """
        This function tests the get_profession function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_profession(164)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_profession_media(self, api_settings : dict):
        """
        This function tests the get_profession_media function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_profession_media(164)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_profession_skill_tier(self, api_settings : dict):
        """
        This function tests the get_profession_skill_tier function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
        
        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_profession_skill_tier(164, 2477)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_recipe(self, api_settings : dict):
        """
        This function tests the get_recipe function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
        
        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_recipe(1631)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_recipe_media(self, api_settings : dict):
        """
        This function tests the get_recipe_media function from the Profession class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
                
        profession = Profession(api_settings['client_id'], api_settings['client_secret'])
        result = profession.get_recipe_media(1631)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result