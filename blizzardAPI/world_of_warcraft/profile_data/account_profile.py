from typing import Optional, Dict, Any
from ...api import API

class AccountProfile(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_account_profile_summary(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account profile summary from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account profile summary.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_protected_account_profile_summary(self, access_token: Any, realm_id: int, character_id: int,**kwargs: Any) -> Dict:
        """
        Returns the protected account profile summary from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_id: The realm id of the character you want to get the profile summary from.
            character_id: The character id of the character you want to get the profile summary from.

        Return:
            The protected account profile summary.

        Raises:
            ValueError: If access_token is not provided.
            ValueError: If realm_id is not provided.
            ValueError: If character_id is not provided.
        """

        api = f'/profile/user/wow/protected-character/{realm_id}-{character_id}'

        if access_token is None:
            raise ValueError('access_token is required')

        if realm_id is None:
            raise ValueError('realm_id is required')

        if character_id is None:
            raise ValueError('character_id is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_account_collections_index(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account collections index from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account collections index.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow/collections'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_account_mounts_collection_summary(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account mounts collection summary from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account mounts collection summary.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow/collections/mounts'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_account_pets_collection_summary(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account pets collection summary from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account pets collection summary.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow/collections/pets'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_account_toys_collection_summary(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account toys collection index from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account toys collection index.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow/collections/toys'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_account_heirlooms_collection_summary(self, access_token: Any, **kwargs: Any) -> Dict:
        """
        Returns the account heirlooms collection index from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.

        Return:
            The account heirlooms collection index.

        Raises:
            ValueError: If access_token is not provided.
        """

        api = '/profile/user/wow/collections/heirlooms'

        if access_token is None:
            raise ValueError('access_token is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
