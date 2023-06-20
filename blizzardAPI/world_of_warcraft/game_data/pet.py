from typing import Dict, Optional
from ...api import API

class Pet(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_pets_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of pets from the API.

        Requested API:
            /data/wow/pet/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pets index.
        """

        api = '/data/wow/pet/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pet(self, region: Optional[str], locale: Optional[str], pet_id: int) -> Dict:
        """
        This function will return the details of a specific pet from the API.

        Requested API:
            /data/wow/pet/{petId}

        Args:
            region: The region of the API you want to access.
            pet_id: The ID of the pet you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pet details.
        """

        api = f'/data/wow/pet/{pet_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pet_media(self, region: Optional[str], locale: Optional[str], pet_id: int) -> Dict:
        """
        This function will return the media of a specific pet from the API.

        Requested API:
            /data/wow/media/pet/{petId}

        Args:
            region: The region of the API you want to access.
            pet_id: The ID of the pet you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pet media.
        """

        api = f'/data/wow/media/pet/{pet_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pet_abilities_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of pet abilities from the API.

        Requested API:
            /data/wow/pet-ability/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pet abilities index.
        """

        api = '/data/wow/pet-ability/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pet_ability(self, region: Optional[str], locale: Optional[str], pet_ability_id: int) -> Dict:
        """
        This function will return the details of a specific pet ability from the API.

        Requested API:
            /data/wow/pet-ability/{petAbilityId}

        Args:
            region: The region of the API you want to access.
            pet_ability_id: The ID of the pet ability you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pet ability details.
        """

        api = f'/data/wow/pet-ability/{pet_ability_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pet_ability_media(self, region: Optional[str], locale: Optional[str], pet_ability_id: int) -> Dict:
        """
        This function will return the media of a specific pet ability from the API.

        Requested API:
            /data/wow/media/pet-ability/{petAbilityId}

        Args:
            region: The region of the API you want to access.
            pet_ability_id: The ID of the pet ability you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the pet ability media.
        """

        api = f'/data/wow/media/pet-ability/{pet_ability_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)