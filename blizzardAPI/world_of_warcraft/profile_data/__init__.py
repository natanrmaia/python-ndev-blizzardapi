from .account_profile                   import AccountProfile
from .character_achievements            import CharacterAchievements
from .character_appearance              import CharacterAppearance
from .character_collections             import CharacterCollections
from .character_encounters              import CharacterEncounters
from .character_equipment               import CharacterEquipment
from .character_hunter_pets             import CharacterHunterPets
from .character_media                   import CharacterMedia
from .character_mythic_keystone_profile import CharacterMythicKeystoneProfile
from .character_professions             import CharacterProfessions
from .character_profile                 import CharacterProfile
from .character_pvp                     import CharacterPvP
from .character_quests                  import CharacterQuests
from .character_reputations             import CharacterReputations
from .character_soulbinds               import CharacterSoulbinds
from .character_specializations         import CharacterSpecializations
from .character_statistics              import CharacterStatistics
from .character_titles                  import CharacterTitles
from .guild                             import Guild

class Profile:

    def __init__(self, client_id, client_secret):

        self.account_profile                      = AccountProfile(client_id, client_secret)
        self.character_achievements               = CharacterAchievements(client_id, client_secret)
        self.character_appearance                 = CharacterAppearance(client_id, client_secret)
        self.character_collections                = CharacterCollections(client_id, client_secret)
        self.character_encounters                 = CharacterEncounters(client_id, client_secret)
        self.character_equipment                  = CharacterEquipment(client_id, client_secret)
        self.character_hunter_pets                = CharacterHunterPets(client_id, client_secret)
        self.character_media                      = CharacterMedia(client_id, client_secret)
        self.character_mythic_keystone_profile    = CharacterMythicKeystoneProfile(client_id, client_secret)
        self.character_professions                = CharacterProfessions(client_id, client_secret)
        self.character_profile                    = CharacterProfile(client_id, client_secret)
        self.character_pvp                        = CharacterPvP(client_id, client_secret)
        self.character_quests                     = CharacterQuests(client_id, client_secret)
        self.character_reputations                = CharacterReputations(client_id, client_secret)
        self.character_soulbinds                  = CharacterSoulbinds(client_id, client_secret)
        self.character_specializations            = CharacterSpecializations(client_id, client_secret)
        self.character_statistics                 = CharacterStatistics(client_id, client_secret)
        self.character_titles                     = CharacterTitles(client_id, client_secret)
        self.guild                                = Guild(client_id, client_secret)
