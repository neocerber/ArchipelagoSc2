import json
import os

from worlds.AutoWorld import World
from BaseClasses import ItemClassification, Region, Item, Location, MultiWorld
from worlds.generic.Rules import set_rule, add_item_rule
from typing import Any, Dict, List

from .Items import items, ItemData
from .Locations import locations
from .Rules import get_rules
from .Names import names as el
from .Options import el_options, get_option_value

ENDERLILIES = "Ender Lilies"

class EnderLiliesItem(Item):
    game = ENDERLILIES

class EnderLiliesLocation(Location):
    game = ENDERLILIES

class EnderLiliesWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS
    """
    game                = ENDERLILIES
    option_definitions = el_options
    location_name_to_id = { name: data.address for name, data in locations.items() }
    item_name_to_id     = { name: data.code for name, data in items.items() }

    def generate_early(self):
        val = get_option_value(self.multiworld, self.player, "early_maneuver")
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
            return EnderLiliesItem(item, items[item].classification, items[item].code, self.player)
        else:
            return EnderLiliesItem(item, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        starting_item = assign_starting_item(self.multiworld, self.player, items)
        
        filter_items_to_locations_number(self.multiworld, self.player, items) 

        for item, data in items.items():
            if item != starting_item:
                for i in range(data.count):
                    self.multiworld.itempool.append(self.create_item(item))

    def create_regions(self) -> None:
        regions = {
            'Menu' : Region('Menu', self.player, self.multiworld),
            'Game' : Region('Game', self.player, self.multiworld),
        }        
        self.multiworld.regions.extend(regions.values())
        regions["Menu"].connect(regions["Game"])
        for location, data in locations.items():
            check = EnderLiliesLocation(self.player, location, data.address, regions["Game"])
            if not data.address:
                check.show_in_spoiler = False
                check.event = True
                check.place_locked_item(self.create_item(data.content))
            regions["Game"].locations.append(check)


    def set_rules(self) -> None:
        locations_rules, items_rules = get_rules(self.player)
        player = self.player        

        can_contain_map = lambda item : item.player == player and item.name.startswith('Map.')
        cannot_contain_map = lambda item : item.name.startswith('Map.') == False

        for name, rule in locations_rules.items():
            set_rule(self.multiworld.get_location(name, self.player), rule)
        for name, rule in items_rules.items():
            add_item_rule(self.multiworld.get_location(name, self.player), rule)

        set_rule(self.multiworld.get_location(el['Start'], self.player), lambda state : True)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(el["Abyss03Left"], self.player)

    def generate_output(self, output_directory: str) -> None:
        filename = f"{self.multiworld.get_player_name(self.player)}.EnderLiliesSeed.txt"
        with open(os.path.join(output_directory, filename), 'w') as f:
            print(f"SEED:{self.multiworld.seed}", file=f)
            for location in self.multiworld.get_locations(self.player):
                if location.show_in_spoiler:
                    if location.item.player == self.player:
                        print(f"{location.name}:{location.item.name}", file=f)
                    else:
                        print(f"{location.name}:AP.{location.address}", file=f)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        slot_data["SEED"] = str(self.multiworld.seed)
        for location in self.multiworld.get_locations(self.player):
            if location.show_in_spoiler:
                if location.item.player == self.player:
                    slot_data[location.name] = f"{location.item.name}"
                else:
                    slot_data[location.name] = f"AP.{location.address}"
        return slot_data

def filter_items_to_locations_number(multiworld: MultiWorld, player: int, items):
    val = get_option_value(multiworld, player, "item_filter_behavior")
    if val != 2:
        # Not sure how to differ locations with item and entrance. Using address for now...
        nb_locations_items = len([x for x in locations if locations[x].address is not None])
        nb_items = sum([items[x].count for x in items])
        nb_excedant_items = nb_items - nb_locations_items
        if nb_excedant_items > 0:
            if val == 0:
                discard_candidates = sorted(x for x in items if items[x].classification == ItemClassification.filler)
            elif val == 1:
                discard_candidates = sorted(x for x in items if (items[x].classification == ItemClassification.filler
                                                            or items[x].classification == ItemClassification.useful))
            for i in range(nb_excedant_items):
                curr_candidate = multiworld.random.choice(discard_candidates)
                if items[curr_candidate].count == 1:
                    del items[curr_candidate] 
                    discard_candidates.remove(curr_candidate)
                else:
                    items[curr_candidate] = ItemData(code=items[curr_candidate].code, 
                                                        count=items[curr_candidate].count - 1, 
                                                        classification=items[curr_candidate].classification)

def assign_starting_item(multiworld: MultiWorld, player: int, items) -> str:
    non_local_items = multiworld.non_local_items[player].value

    val = get_option_value(multiworld, player, "starting_spirit")
    if val == 0: 
        spirit_list = ['Spirit.s5000']
    elif val == 1: 
        spirit_list = [x for x in list(items.keys()) if x.startswith('Spirit.s5')]
    elif val == 2: 
        spirit_list = [x for x in list(items.keys()) if x.startswith('Spirit.s')]

    avail_spirit = sorted(item for item in spirit_list if item not in non_local_items)
    if not avail_spirit:
        raise Exception("At least one spirit must be local")

    spirit_name = multiworld.random.choice(avail_spirit)

    item = EnderLiliesItem(spirit_name, items[spirit_name].classification, 
                           items[spirit_name].code, player)

    multiworld.get_location('starting_weapon', player).place_locked_item(item)

    return spirit_name 
