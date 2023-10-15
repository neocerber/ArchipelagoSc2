from worlds.AutoWorld import World
from BaseClasses import Item
from operator import index
from typing import Any, Dict, Type, List, Union, FrozenSet
from Options import Choice, Option, DefaultOnToggle
from .Names import names as el


def option(name: str):
    @classmethod
    def get_option(cls, world: World) -> Option:
        return getattr(world.multiworld, cls.name)[world.player]

    def decorator(cls: Type[Option]) -> Type[Option]:
        cls.name = name
        cls.get_option = get_option
        return cls

    return decorator


@option("starting_spirit")
class StartingSpirit(Choice):
    """Defines the spirit you start with, starting spirit will have infinite usage.
    default: Any Main Spirit."""

    display_name = "Starting spirit"

    option_any_main_spirit = 26
    option_any_sub_spirit = 27

    option_umbral = 0
    option_gerrod = 1
    option_silva = 2
    option_julius = 3
    option_ulv = 4
    option_eleine = 5
    option_hoenir = 6
    option_faden = 7

    option_siegrid = 8
    option_youth = 9
    option_defender = 10
    option_bird = 11
    option_dog = 12
    option_archer = 13
    option_crypt = 14
    option_fungal = 15
    option_floral = 16
    option_sentinel = 17
    option_subject = 18
    option_executionner = 19
    option_sinner = 20
    option_champion = 21
    option_elder = 22
    option_chief = 23
    option_aegis = 24
    option_fellwyrm = 25

    spirits = [
        el["umbral"],
        el["gerrod"],
        el["silva"],
        el["julius"],
        el["ulv"],
        el["eleine"],
        el["hoenir"],
        el["faden"],
        el["siegrid"],
        el["youth"],
        el["defender"],
        el["bird"],
        el["dog"],
        el["archer"],
        el["crypt"],
        el["fungal"],
        el["floral"],
        el["sentinel"],
        el["subject"],
        el["executionner"],
        el["sinner"],
        el["champion"],
        el["elder"],
        el["chief"],
        el["aegis"],
        el["fellwyrm"],
    ]

    default = option_any_main_spirit

    def get_starting_weapon_pool(self) -> List[str]:
        if self.value == StartingSpirit.option_any_main_spirit:
            return StartingSpirit.spirits[:8]
        elif self.value == StartingSpirit.option_any_sub_spirit:
            return StartingSpirit.spirits[8:]
        else:
            return StartingSpirit.spirits[self.value]


@option("starting_location")
class StartingLocation(Choice):
    """Defines where you start the game.
    default: start."""

    display_name = "Starting location"

    option_start = 0
    option_cellar = 3
    option_cathedral_cloister = 5
    option_saints_passage = 9
    option_crossroads = 12

    option_collapsed_shack = 19
    option_bridgehead = 23

    option_ruined_castle_cellar = 35
    option_guest_chamber = 38
    option_maelstrom_remparts = 41

    option_bastion_gates = 55
    option_courtyard = 61
    option_second_spire_chamber = 62
    option_mourninghall = 72

    option_dryad_lake = 78
    option_witchs_hermitage = 83
    option_covenhalls = 87

    option_bottom_of_the_well = 91
    option_charnel = 93
    option_ossuary = 103
    option_great_hall = 106

    option_aqueduct = 115
    option_cells = 123
    option_dark_chamber = 132
    option_execution_grounds = 138

    option_lab1 = 145
    option_lab2 = 150

    default = option_start
    id_to_name = {
        0: "Start",
        3: "Cellar",
        5: "CathedralCloister",
        9: "SaintsPassage",
        12: "Crossroads",
        19: "CollapsedShack",
        23: "BridgeHead",
        35: "RuinedCastleCellar",
        38: "GuestChamber",
        41: "MaelstromRemparts",
        55: "BastionGates",
        61: "Courtyard",
        62: "SecondSpireChamber",
        72: "MourningHall",
        78: "DryadLake",
        83: "WitchsHermitage",
        87: "CovenHalls",
        91: "BottomOfTheWell",
        93: "Charnel",
        103: "Ossuary",
        106: "GreatHall",
        115: "Aqueduct",
        123: "Cells",
        132: "DarkChamber",
        138: "ExecutionGrounds",
        145: "Lab1",
        150: "Lab2",
    }

    def get_starting_location(self) -> str:
        return el[StartingLocation.id_to_name[self.value]]


@option("item_pool_priority")
class ItemPoolPriority(Choice):
    """Defines what items will be kept in the pool when there are more items than locations left
    Useful: Give priority to useful items over filler (Findings).
    Any: Priority is the same for any non-progression items.
    All: Leave all items in the pool and let Archipelago pick
    default: Useful."""

    display_name = "Prioritize Useful Items"
    option_any = 0
    option_useful = 1
    option_all = 2
    default = option_useful

    def sort_items_list(self, items: List[Item], locations_count: int) -> None:
        def item_score(item: Item):
            if item.advancement:
                return 2
            if item.useful:
                return self.value == ItemPoolPriority.option_useful
            return 0

        if self.value == ItemPoolPriority.option_all:
            return items
        items.sort(key=item_score, reverse=True)
        return items[:locations_count]


@option("goal")
class Goal(Choice):
    """Goal to complete for Archipelago
    Ending A - Benevolence.
    Ending B - Journey's End.
    Ending C - Dawn Prayer.
    Any Ending: Achieving any Ending.
    default: Ending C"""

    display_name = "Goal"
    option_ending_a = 0
    option_ending_b = 1
    option_ending_c = 2
    option_any_ending = 3
    default = option_ending_c

    def get_victory_locations(self) -> List[str]:
        if self.value == Goal.option_ending_a:
            return ["Ending_A"]
        elif self.value == Goal.option_ending_b:
            return ["Ending_B"]
        elif self.value == Goal.option_ending_c:
            return ["Ending_C"]
        else:
            return ["Ending_A", "Ending_B", "Ending_C"]


options: Type[Option] = [
    StartingSpirit,
    StartingLocation,
    ItemPoolPriority,
    Goal,
]
