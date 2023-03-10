from ..api import API

class BattleNetAPI_OAuth(API):
    """
    This class is used to make requests to the Battle.net API.

    Attributes:
        :param client_id: The client ID you received from Blizzard
        :param client_secret: The client secret you received from Blizzard
    """

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_user_info(self, region, access_token):
        """
        It takes the region and access token as parameters, and returns the user info from the API
        
        :param region: The region of the API endpoint you want to use
        :param access_token: The access token returned by the authorization server
        :return: The user's information.
        """
        api = '/oauth/userinfo'
        query_params = {
            'access_token': access_token,
        }
        return super().get_oauth(api, region, query_params)
    
    def get_token_validation(self, region, access_token):
        """
        It takes the region and access token as parameters, and returns the token validation from the API
        
        :param region: The region of the API endpoint you want to use
        :param access_token: The access token returned by the authorization server
        :return: The token validation.
        """
        api = '/oauth/check_token'
        query_params = {
            'token': access_token,
        }
        return super().get_oauth(api, region, query_params)