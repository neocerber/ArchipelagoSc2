import json
import os

from worlds.AutoWorld import World
from BaseClasses import ItemClassification, Region, Item, Location, Type
from worlds.generic.Rules import set_rule, add_item_rule
from typing import Any, Dict, List, Union
from Options import Option

from .Items import items
from .Locations import locations
from .Rules import get_rules
from .Options import *

ENDERLILIES = "Ender Lilies"


class EnderLiliesItem(Item):
    game = ENDERLILIES


class EnderLiliesLocation(Location):
    game = ENDERLILIES


class EnderLiliesWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS
    """

    game = ENDERLILIES
    option_definitions = {option_class.name: option_class for option_class in options}
    location_name_to_id = {name: data.address for name, data in locations.items()}
    item_name_to_id = {name: data.code for name, data in items.items()}

    def generate_early(self):
        val = self.get_option(EarlyManeuver).value
        if val != 0:
            maneuver_items = [el['djump'], el['silva'], el['champion'], el['claw']]

            if val == 1:
                non_local_items = self.multiworld.non_local_items[self.player].value
                avail_local_maneuver = sorted(item for item in maneuver_items 
                                          if item not in non_local_items)
                item_name = self.multiworld.random.choice(avail_local_maneuver)
                self.multiworld.local_early_items[self.player][item_name] = 1
            elif val == 2:
                item_name = self.multiworld.random.choice(maneuver_items)
                self.multiworld.early_items[self.player][item_name] = 1

    def create_item(self, item: str) -> EnderLiliesItem:
        if item in self.item_name_to_id:
            return EnderLiliesItem(
                item, items[item].classification, items[item].code, self.player
            )
        else:
            return EnderLiliesItem(
                item, ItemClassification.progression, None, self.player
            )

    def create_items(self) -> None:
        starting_items = self.assign_starting_items()
        pool = []
        for item, data in items.items():
            if item in starting_items:
                continue
            for i in range(data.count):
                pool.append(self.create_item(item))
        unfilled_location = self.multiworld.get_unfilled_locations(self.player)
        self.multiworld.random.shuffle(pool)
        pool = self.get_option(ItemPoolPriority).sort_items_list(pool, len(unfilled_location))

        self.multiworld.itempool.extend(pool)

    def create_regions(self) -> None:
        regions = {
            "Menu": Region("Menu", self.player, self.multiworld),
            "Game": Region("Game", self.player, self.multiworld),
        }
        self.multiworld.regions.extend(regions.values())
        victory = self.get_option(Goal).get_victory_locations()
        regions["Menu"].connect(regions["Game"])
        for location, data in locations.items():
            check = EnderLiliesLocation(self.player, location, data.address, regions["Game"]
            )
            if not data.address:
                check.show_in_spoiler = False
                if location in victory:
                    check.place_locked_item(self.create_item("Victory"))
                else:
                    check.place_locked_item(self.create_item(data.content))
            regions["Game"].locations.append(check)

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

    def generate_output(self, output_directory: str) -> None:
        filename = f"{self.multiworld.get_player_name(self.player)}.EnderLiliesSeed.txt"
        with open(os.path.join(output_directory, filename), "w") as f:
            print(f"SEED:{self.multiworld.seed}", file=f)
            for location in self.multiworld.get_locations(self.player):
                if location.show_in_spoiler:
                    if location.item.player == self.player:
                        print(f"{location.name}:{location.item.name}", file=f)
                    else:
                        print(f"{location.name}:AP.{location.address}", file=f)

    def fill_slot_data(self) -> Dict[str, Any]:
        # Content that will be send to the game
        slot_data: Dict[str, Any] = {}
        slot_data['SETTINGS:victory'] = self.get_option(Goal).get_victory_locations();
        slot_data["SEED"] = str(self.multiworld.seed)
        
        if self.get_option(ShuffleRelicsCosts):
            slot_data[f'SETTINGS:{ShuffleRelicsCosts.name}'] = None;
        if self.get_option(SubSpiritsIncreaseChapter):
            slot_data[f'SETTINGS:{SubSpiritsIncreaseChapter.name}'] = None;
        if self.get_option(NewGamePlusAI):
            slot_data[f'SETTINGS:{NewGamePlusAI.name}'] = None;
        if self.get_option(ShuffleSpiritsUpgrades):
            slot_data[f'SETTINGS:{ShuffleSpiritsUpgrades.name}'] = None;
        if self.get_option(StartingWeaponUsesAncientSouls):
            slot_data[f'SETTINGS:{StartingWeaponUsesAncientSouls.name}'] = None;
        if self.get_option(ShuffleBGM):
            slot_data[f'SETTINGS:{ShuffleBGM.name}'] = None;
        
        if self.get_option(ChapterMin).value != ChapterMin.default:
            slot_data[f'SETTINGS:{ChapterMin.name}'] = str(self.get_option(ChapterMin).value);
        if self.get_option(ChapterMax).value != ChapterMax.default:
            slot_data[f'SETTINGS:{ChapterMax.name}'] = str(self.get_option(ChapterMax).value);

        slot_data["SETTINGS:starting_room"] = str(self.get_option(StartingLocation).value)
        for location in self.multiworld.get_locations(self.player):
            if location.show_in_spoiler:
                if location.item.player == self.player:
                    slot_data[location.name] = f"{location.item.name}"
                else:
                    slot_data[location.name] = f"AP.{location.address}"
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
        self.multiworld.get_location("starting_weapon", self.player).place_locked_item(starting_weapon)

        return [weapon_name]
