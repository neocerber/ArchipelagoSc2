from typing import List, Union

class StartingLocationData():
    yamlKey: str
    clientKey: str
    earlyManeuverItems: List[str]
    def __init__(self, yamlKey: str, clientKey: str, 
                 earlyManeuverItems: Union[List[str], str]):
        # Not used right now...
        self.yamlKey = yamlKey
        self.clientKey = clientKey
        if type(earlyManeuverItems) is not list:
            self.earlyManeuverItems = [earlyManeuverItems] 
        else:
            self.earlyManeuverItems = earlyManeuverItems
        if "LEDGE" in earlyManeuverItems:
            self.earlyManeuverItems.remove("LEDGE")
            self.earlyManeuverItems.extend(["djump", "silva", "champion"])
        # For random seed determinism
        self.earlyManeuverItems.sort()

startingLocationsData = {}
startingLocationsData[0] = StartingLocationData("start", 
                                    "Start", ["LEDGE", "claw"])
startingLocationsData[3] = StartingLocationData("cellar", 
                                    "Cellar", ["LEDGE", "claw"])
startingLocationsData[5] = StartingLocationData("cathedral_cloister", 
                                    "CathedralCloister", ["LEDGE", "claw"])
startingLocationsData[9] = StartingLocationData("saints_passage", 
                                    "SaintsPassage", ["LEDGE", "claw"])
startingLocationsData[12] = StartingLocationData("crossroads", 
                                    "Crossroads", ["LEDGE", "claw"])
startingLocationsData[19] = StartingLocationData("collapsed_shack", 
                                    "CollapsedShack", ["LEDGE", "hook"])
startingLocationsData[23] = StartingLocationData("bridgehead", 
                                    "BridgeHead", "swim")
startingLocationsData[35] = StartingLocationData("ruined_castle_cellar", 
                                    "RuinedCastleCellar", ["LEDGE", "claw"])
startingLocationsData[38] = StartingLocationData("guest_chamber", 
                                    "GuestChamber", ["LEDGE", "claw"])
startingLocationsData[41] = StartingLocationData("maelstrom_remparts", 
                                    "MaelstromRemparts", "claw")
startingLocationsData[55] = StartingLocationData("bastion_gates", 
                                    "BastionGates", ["LEDGE", "sinner"])
startingLocationsData[61] = StartingLocationData("courtyard", 
                                    "Courtyard", "LEDGE")
startingLocationsData[62] = StartingLocationData("second_spire_chamber", 
                                    "SecondSpireChamber", "LEDGE")
startingLocationsData[72] = StartingLocationData("mourninghall", 
                                    "MourningHall", "claw")
startingLocationsData[78] = StartingLocationData("dryad_lake", 
                                    "DryadLake", ["LEDGE", "claw"])
startingLocationsData[83] = StartingLocationData("witchs_hermitage", 
                                    "WitchsHermitage", "LEDGE")
startingLocationsData[87] = StartingLocationData("covenhalls", 
                                    "CovenHalls", "LEDGE")
startingLocationsData[91] = StartingLocationData("bottom_of_the_well", 
                                    "BottomOfTheWell", "claw")
startingLocationsData[93] = StartingLocationData("charnel", 
                                    "Charnel", "claw")
startingLocationsData[103] = StartingLocationData("ossuary", 
                                    "Ossuary", ["LEDGE", "claw", "sinner"])
startingLocationsData[106] = StartingLocationData("great_hall", 
                                    "GreatHall", "claw")
startingLocationsData[115] = StartingLocationData("aqueduct", 
                                    "Aqueduct", ["LEDGE", "claw", "swim"])
startingLocationsData[123] = StartingLocationData("cells", 
                                    "Cells", "swim")
startingLocationsData[132] = StartingLocationData("dark_chamber", 
                                    "DarkChamber", "hook")
startingLocationsData[138] = StartingLocationData("execution_grounds", 
                                    "ExecutionGrounds", "hook")
startingLocationsData[145] = StartingLocationData("lab1", 
                                    "Lab1", "swim")
startingLocationsData[150] = StartingLocationData("lab2", 
                                    "Lab2", "LEDGE")