from typing import Dict, Optional, Any
from ...api import API

class Profession(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_professions_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of professions from the API.

        Requested API:
            /data/wow/profession/index

        Returns:
            A dictionary of the professions index.
        """

        api = '/data/wow/profession/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_profession(self, profession_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific profession from the API.

        Requested API:
            /data/wow/profession/{professionId}

        Args:
            profession_id: The ID of the profession you want to retrieve.

        Returns:
            A dictionary of the profession details.

        Raises:
            ValueError: If the profession ID is not valid.
        """

        if profession_id is None:
            raise ValueError('Profession ID cannot be None.')

        api = f'/data/wow/profession/{profession_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_profession_media(self, profession_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific profession from the API.

        Requested API:
            /data/wow/media/profession/{professionId}

        Args:
            profession_id: The ID of the profession you want to retrieve.

        Returns:
            A dictionary of the profession media.

        Raises:
            ValueError: If the profession ID is not valid.
        """

        if profession_id is None:
            raise ValueError('Profession ID cannot be None.')

        api = f'/data/wow/media/profession/{profession_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_profession_skill_tier(self, profession_id: int, skill_tier_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific profession skill tier from the API.

        Requested API:
            /data/wow/profession/{professionId}/skill-tier/{skillTierId}

        Args:
            profession_id: The ID of the profession you want to retrieve.
            skill_tier_id: The ID of the skill tier you want to retrieve.

        Returns:
            A dictionary of the profession skill tier details.

        Raises:
            ValueError: If the profession ID is not valid.
            ValueError: If the skill tier ID is not valid.
        """

        if profession_id is None:
            raise ValueError('Profession ID cannot be None.')

        if skill_tier_id is None:
            raise ValueError('Skill tier ID cannot be None.')


        api = f'/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_recipe(self, recipe_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific recipe from the API.

        Requested API:
            /data/wow/recipe/{recipeId}

        Args:
            region: The region of the API you want to access.
            recipe_id: The ID of the recipe you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the recipe details.

        Raises:
            ValueError: If the recipe ID is not valid.
        """

        if recipe_id is None:
            raise ValueError('Recipe ID cannot be None.')

        api = f'/data/wow/recipe/{recipe_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_recipe_media(self, recipe_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific recipe from the API.

        Requested API:
            /data/wow/media/recipe/{recipeId}

        Args:
            recipe_id: The ID of the recipe you want to retrieve.

        Returns:
            A dictionary of the recipe media.

        Raises:
            ValueError: If the recipe ID is not valid.
        """

        if recipe_id is None:
            raise ValueError('Recipe ID cannot be None.')

        api = f'/data/wow/media/recipe/{recipe_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)