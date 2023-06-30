from blizzardAPI.world_of_warcraft.game_data.pet import Pet

class TestPet:

    def test_get_pets_index(self, api_settings : dict):
        """
        This function tests the get_pets_index function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'pets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pets_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'pets' in result

    def test_get_pet(self, api_settings : dict):
        """
        This function tests the get_pet function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pet(39)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_pet_media(self, api_settings : dict):
        """
        This function tests the get_pet_media function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pet_media(39)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_pets_abilities_index(self, api_settings : dict):
        """
        This function tests the get_pets_abilities_index function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'abilities'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pet_abilities_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'abilities' in result

    def test_get_pet_ability(self, api_settings : dict):
        """
        This function tests the get_pet_ability function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pet_ability(640)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_pet_ability_media(self, api_settings : dict):
        """
        This function tests the get_pet_ability_media function from the Pet class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        pet = Pet(api_settings['client_id'], api_settings['client_secret'])
        result = pet.get_pet_ability_media(640)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result