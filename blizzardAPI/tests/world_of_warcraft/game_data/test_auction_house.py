from blizzardAPI.world_of_warcraft.game_data.auction_house import AuctionHouse

class TestAuctionHouse:
    
        def test_get_auctions(self, api_settings : dict):
            """
            This function tests the get_auction_house_index function from the AuctionHouse class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'auctions'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            auction_house = AuctionHouse(api_settings['client_id'], api_settings['client_secret'])
            result = auction_house.get_auctions(region='us', connected_realm_id=121)
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'auctions' in result
    
        def test_get_commodities(self, api_settings : dict):
            """
            This function tests the get_auction_house function from the AuctionHouse class.
    
            This function will test the following:
                - If the function returns a dict.
                - If the dict contains the key 'id'.
    
            Args:
                api_settings (dict): A dictionary containing the api args required for test.
    
            Returns:
                A boolean value indicating if the test passed.
            """
    
            auction_house = AuctionHouse(api_settings['client_id'], api_settings['client_secret'])
            result = auction_house.get_commodities(region='us')
    
            if not isinstance(result, dict):
                return False
            else:
                assert 'auctions' in result