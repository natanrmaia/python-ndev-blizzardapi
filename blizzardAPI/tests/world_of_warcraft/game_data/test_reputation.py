from blizzardAPI.world_of_warcraft.game_data.reputation import Reputation

class TestReputation:

    def test_get_reputation_factions_index(self, api_settings : dict):
        """
        This function tests the get_reputation_factions_index function from the Reputation class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'factions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        reputation = Reputation(api_settings['client_id'], api_settings['client_secret'])
        result = reputation.get_reputation_factions_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'factions' in result

    def test_get_reputation_faction(self, api_settings : dict):
        """
        This function tests the get_reputation_faction function from the Reputation class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        reputation = Reputation(api_settings['client_id'], api_settings['client_secret'])
        result = reputation.get_reputation_faction(21)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_reputation_tiers_index(self, api_settings : dict):
        """
        This function tests the get_reputation_tiers_index function from the Reputation class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'reputation_tiers'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        reputation = Reputation(api_settings['client_id'], api_settings['client_secret'])
        result = reputation.get_reputation_tiers_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'reputation_tiers' in result

    def test_get_reputation_tiers(self, api_settings : dict):
        """
        This function tests the get_reputation_tiers function from the Reputation class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        reputation = Reputation(api_settings['client_id'], api_settings['client_secret'])
        result = reputation.get_reputation_tiers(2)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

