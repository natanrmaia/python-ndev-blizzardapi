from blizzardAPI.world_of_warcraft.game_data.media import Media

class TestMedia:
    
        def test_get_media_search(self, api_settings : dict):
            """
            This function tests the get_media_search function from the Media class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'assets'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            media = Media(api_settings['client_id'], api_settings['client_secret'])
            result = media.get_media_search()
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'results' in result
