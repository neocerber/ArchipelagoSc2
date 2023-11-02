from worlds.AutoWorld import World
from BaseClasses import ItemClassification, Region, Item, Location, Type
from worlds.generic.Rules import set_rule, add_item_rule
from typing import Any, Dict, List, Optional, TextIO, Union
from Options import Option
from Fill import swap_location_item

from .Items import ItemData, items
from .Locations import LocationData, locations
from .Rules import get_rules
from .Options import *

from .EntranceRandomizer import EntranceRandomizer

ENDERLILIES = "Ender Lilies"

class EnderLiliesEvent(Item):
    game = ENDERLILIES

    def key(self):
        return self.name

class EnderLiliesItem(Item):
    game = ENDERLILIES
    data : ItemData

    def __init__(self, name: str, data : ItemData, player: int):
        super().__init__(name, data.classification, data.code, player)
        self.data = data

    def key(self):
        return self.data.key

class EnderLiliesLocation(Location):
    game = ENDERLILIES
    data : LocationData

    def __init__(self, player: int, name: str, data : LocationData, parent: Optional[Region] = None):
        super().__init__(player, name, data.address, parent)
        self.data = data

    def key(self):
        return self.data.key


class EnderLiliesWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS
    """

    game = ENDERLILIES
    option_definitions = options
    location_name_to_id = {name: data.address for name, data in locations.items()}
    item_name_to_id = {name: data.code for name, data in items.items()}

    def generate_early(self):
        early_maneuver_opt = self.get_option(EarlyManeuver)
        if early_maneuver_opt.value != 0:
            # Maneuver items of interest depends on starting location
            maneuver_items = early_maneuver_opt.get_early_maneuver(
                                                      self.get_option(StartingLocation))
            if early_maneuver_opt.value == 1:
                non_local_items = self.multiworld.non_local_items[self.player].value
                avail_local_maneuver = [item for item in maneuver_items 
                                          if item not in non_local_items]
                item_name = self.multiworld.random.choice(avail_local_maneuver)
                self.multiworld.local_early_items[self.player][item_name] = 1
            elif early_maneuver_opt.value == 2:
                item_name = self.multiworld.random.choice(maneuver_items)
                self.multiworld.early_items[self.player][item_name] = 1

    def create_item(self, item: str) -> EnderLiliesItem:
        if item in self.item_name_to_id:
            item_object = EnderLiliesItem(item, items[item], self.player)
        else:
            item_object = EnderLiliesEvent(item, ItemClassification.progression, None, self.player)
        return item_object

    def create_items(self) -> None:
        starting_items = self.assign_starting_items()

        pool = []
        for item, data in items.items():
            if item in starting_items or data.unused and not self.get_option(AddUnusedItems):
                continue
            for i in range(data.count):
                pool.append(self.create_item(item))
        unfilled_location = self.multiworld.get_unfilled_locations(self.player)
        self.multiworld.random.shuffle(pool)
        pool : List[EnderLiliesItem] = self.get_option(ItemPoolPriority).sort_items_list(pool, len(unfilled_location))

        if self.get_option(StoneTabletsPlacement).value == StoneTabletsPlacement.option_region:
            self.multiworld.local_items[self.player].value.add("Stone Tablet Fragment")
            for item in pool:
                if item.name == 'Stone Tablet Fragment':
                    item.classification = ItemClassification.progression_skip_balancing

        self.multiworld.itempool.extend(pool)

    def create_regions(self) -> None:
        regions = {
            "Menu": Region("Menu", self.player, self.multiworld),
            "Game": Region("Game", self.player, self.multiworld),
        }
        self.multiworld.regions.extend(regions.values())
        victory = self.get_option(Goal).get_victory_locations()
        regions["Menu"].connect(regions["Game"])
        
        randomized_entrances = {}
        starting_location = self.get_option(StartingLocation).get_starting_location()        
        if self.get_option(RandomizeEntrances):
            er = EntranceRandomizer(starting_location)
            portals = er.get_portals()
            self.multiworld.random.shuffle(portals)
            randomized_entrances = er.Randomize(portals)

        for location, data in locations.items():
            check = EnderLiliesLocation(self.player, location, data, regions["Game"])
            if not data.address:
                check.show_in_spoiler = False
                if location in victory:
                    check.place_locked_item(self.create_item("Victory"))
                else:
                    if location in randomized_entrances:
                        check.place_locked_item(self.create_item(randomized_entrances[location]))
                        check.show_in_spoiler = True
                    else:
                        check.place_locked_item(self.create_item(data.content))
            regions["Game"].locations.append(check)

    def post_fill(self) -> None:
        if self.get_option(StoneTabletsPlacement) == StoneTabletsPlacement.option_region:
            tablets_locations : List[Location]  = self.multiworld.find_item_locations(el["tablet"], self.player)
            tablet : EnderLiliesItem = tablets_locations[0].item
            valid_locations : List[Location]  = [location for location in self.multiworld.get_locations(self.player) if not location.locked and location.can_fill(self.multiworld.state, tablet) and location.item == None or not location.item.advancement]
            self.multiworld.random.shuffle(valid_locations)
            swaps : List[Tuple[Location, Location]] = StoneTabletsPlacement.place_tablets_in_regions(tablets_locations, valid_locations)
            for swap in swaps:
                swap_location_item(swap[0], swap[1], True)
        return super().post_fill()

    def set_rules(self) -> None:
        locations_rules, items_rules = get_rules(self.player)

        for name, rule in locations_rules.items():
            set_rule(self.multiworld.get_location(name, self.player), rule)
        for name, rule in items_rules.items():
            add_item_rule(self.multiworld.get_location(name, self.player), rule)

        starting_location = self.get_option(StartingLocation).get_starting_location()
        set_rule(self.multiworld.get_location(starting_location, self.player), lambda s : True)

        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Victory", self.player
        )

    def fill_slot_data(self) -> Dict[str, Any]:
        # Content that will be send to the game
        slot_data: Dict[str, Any] = {}

        # Data for LiveSplit
        slot_data['AP.victory'] = self.get_option(Goal).get_victory_locations()
        slot_data['AP.key_to_address'] = {data.key: data.address  for _, data in locations.items() if data.address and data.key}
        slot_data['AP.key_to_code'] = {data.key: data.code for _, data in items.items() if data.code and data.key}

        # Data that will be in the seed file
        slot_data["SEED"] = str(self.multiworld.seed)
        if self.get_option(ShuffleRelicsCosts):
            slot_data[f'SETTINGS:{ShuffleRelicsCosts.name}'] = None
        if self.get_option(SubSpiritsIncreaseChapter):
            slot_data[f'SETTINGS:{SubSpiritsIncreaseChapter.name}'] = None
        if self.get_option(NewGamePlusAI):
            slot_data[f'SETTINGS:NG+'] = None
        if self.get_option(ShuffleSpiritsUpgrades):
            slot_data[f'SETTINGS:{ShuffleSpiritsUpgrades.name}'] = None
        if self.get_option(StartingWeaponUsesAncientSouls):
            slot_data[f'SETTINGS:{StartingWeaponUsesAncientSouls.name}'] = None
        if self.get_option(ShuffleBGM):
            slot_data[f'SETTINGS:{ShuffleBGM.name}'] = None
        if self.get_option(ChapterMin).value != ChapterMin.default:
            slot_data[f'SETTINGS:{ChapterMin.name}'] = str(self.get_option(ChapterMin).value)
        if self.get_option(ChapterMax).value != ChapterMax.default:
            slot_data[f'SETTINGS:{ChapterMax.name}'] = str(self.get_option(ChapterMax).value)
        slot_data["SETTINGS:starting_room"] = str(self.get_option(StartingLocation).value)
        for location in self.multiworld.get_locations(self.player):
            if location.show_in_spoiler:
                if location.item.player == self.player:
                    slot_data[location.key()] = f"{location.item.key()}"
                else:
                    slot_data[location.key()] = f"AP.{self.multiworld.player_name[location.item.player]}|{location.item.game}|{location.item.name}"
        return slot_data

    def get_option(self, option: Union[str, Type[Option]]) -> Option:
        if self.multiworld is None:
            return option.default
        if isinstance(option, str):
            return self.multiworld.__getattribute__(option)[self.player]
        return self.multiworld.__getattribute__(option.name)[self.player]

    def get_filler_item_name(self) -> str:
        return "nothing"

    def assign_starting_items(self) -> List[str]:
        weapon_name = self.get_option(StartingSpirit).get_starting_weapon_pool()
        if isinstance(weapon_name, list):
            weapon_name = self.multiworld.random.choice(weapon_name)
        starting_weapon = self.create_item(weapon_name)
        self.multiworld.get_location("Starting Spirit", self.player).place_locked_item(starting_weapon)
        return [weapon_name]
