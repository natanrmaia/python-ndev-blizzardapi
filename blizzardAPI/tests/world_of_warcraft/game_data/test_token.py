from blizzardAPI.world_of_warcraft.game_data.token import Token
import pytest, os

class TestToken:

    def test_get_token_index(self, api_settings):
        """
        This function tests the get_token_index function from the Token class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'price'.

        Returns:
            A boolean value indicating if the test passed.
        """

        print (api_settings)

        token = Token(api_settings['client_id'], api_settings['client_secret'])
        result = token.get_token_index('us')

        if not isinstance(result, dict):
            return False
        else:
            assert 'price' in result