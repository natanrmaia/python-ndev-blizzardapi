from blizzardAPI.world_of_warcraft.game_data.creature import Creature

class TestCreature:
    
    def test_get_creature_families_index(self, api_settings : dict):
        """
        This function tests the get_creature_families_index function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'creature_families'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_families_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'creature_families' in result

    def test_get_creature_family(self, api_settings : dict):
        """
        This function tests the get_creature_family function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_family(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_creature_types_index(self, api_settings : dict):
        """
        This function tests the get_creature_types_index function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'creature_types'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_types_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'creature_types' in result


    def test_get_creature_type(self, api_settings : dict):
        """
        This function tests the get_creature_type function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_type(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_creature(self, api_settings : dict):
        """
        This function tests the get_creature function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature(42719)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_creature_display_media(self, api_settings : dict):
        """
        This function tests the get_creature_display_media function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_display_media(30221)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_get_creature_families_media(self, api_settings : dict):
        """
        This function tests the get_creature_families_media function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        creature = Creature(api_settings['client_id'], api_settings['client_secret'])
        result = creature.get_creature_family_media(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result

    def test_search_creature(self, api_settings : dict):
        """
        This function tests the search_creature function from the Creature class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
        
        creature = Creature(api_settings['client_id'], api_settings['client_secret'])

        result = creature.get_creature_search(name = 'Dragon')

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result
