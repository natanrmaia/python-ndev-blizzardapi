from typing import Optional, Dict, Any
from ...api import API

class Creature(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_creature_families_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of creature families from the API.

        Requested API:
            /data/wow/creature-family/index

        Returns:
            A dictionary of the creature family index.
        """

        api = '/data/wow/creature-family/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_family(self, creature_family_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific creature family in the World of Warcraft
        game.

        Requested API:
            /data/wow/creature-family/{creature_family_id}

        Args:
            creature_family_id: The ID of the creature family.

        Returns:
            A dictionary of the creature family.

        Raises:
            ValueError: If creature_family_id is not provided.
        """

        if creature_family_id is None:
            raise ValueError('creature_family_id is required')

        api = f'/data/wow/creature-family/{creature_family_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_types_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of creature types from the API.

        Requested API:
            /data/wow/creature-type/index

        Returns:
            A dictionary of the creature type index.
        """

        api = '/data/wow/creature-type/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_type(self, creature_type_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific creature type in the World of Warcraft
        game.

        Requested API:
            /data/wow/creature-type/{creature_type_id}

        Args:
            creature_type_id: The ID of the creature type.

        Returns:
            A dictionary of the creature type.

        Raises:
            ValueError: If creature_type_id is not provided.
        """

        if creature_type_id is None:
            raise ValueError('creature_type_id is required')

        api = f'/data/wow/creature-type/{creature_type_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature(self, creature_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific creature in the World of Warcraft game.

        Requested API:
            /data/wow/creature/{creature_id}

        Args:
            creature_id: The ID of the creature.

        Returns:
            A dictionary of the creature.

        Raises:
            ValueError: If creature_id is not provided.
        """

        if creature_id is None:
            raise ValueError('creature_id is required')

        api = f'/data/wow/creature/{creature_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_search(self, **kwargs: Any) -> Dict:
        """
        This function searches for creatures with the given search parameters.

        Requested API:
            /data/wow/search/creature

        Returns:
            A dictionary of the creature search results.
        """

        api = '/data/wow/search/creature'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_display_media(self, creature_display_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves the media for a specific creature display.

        Requested API:
            /data/wow/media/creature-display/{creature_display_id}

        Args:
            creature_display_id: The ID of the creature display media.

        Returns:
            A dictionary of the creature display media.

        Raises:
            ValueError: If creature_display_id is not provided.
        """

        if creature_display_id is None:
            raise ValueError('creature_display_id is required')

        api = f'/data/wow/media/creature-display/{creature_display_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_creature_family_media(self, creature_family_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves the media for a specific creature family.

        Requested API:
            /data/wow/media/creature-family/{creature_family_id}

        Args:
            creature_family_id: The ID of the creature family media.

        Returns:
            A dictionary of the creature family media.

        Raises:
            ValueError: If creature_family_id is not provided.
        """

        if creature_family_id is None:
            raise ValueError('creature_family_id is required')

        api = f'/data/wow/media/creature-family/{creature_family_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)