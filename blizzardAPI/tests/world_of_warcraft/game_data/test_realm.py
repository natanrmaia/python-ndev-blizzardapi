from blizzardAPI.world_of_warcraft.game_data.realm import Realm

class TestRealm:

    def test_get_realms_index(self, api_settings : dict):
        """
        This function tests the get_realms_index function from the Realm class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'realms'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        realm = Realm(api_settings['client_id'], api_settings['client_secret'])
        result = realm.get_realms_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'realms' in result

    def test_get_realm(self, api_settings : dict):
        """
        This function tests the get_realm function from the Realm class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        realm = Realm(api_settings['client_id'], api_settings['client_secret'])
        result = realm.get_realm('tichondrius')

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_realm_search(self, api_settings : dict):
        """
        This function tests the get_realm_search function from the Realm class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        realm = Realm(api_settings['client_id'], api_settings['client_secret'])
        result = realm.get_realm_search('tichondrius')

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result