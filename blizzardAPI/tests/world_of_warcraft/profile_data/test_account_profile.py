from blizzardAPI.world_of_warcraft.profile_data.account_profile import AccountProfile

class TestAccountProfile:

    def test_get_account_profile_summary(self, api_settings : dict):
        """
        This function tests the get_account_profile_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'wow_accounts'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_profile_summary(api_settings['access_token'])

        args = {
            'region': api_settings['region']
        }

        if not isinstance(result, dict):
            return False
        else:
            assert 'wow_accounts' in result

    def test_get_protected_account_profile_summary(self, api_settings : dict):
        """
        This function tests the get_protected_account_profile_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'wow_accounts'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_protected_account_profile_summary(api_settings['access_token'], api_settings['realm_id'], api_settings['character_id'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'wow_accounts' in result
    

    def test_get_account_collections_index(self, api_settings : dict):
        """
        This function tests the get_account_collections_index function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'mounts'.
            - If the dict contains the key 'pets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_collections_index(api_settings['access_token'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'mounts' in result
            assert 'pets' in result

    def test_get_account_mounts_collection_summary(self, api_settings : dict):
        """
        This function tests the get_account_mounts_collection_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'mounts'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_mounts_collection_summary(api_settings['access_token'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'mounts' in result

    def test_get_account_pets_collection_summary(self, api_settings : dict):
        """
        This function tests the get_account_pets_collection_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'pets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_pets_collection_summary(api_settings['access_token'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'pets' in result

    def test_get_account_toys_collection_summary(self, api_settings : dict):
        """
        This function tests the get_account_toys_collection_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'toys'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_toys_collection_summary(api_settings['access_token'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'toys' in result

    def test_get_account_heirlooms_summary(self, api_settings : dict):
        """
        This function tests the get_account_heirlooms_summary function from the AccountProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'heirlooms'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        account_profile = AccountProfile(api_settings['client_id'], api_settings['client_secret'])
        result = account_profile.get_account_heirlooms_collection_summary(api_settings['access_token'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'heirlooms' in result