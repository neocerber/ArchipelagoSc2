from typing import Dict, FrozenSet, Union
from Options import Choice, Option, Toggle
from BaseClasses import MultiWorld


class ShuffleSlots(Toggle):
    display_name = "Shuffle Slots"

class ShuffleBGM(Toggle):
    display_name = "Shuffle Background Music"

class ShuffleEnemies(Toggle):
    display_name = "Shuffle Enemies"

class NewGamePlus(Toggle):
    display_name = "New Game Plus"

class ForceAncientSouls(Toggle):
    display_name = "Ancient Souls on starting spirit"

class MiniBossIncrementsChapter(Toggle):
    display_name = "Sub Spirits Increment Chapter"

class ShuffleUpgrades(Toggle):
    display_name = "Shuffle Upgrades"

class StartingSpirit(Choice):
    """Defines which spirit you might start with. The starting spirit has infinite usage. Default option is Umbral Knight.

    Vanilla: Umbral knight.
    Main: One of the main spirit (Gerrod, Silva, Julius, Ulv, Eleine, Hoenir, Faden, Siegrid
    Any: Any of the spirits.
    None: You will receive an item at the start but it can from any world.
        Warning: the logic currently assumes that you start with a spirit. It might make a world impossible. """
    display_name = "Starting spirits"
    option_vanilla = 0
    option_main = 1
    option_any = 2
    default = option_vanilla

el_options: Dict[str, type(Option)] = {
    # # Not added since not sure if the client can read it right now.
    # "shuffle_slots": ShuffleSlots,
    # "shuffle_bgm": ShuffleBGM,
    # "shuffle_enemies": ShuffleEnemies,
    # "new_game_plus": NewGamePlus,
    # "force_ancient_souls": ForceAncientSouls,
    # "mini_boss_incrememnts_chapter": MiniBossIncrementsChapter,
    # "shuffle_upgrades": ShuffleUpgrades,
    "starting_spirit": StartingSpirit,
}


def get_option_value(multiworld: MultiWorld, player: int, name: str) -> Union[int,  FrozenSet]:
    if multiworld is None:
        return el_options[name].default

    player_option = getattr(multiworld, name)[player]

    return player_option.value
