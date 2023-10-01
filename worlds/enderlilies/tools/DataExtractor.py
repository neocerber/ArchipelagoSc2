import json
import re

from typing import Dict

json_path       = "worlds/enderlilies/data/EnderLilies.Randomizer.json"
names_path      = "worlds/enderlilies/Names.py"
items_path      = "worlds/enderlilies/Items.py"
locations_path  = "worlds/enderlilies/Locations.py"
rules_path      = "worlds/enderlilies/Rules.py"

def set_is_progress(item: str):
    global items
    if item in items:
        items[item][1] = 'progression'


def is_useful(item : str):
    return item.startswith('Aptitude') or item == "Generic.i_FinalPassivePart_Up"

def add_item(item : str):
    global items
    if item not in items:
        if is_useful(item):
            items[item] = [0, 'progression']
        else:
            items[item] = [0, 'filler']
    items[item][0] += 1

def rule_to_py(rule: str) -> str:
    global macros, item_aliases, nodes_aliases

    # Tokenization
    logic_pattern = r"\b\w+\b|\(|\)|\||\+"
    logic_tokens = re.findall(logic_pattern, rule)
    
    conversion = {
        "(" : "(",
        ")" : ")",
        "+" : " and ",
        "|" : " or ",
    }

    py_rule = ""
    for token in logic_tokens:
        if token in conversion:
            py_rule += conversion[token]
        elif token in macros:
            py_rule += f"macros['{token}'](s)"
        elif token in nodes_aliases:
            py_rule += f"s.can_reach(el['{token}'], 'Location', p)"
        elif token in item_aliases:
            py_rule += f"s.has(el['{token}'], p)"
            set_is_progress(item_aliases[token])
        else:
            py_rule += f"s.has('{token}', p)"
            set_is_progress(token)
    return py_rule

with open(json_path, "r") as f:
    data = json.load(f)

item_aliases = {}
nodes_aliases = {}

events : Dict[str, any] = {}
items : Dict[str, any] = {}
regions : Dict[str, any] = {}
locations : Dict[str, any] = {}
macros : Dict[str, any] = {}

for alias, item in data["items_alias"].items():
    item_aliases[alias] = item

for alias, node in data["nodes_alias"].items():
    if node.startswith("Map."):
        item_aliases[alias] = node
    else:
        nodes_aliases[alias] = node

for name, rule in data["macros"].items():
    macros[name] = rule

for node_name, node in data["nodes"].items():
    if "content" in node:
        if node["content"].startswith("Map."):
            events[node_name] = node["content"]
        else:
            locations[node_name] = node
            add_item(node["content"])
    else:
        events[node_name] = node_name
    matches = re.findall(r"^[^_]+_[^_]+", node_name)
    if not matches:
        region = "__no_region"
    else:
        region = matches[0]
    if region not in regions:
        regions[region] = []
    regions[region].append(node_name)
    
for name in data["extra_items"]:
    add_item(name)

with open(names_path, "w") as names_py:
    print(f"from typing import Dict\n", file=names_py)
    
    maxlen = max(len(max(item_aliases.keys(), key=len)),
                 len(max(nodes_aliases.keys(), key=len)))
    print("names : Dict[str, str] = {", file=names_py)
    for alias in item_aliases:
        print(f'\t"{alias}"{"".ljust(maxlen - len(alias))} : "{item_aliases[alias]}",' ,file=names_py)
    for alias in nodes_aliases:
        print(f'\t"{alias}"{"".ljust(maxlen - len(alias))} : "{nodes_aliases[alias]}",' ,file=names_py)
    print("}\n", file=names_py)

with open(rules_path, "w") as rules_py:
    print(f"from typing import Dict, Tuple", file=rules_py)
    print(f"from worlds.generic.Rules import CollectionRule, ItemRule", file=rules_py)
    print(f"from .Names import names as el\n", file=rules_py)
    
    print(f"def get_rules(p : int) -> Tuple[Dict[str, CollectionRule], Dict[str, ItemRule]]: \n", file=rules_py)
    
    maxlen = len(max(macros.keys(), key=len))
    print("\tmacros : Dict[str, CollectionRule] = {", file=rules_py)
    for macro, rule in macros.items():
        py_rule = rule_to_py(rule)
        print(f"\t\t'{macro}'{''.ljust(maxlen - len(macro))} : lambda s : {py_rule}," ,file=rules_py)
    print("\t}\n", file=rules_py)

    maxlen = len(max(data["nodes"].keys(), key=len))
    print("\tlocations_rules : Dict[str, CollectionRule] = {", file=rules_py)
    for node_name, node in data["nodes"].items():
        if 'rules' in node:
            py_rule = rule_to_py(node['rules'])
        else:
            py_rule = "True"
        print(f"\t\t'{node_name}'{''.ljust(maxlen - len(node_name))} : lambda s : {py_rule}," ,file=rules_py)
    print("\t}\n", file=rules_py)

    print("\titems_rules : Dict[str, ItemRule] = {", file=rules_py)
    print("\t\t'starting_weapon' : lambda item : item.player == p and item.name.startswith('Spirit.'),", file=rules_py)
    print("\t}\n", file=rules_py)
    
    print("\treturn (locations_rules, items_rules)", file=rules_py)

with open(items_path, "w") as items_py:
    print("from typing import Optional, NamedTuple, Dict", file=items_py)
    print("from BaseClasses import ItemClassification as IC\n", file=items_py)
    print("class ItemData(NamedTuple):\n\
    code: Optional[int]\n\
    count: Optional[int]\n\
    classification: IC\n", file=items_py)
    print("items : Dict[str, ItemData]= {", file=items_py)
    keys : list[str] = list(items.keys())
    keys.sort()
    code = 1
    maxlen = len(max(keys, key=len))
    for item in keys:
        print(f"\t'{item}'{''.ljust(maxlen - len(item))} : ItemData(code={code:#0{4}x}, count={str(items[item][0]).ljust(2)}, classification=IC.{items[item][1]}),", file=items_py)
        code += 1
    print("}\n", file=items_py)

with open(locations_path, "w") as locations_py:
    print("from typing import Optional, NamedTuple, Dict\n", file=locations_py)

    print("class LocationData(NamedTuple):\n\
    address: Optional[int]\n\
    content: str\n", file=locations_py)
    
    address = 1
    maxlen = max(len(max(locations.keys(), key=len)),
                 len(max(events.keys(), key=len)))
    print("locations : Dict[str, LocationData]= {", file=locations_py)
    for node_name, node in locations.items():
        print(f"\t'{node_name}'{''.ljust(maxlen - len(node_name))} : LocationData(address={address:#0{5}x}, content='{node['content']}'),", file=locations_py)
        address += 1
    print("\n# entrances and events\n", file=locations_py)
    for node_name, content in events.items():
        print(f"\t'{node_name}'{''.ljust(maxlen - len(node_name))} : LocationData(address=None, content='{content}'),", file=locations_py)
    print("}", file=locations_py)
