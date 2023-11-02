from Locations import locations
from Items import items
from Names import names as el

area = {
    "Abyss": "The Abyss",
    "Castle": "Ruined Castle",
    "Cave": "Catacombs",
    "Church": "White Parish",
    "Forest": "Witch's Thicket",
    "Fort": "Twin Spires",
    "Oubliette": "Stockade",
    "Outside": "Hinterlands",
    "Swamp": "Verboten Domain",
    "Village": "Cliffside Hamlet",
}

def ReplaceKeyByNames():
    key_to_name = {data.key: location for location, data in locations.items() if data.key}
    maxlen = len(max(el.keys(), key=len))
    maxlen2 = len(max(key_to_name.values(), key=len))
    for name, key in el.items():
        if key in key_to_name:
            print(f'"{name}"{"".ljust(maxlen - len(name))} : "{key_to_name[key]}",{"".ljust(maxlen2 - len(key_to_name[key]))}# {key}')
        elif key in locations:
            print(f'"{name}"{"".ljust(maxlen - len(name))} : "{key}",{"".ljust(maxlen2 - len(key))}# {locations[key].key}')
        elif key in items:
            print(f'"{name}"{"".ljust(maxlen - len(name))} : "{key}",{"".ljust(maxlen2 - len(key))}# {items[key].key}')
        else:
            print(f'"{name}"{"".ljust(maxlen - len(name))} : "{key}",{"".ljust(maxlen2 - len(key))}# EVENT')
ReplaceKeyByNames()


def MakeUniqueNames():
    keys = {data.key: name for name, data in items.items()}

    maps = {key: al for al, key in el.items() if key.startswith("Map")}

    names = {}
    kee = {}

    size1 = 0
    size2 = 0
    for key, data in locations.items():
        size2 = max(size2, len(key))

    for loc, data in locations.items():
        region = loc.split("_", 1)[0]
        if region not in area or not data.content or not data.content.startswith("Map."):
            continue
        number = loc.split("_", 1)[1].split(".", 1)[0].rsplit("_", 1)[0]
        content = maps[data.content]
        for a in area:
            if content.startswith(a):
                l = len(a)
                content = f"{area[a]} {content[l:l+2]}"
                break
            content = content.replace(a, (area[a] + " "))

        result = f"{area[region]} {number} To {content}"
        while result in names:
            result += "_TO_RENAME"
        kee[result] = maps[data.content]
        names[result] = loc

    for item in names:
        print(names[item] + '	' + item + '	' + kee[item])
