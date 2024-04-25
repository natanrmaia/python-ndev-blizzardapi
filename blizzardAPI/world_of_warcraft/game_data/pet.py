from typing import Dict, Optional, Any
from ...api import API

class Pet(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_pets_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of pets from the API.

        Requested API:
            /data/wow/pet/index

        Returns:
            A dictionary of the pets index.
        """

        api = '/data/wow/pet/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pet(self, pet_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific pet from the API.

        Requested API:
            /data/wow/pet/{petId}

        Args:
            pet_id: The ID of the pet you want to retrieve.

        Returns:
            A dictionary of the pet details.
        """

        api = f'/data/wow/pet/{pet_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pet_media(self, pet_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific pet from the API.

        Requested API:
            /data/wow/media/pet/{petId}

        Args:
            pet_id: The ID of the pet you want to retrieve.

        Returns:
            A dictionary of the pet media.
        """

        api = f'/data/wow/media/pet/{pet_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pet_abilities_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of pet abilities from the API.

        Requested API:
            /data/wow/pet-ability/index

        Returns:
            A dictionary of the pet abilities index.
        """

        api = '/data/wow/pet-ability/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pet_ability(self, pet_ability_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific pet ability from the API.

        Requested API:
            /data/wow/pet-ability/{petAbilityId}

        Args:
            pet_ability_id: The ID of the pet ability you want to retrieve.

        Returns:
            A dictionary of the pet ability details.
        """

        api = f'/data/wow/pet-ability/{pet_ability_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pet_ability_media(self, pet_ability_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific pet ability from the API.

        Requested API:
            /data/wow/media/pet-ability/{petAbilityId}

        Args:
            pet_ability_id: The ID of the pet ability you want to retrieve.

        Returns:
            A dictionary of the pet ability media.
        """

        api = f'/data/wow/media/pet-ability/{pet_ability_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)