from blizzardAPI.world_of_warcraft.game_data.connected_realm import ConnectedRealm

class TestConnectedRealm:
    
        def test_get_connected_realms_index(self, api_settings : dict):
            """
            This function tests the get_connected_realms_index function from the ConnectedRealm class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'connected_realms'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            connected_realm = ConnectedRealm(api_settings['client_id'], api_settings['client_secret'])
            result = connected_realm.get_connected_realms_index()
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'connected_realms' in result
    
        def test_get_connected_realm(self, api_settings : dict):
            """
            This function tests the get_connected_realm function from the ConnectedRealm class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'id'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            connected_realm = ConnectedRealm(api_settings['client_id'], api_settings['client_secret'])
            result = connected_realm.get_connected_realms_index()
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'id' in result
    
        def test_get_connected_realm(self, api_settings : dict):
            """
            This function tests the get_connected_realm_search function from the ConnectedRealm class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'results'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            connected_realm = ConnectedRealm(api_settings['client_id'], api_settings['client_secret'])
            result = connected_realm.get_connected_realm(11)
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'id' in result

        def test_get_connected_realm_search(self, api_settings : dict):
            """
            This function tests the get_connected_realm_search function from the ConnectedRealm class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'results'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            connected_realm = ConnectedRealm(api_settings['client_id'], api_settings['client_secret'])
            result = connected_realm.get_connected_realm_search()
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'results' in result