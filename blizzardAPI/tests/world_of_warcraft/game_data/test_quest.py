from blizzardAPI.world_of_warcraft.game_data.quest import Quest

class TestQuest:

    def test_get_quests_index(self, api_settings : dict):
        """
        This function tests the get_quests_index function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'quests'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quests_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result

    def test_get_quest(self, api_settings : dict):
        """
        This function tests the get_quest function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest(2)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_quest_categories_index(self, api_settings : dict):
        """
        This function tests the get_quest_categories_index function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'categories'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_categories_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result

    def test_get_quest_category(self, api_settings : dict):
        """
        This function tests the get_quest_category function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_category(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_quest_areas_index(self, api_settings : dict):
        """
        This function tests the get_quest_areas_index function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'areas'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_areas_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'areas' in result

    def test_get_quest_area(self, api_settings : dict):
        """
        This function tests the get_quest_area function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_area(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_quest_types_index(self, api_settings : dict):
        """
        This function tests the get_quest_types_index function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'types'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_types_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'types' in result

    def test_get_quest_type(self, api_settings : dict):
        """
        This function tests the get_quest_type function from the Quest class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        quest = Quest(api_settings['client_id'], api_settings['client_secret'])
        result = quest.get_quest_type(1)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result