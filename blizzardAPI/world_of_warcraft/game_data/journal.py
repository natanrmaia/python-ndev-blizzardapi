from typing import Optional, Dict, Any
from ...api import API

class Journal(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_journal_expansions_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of expansions from the API.

        Requested API:
            /data/wow/journal-expansion/index

        Returns:
            A dictionary of the expansion index.
        """

        api = '/data/wow/journal-expansion/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_expansion(self, journal_expansion_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific expansion in the World of Warcraft
        game.

        Requested API:
            /data/wow/journal-expansion/{journal_expansion_id}

        Args:
            journal_expansion_id: The ID of the expansion.

        Returns:
            A dictionary of the expansion.

        Raises:
            ValueError: If journal_expansion_id is not provided.
        """

        if journal_expansion_id is None:
            raise ValueError('journal_expansion_id is required')

        api = f'/data/wow/journal-expansion/{journal_expansion_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_encounters_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of encounters from the API.

        Requested API:
            /data/wow/journal-encounter/index

        Returns:
            A dictionary of the encounter index.
        """

        api = '/data/wow/journal-encounter/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_encounter(self, journal_encounter_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific encounter in the World of Warcraft
        game.

        Requested API:
            /data/wow/journal-encounter/{journal_encounter_id}

        Args:
            journal_encounter_id: The ID of the encounter.

        Returns:
            A dictionary of the encounter.

        Raises:
            ValueError: If journal_encounter_id is not provided.
        """

        if journal_encounter_id is None:
            raise ValueError('journal_encounter_id is required')

        api = f'/data/wow/journal-encounter/{journal_encounter_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_encounter_search(self, **kwargs: Any) -> Dict:
        """
        This function will perform a search of encounters from the API.

        Requested API:
            /data/wow/search/journal-encounter

        Returns:
            A dictionary of the encounter search.
        """

        api = '/data/wow/search/journal-encounter'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_instances_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of instances from the API.

        Requested API:
            /data/wow/journal-instance/index

        Returns:
            A dictionary of the instance index.
        """

        api = '/data/wow/journal-instance/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_instance(self, journal_instance_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific instance from the API.

        Requested API:
            /data/wow/journal-instance/{journal_instance_id}

        Args:
            journal_instance_id: The ID of the instance.

        Returns:
            A dictionary of the instance.

        Raises:
            ValueError: If journal_instance_id is not provided.
        """

        if journal_instance_id is None:
            raise ValueError('journal_instance_id is required')

        api = f'/data/wow/journal-instance/{journal_instance_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_journal_instance_media(self, journal_instance_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves media for a specific instance from API.

        Requested API:
            /data/wow/media/journal-instance/{journal_instance_id}

        Args:
            journal_instance_id: The ID of the instance.

        Returns:
            A dictionary of the instance media.

        Raises:
            ValueError: If journal_instance_id is not provided.
        """

        if journal_instance_id is None:
            raise ValueError('journal_instance_id is required')

        api = f'/data/wow/media/journal-instance/{journal_instance_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
