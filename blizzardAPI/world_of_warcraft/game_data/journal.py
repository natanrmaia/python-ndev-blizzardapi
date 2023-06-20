from typing import Optional, Dict
from ...api import API

class Journal(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_journal_expansions_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of expansions from the API.

        Requested API:
            /data/wow/journal-expansion/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the expansion index.
        """

        api = '/data/wow/journal-expansion/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_journal_expansion(self, region: Optional[str], locale: Optional[str], journal_expansion_id: int) -> Dict:
        """
        This function retrieves information about a specific expansion in the World of Warcraft
        game.

        Requested API:
            /data/wow/journal-expansion/{journal_expansion_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            journal_expansion_id: The ID of the expansion.

        Returns:
            A dictionary of the expansion.

        Raises:
            ValueError: If journal_expansion_id is not provided.
        """

        if journal_expansion_id is None:
            raise ValueError('journal_expansion_id is required')

        api = '/data/wow/journal-expansion/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(journal_expansion_id), query_params)
    
    def get_journal_encounters_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of encounters from the API.

        Requested API:
            /data/wow/journal-encounter/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the encounter index.
        """

        api = '/data/wow/journal-encounter/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_journal_encounter(self, region: Optional[str], locale: Optional[str], journal_encounter_id: int) -> Dict:
        """
        This function retrieves information about a specific encounter in the World of Warcraft
        game.

        Requested API:
            /data/wow/journal-encounter/{journal_encounter_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            journal_encounter_id: The ID of the encounter.

        Returns:
            A dictionary of the encounter.

        Raises:
            ValueError: If journal_encounter_id is not provided.
        """

        if journal_encounter_id is None:
            raise ValueError('journal_encounter_id is required')

        api = '/data/wow/journal-encounter/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(journal_encounter_id), query_params)
    

    def get_journal_encounter_search(self, region: Optional[str], locale: Optional[str], instance_name_en: Optional[str], order_by: Optional[str], page: Optional[str]) -> Dict:
        """
        This function will perform a search of encounters from the API.

        Requested API:
            /data/wow/search/journal-encounter

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            search: The string to search for.

        Returns:
            A dictionary of the encounter search.
        """

        api = '/data/wow/search/journal-encounter'


        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        if instance_name_en is not None:
            query_params['instance.name.en_US'] = instance_name_en

        if order_by is not None:
            query_params['orderby'] = order_by

        if page is not None:
            query_params['page'] = page

        return super().get_api(region, api, query_params)
    
    def get_journal_instances_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of instances from the API.

        Requested API:
            /data/wow/journal-instance/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the instance index.
        """

        api = '/data/wow/journal-instance/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_journal_instance(self, region: Optional[str], locale: Optional[str], journal_instance_id: int) -> Dict:
        """
        This function retrieves information about a specific instance from the API.

        Requested API:
            /data/wow/journal-instance/{journal_instance_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            journal_instance_id: The ID of the instance.

        Returns:
            A dictionary of the instance.

        Raises:
            ValueError: If journal_instance_id is not provided.
        """

        if journal_instance_id is None:
            raise ValueError('journal_instance_id is required')

        api = '/data/wow/journal-instance/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(journal_instance_id), query_params)
    
    def get_journal_instance_media(self, region: Optional[str], locale: Optional[str], journal_instance_id: int) -> Dict:
        """
        This function retrieves media for a specific instance from API.

        Requested API:
            /data/wow/media/journal-instance/{journal_instance_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            journal_instance_id: The ID of the instance.

        Returns:
            A dictionary of the instance media.

        Raises:
            ValueError: If journal_instance_id is not provided.
        """

        if journal_instance_id is None:
            raise ValueError('journal_instance_id is required')

        api = '/data/wow/media/journal-instance/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(journal_instance_id), query_params)
