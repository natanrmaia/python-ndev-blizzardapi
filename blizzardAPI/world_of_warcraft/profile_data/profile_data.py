from ...api import API

from .account_profile import AccountProfile

class Profile(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

        self.account_profile                        = AccountProfile(client_id, client_secret)
        # self.character_achievements               = CharacterAchievements(client_id, client_secret)
        # self.character_appearance                 = CharacterAppearance(client_id, client_secret)
        # self.character_collections                = CharacterCollections(client_id, client_secret)
        # self.character_encounters                 = CharacterEncounters(client_id, client_secret)
        # self.character_equipment                  = CharacterEquipment(client_id, client_secret)
        # self.character_hunter_pets                = CharacterHunterPets(client_id, client_secret)
        # self.character_media                      = CharacterMedia(client_id, client_secret)
        # self.character_mythic_keystone_profile    = CharacterMythicKeystoneProfile(client_id, client_secret)
        # self.character_professions                = CharacterProfessions(client_id, client_secret)
        # self.character_profile                    = CharacterProfile(client_id, client_secret)
        # self.character_pvp                        = CharacterPvP(client_id, client_secret)
        # self.character_quests                     = CharacterQuests(client_id, client_secret)
        # self.character_reputations                = CharacterReputations(client_id, client_secret)
        # self.character_soulbinds                  = CharacterSoulbinds(client_id, client_secret)
        # self.character_specializations            = CharacterSpecializations(client_id, client_secret)
        # self.character_statistics                 = CharacterStatistics(client_id, client_secret)
        # self.character_titles                     = CharacterTitles(client_id, client_secret)
        # self.guild                                = Guild(client_id, client_secret)
