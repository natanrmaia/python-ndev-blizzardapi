from .achievement                   import Achievement
from .auction_house                 import AuctionHouse
from .azerite_essence               import AzeriteEssence
from .connected_realm               import ConnectedRealm
from .covenant                      import Covenant
from .creature                      import Creature
from .guild_crest                   import GuildCrest
from .heirloom                      import Heirloom
from .item                          import Item
from .journal                       import Journal
from .media                         import Media
from .modified_crafting             import ModifiedCrafting
from .mount                         import Mount
# from .mythic_keystone_affix         import MythicKeystoneAffix
# from .mythic_keystone_dungeon       import MythicKeystoneDungeon
# from .mythic_keystone_leaderboard   import MythicKeystoneLeaderboard
# from .mythic_raid_leaderboard       import MythicRaidLeaderboard
# from .pet                           import Pet
# from .playable_class                import PlayableClass
# from .playable_race                 import PlayableRace
# from .playable_specialization       import PlayableSpecialization
# from .power_type                    import PowerType
# from .profession                    import Profession
# from .pvp_season                    import PvPSeason
# from .pvp_tier                      import PvPTier
# from .quest                         import Quest
# from .realm                         import Realm
# from .region                        import Region
# from .reputation                    import Reputation
# from .spell                         import Spell
# from .talent                        import Talent
# from .tech_talent                   import TechTalent
# from .title                         import Title
from .token                         import Token
from .toy                           import Toy

class Game:

    def __init__(self, client_id, client_secret):
        self.achievement                      = Achievement(client_id, client_secret)
        self.auction_house                    = AuctionHouse(client_id, client_secret)
        self.azerite_essence                  = AzeriteEssence(client_id, client_secret)
        self.connected_realm                  = ConnectedRealm(client_id, client_secret)
        self.covenant                         = Covenant(client_id, client_secret)
        self.creature                         = Creature(client_id, client_secret)
        self.guild_crest                      = GuildCrest(client_id, client_secret)
        self.heirloom                         = Heirloom(client_id, client_secret)
        self.item                             = Item(client_id, client_secret)
        self.journal                          = Journal(client_id, client_secret)
        self.media                            = Media(client_id, client_secret)
        self.modified_crafting                = ModifiedCrafting(client_id, client_secret)
        self.mount                            = Mount(client_id, client_secret)
        # self.mythic_keystone_Affix            = MythicKeystoneAffix(client_id, client_secret)
        # self.mythic_keystone_dungeon          = MythicKeystoneDungeon(client_id, client_secret)
        # self.mythic_keystone_leaderboard      = MythicKeystoneLeaderboard(client_id, client_secret)
        # self.mythic_raid_leaderboard          = MythicRaidLeaderboard(client_id, client_secret)
        # self.pet                              = Pet(client_id, client_secret)
        # self.playable_class                   = PlayableClass(client_id, client_secret)
        # self.playable_race                    = PlayableRace(client_id, client_secret)
        # self.playable_specialization          = PlayableSpecialization(client_id, client_secret)
        # self.power_type                       = PowerType(client_id, client_secret)
        # self.profession                       = Profession(client_id, client_secret)
        # self.pvp_season                       = PvPSeason(client_id, client_secret)
        # self.pvp_tier                         = PvPTier(client_id, client_secret)
        # self.quest                            = Quest(client_id, client_secret)
        # self.realm                            = Realm(client_id, client_secret)
        # self.region                           = Region(client_id, client_secret)
        # self.reputation                       = Reputation(client_id, client_secret)
        # self.spell                            = Spell(client_id, client_secret)
        # self.talent                           = Talent(client_id, client_secret)
        # self.tech_talent                      = TechTalent(client_id, client_secret)
        # self.title                            = Title(client_id, client_secret)
        self.wow_token                        = Token(client_id, client_secret)
        self.toy                              = Toy(client_id, client_secret)