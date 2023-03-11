from ..api import API

class WorldOfWarcraft_Profile(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_account_profile_summary(self, region, locale, access_token):
        """
        Returns the account profile summary from the API

        :param region: The region of the API endpoint you want to use
        :param locale: The locale of the API endpoint you want to use
        :param access_token: The access token of the API endpoint you want to use
        :return: The account profile summary.
        """

        api = '/profile/user/wow'

        query_params = {
            'namespace': 'profile',
            'locale': locale,
            'access_token': access_token,
        }

        return super().get_api(region, api, query_params)
    
    def get_protected_character_profile_summary(self, region, locale, access_token, realm_id, character_id):
        """
        Returns the protected character profile summary from the API

        :param region: The region of the API endpoint you want to use
        :param locale: The locale of the API endpoint you want to use
        :param access_token: The access token of the API endpoint you want to use
        :param realm_id: The realm id of the character you want to get the profile summary from
        :param character_id: The character id of the character you want to get the profile summary from
        :return: The protected character profile summary.
        """

        api = '/profile/wow/character/{}/{}'

        query_params = {
            'namespace': 'profile',
            'locale': locale,
            'access_token': access_token,
        }

        return super().get_api(region, api.format(realm_id, character_id), query_params)
    
    def get_account_colletions_index(self, region, locale, access_token):
        """
        Returns the account collections index from the API

        :param region: The region of the API endpoint you want to use
        :param locale: The locale of the API endpoint you want to use
        :param access_token: The access token of the API endpoint you want to use
        :return: The account collections index.
        """

        api = '/profile/user/wow/collections'

        query_params = {
            'namespace': 'profile',
            'locale': locale,
            'access_token': access_token,
        }

        return super().get_api(region, api, query_params)
    
    def get_account_mounts_collection_index(self, region, locale, access_token):
        """
        Returns the account mounts collection index from the API

        :param region: The region of the API endpoint you want to use
        :param locale: The locale of the API endpoint you want to use
        :param access_token: The access token of the API endpoint you want to use
        :return: The account mounts collection index.
        """

        api = '/profile/user/wow/collections/mounts'

        query_params = {
            'namespace': 'profile',
            'locale': locale,
            'access_token': access_token,
        }

        return super().get_api(region, api, query_params)
    
    def get_account_pets_colletion_summary(self, region, locale, access_token):
        """
        Returns the account pets collection summary from the API

        :param region: The region of the API endpoint you want to use
        :param locale: The locale of the API endpoint you want to use
        :param access_token: The access token of the API endpoint you want to use
        :return: The account pets collection summary.
        """

        api = '/profile/user/wow/collections/pets'

        query_params = {
            'namespace': 'profile',
            'locale': locale,
            'access_token': access_token,
        }

        return super().get_api(region, api, query_params)

