from blizzardAPI.world_of_warcraft.game_data.journal import Journal

class TestJournal:

    def test_get_journal_expansions_index(self, api_settings : dict):
        """
        This function tests the get_journal_expansions_index function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'expansions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_expansions_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'tiers' in result

    def test_get_journal_expansion(self, api_settings : dict):
        """
        This function tests the get_journal_expansion function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_expansion(68)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_journal_encounters_index(self, api_settings : dict):
        """
        This function tests the get_journal_encounters_index function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'encounters'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_encounters_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'encounters' in result

    def test_get_journal_encounter(self, api_settings : dict):
        """
        This function tests the get_journal_encounter function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_encounter(2470)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_journal_encounter_search(self, api_settings : dict):
        """
        This function tests the get_journal_encounter_search function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_encounter_search()

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result

    def test_get_journal_instances_index(self, api_settings : dict):
        """
        This function tests the get_journal_instances_index function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'instances'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_instances_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'instances' in result

    def test_get_journal_instance(self, api_settings : dict):
        """
        This function tests the get_journal_instance function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_instance(249)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_journal_instance_media(self, api_settings : dict):
        """
        This function tests the get_journal_instance_media function from the Journal class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'assets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """
        
        journal = Journal(api_settings['client_id'], api_settings['client_secret'])
        result = journal.get_journal_instance_media(249)

        if not isinstance(result, dict):
            return False
        else:
            assert 'assets' in result