from blizzardAPI.world_of_warcraft.game_data.mount import Mount

class TestMount:

    def test_get_mounts_index(self, api_settings : dict):
        """
        This function tests the get_mounts_index function from the Mount class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'mounts'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mount = Mount(api_settings['client_id'], api_settings['client_secret'])
        result = mount.get_mounts_index()

        if not isinstance(result, dict):
            return False
        else:
            assert 'mounts' in result

    def test_get_mount(self, api_settings : dict):
        """
        This function tests the get_mount function from the Mount class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mount = Mount(api_settings['client_id'], api_settings['client_secret'])
        result = mount.get_mount(6)

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_mount_search(self, api_settings : dict):
        """
        This function tests the get_mount_search function from the Mount class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'results'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        mount = Mount(api_settings['client_id'], api_settings['client_secret'])

        arg = {
            'name.en_US': 'Invincible'
        }

        result = mount.get_mount_search(kwargs=arg)

        if not isinstance(result, dict):
            return False
        else:
            assert 'results' in result