from typing import Dict, Tuple
from worlds.generic.Rules import CollectionRule, ItemRule
from .Names import names as el

def get_rules(p : int) -> Tuple[Dict[str, CollectionRule], Dict[str, ItemRule]]: 

	macros : Dict[str, CollectionRule] = {
#		               djump + silva + champion
		'3LEDGE'      : lambda s : s.has(el['djump'], p) and s.has(el['silva'], p) and s.has(el['champion'], p),
#		               djump + silva | djump + champion | silva + champion
		'2LEDGE'      : lambda s : s.has(el['djump'], p) and s.has(el['silva'], p) or s.has(el['djump'], p) and s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['champion'], p),
#		               djump | silva | champion
		'LEDGE'       : lambda s : s.has(el['djump'], p) or s.has(el['silva'], p) or s.has(el['champion'], p),
#		               dodge + sinner
		'2HORIZONTAL' : lambda s : s.has(el['dodge'], p) and s.has(el['sinner'], p),
#		               dodge | sinner
		'HORIZONTAL'  : lambda s : s.has(el['dodge'], p) or s.has(el['sinner'], p),
#		               silva + djump + dodge
		'FULLSILVA'   : lambda s : s.has(el['silva'], p) and s.has(el['djump'], p) and s.has(el['dodge'], p),
#		               pierce + dash
		'CHARGE'      : lambda s : s.has(el['pierce'], p) and s.has(el['dash'], p),
#		               heal1 + heal2 + heal3
		'3HEAL'       : lambda s : s.has(el['heal1'], p) and s.has(el['heal2'], p) and s.has(el['heal3'], p),
	}

	locations_rules : Dict[str, CollectionRule] = {
#		                                                                           Abyss01Top
		'Abyss_01_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Abyss01Top'], p),
#		                                                                           Abyss01Bottom
		'Abyss_01_GAMEPLAY.BP_SCR_LV2M_2171_2'                                    : lambda s : s.has(el['Abyss01Bottom'], p),
#		                                                                           Abyss01Top
		'Abyss_01_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Abyss01Top'], p),
#		                                                                           Abyss01Bottom | Abyss01Top + CHARGE + slam + swim + (2HORIZONTAL + LEDGE | FULLSILVA | 3LEDGE | silva + (dodge | djump) | champion + djump | claw + HORIZONTAL + LEDGE) + (hook | FULLSILVA | 3LEDGE | 2HORIZONTAL + LEDGE)
		'Abyss_01_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Abyss01Bottom'], p) or s.has(el['Abyss01Top'], p) and macros['CHARGE'](s) and s.has(el['slam'], p) and s.has(el['swim'], p) and (macros['2HORIZONTAL'](s) and macros['LEDGE'](s) or macros['FULLSILVA'](s) or macros['3LEDGE'](s) or s.has(el['silva'], p) and (s.has(el['dodge'], p) or s.has(el['djump'], p)) or s.has(el['champion'], p) and s.has(el['djump'], p) or s.has(el['claw'], p) and macros['HORIZONTAL'](s) and macros['LEDGE'](s)) and (s.has(el['hook'], p) or macros['FULLSILVA'](s) or macros['3LEDGE'](s) or macros['2HORIZONTAL'](s) and macros['LEDGE'](s)),
#		                                                                           Abyss02Top + claw + (2LEDGE | 2LEDGE + HORIZONTAL | 2HORIZONTAL + LEDGE | dodge + dash + LEDGE)
		'Abyss_02_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                     : lambda s : s.has(el['Abyss02Top'], p) and s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) and macros['LEDGE'](s) or s.has(el['dodge'], p) and s.has(el['dash'], p) and macros['LEDGE'](s)),
#		                                                                           Abyss02Top
		'Abyss_02_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Abyss02Top'], p),
#		                                                                           Abyss02Top
		'Abyss_02_GAMEPLAY.BP_Interactable_Item_Tip4'                             : lambda s : s.has(el['Abyss02Top'], p),
#		                                                                           Abyss02Top
		'Abyss_02_GAMEPLAY.BP_Interactable_Passive_healcountup_2'                 : lambda s : s.has(el['Abyss02Top'], p),
#		                                                                           Abyss02Right | Abyss02Top
		'Abyss_02_GAMEPLAY.BP_WorldTravelVolume'                                  : lambda s : s.has(el['Abyss02Right'], p) or s.has(el['Abyss02Top'], p),
#		                                                                           Abyss02Top | Abyss02Right
		'Abyss_02_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Abyss02Top'], p) or s.has(el['Abyss02Right'], p),
#		                                                                           Abyss03Left
		'Abyss_03_GAMEPLAY.BP_WorldTravelVolume3_8'                               : lambda s : s.has(el['Abyss03Left'], p),
#		                                                                           Abyss04Top + mask + slam + hook + 3HEAL + dash
		'Abyss_04_GAMEPLAY.BP_SCR_LV1L_2170_2'                                    : lambda s : s.has(el['Abyss04Top'], p) and s.has(el['mask'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                                           Abyss04Top + mask + slam + hook + 3HEAL + dash
		'Abyss_04_GAMEPLAY.BP_SCR_LV1L_2170_3'                                    : lambda s : s.has(el['Abyss04Top'], p) and s.has(el['mask'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                                           Abyss04Top
		'Abyss_04_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Abyss04Top'], p),
#		                                                                           Abyss04Bottom | Abyss04Top + mask + swim + slam + hook + 3HEAL + dash
		'Abyss_04_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Abyss04Bottom'], p) or s.has(el['Abyss04Top'], p) and s.has(el['mask'], p) and s.has(el['swim'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                                           Abyss05Top
		'Abyss_05_GAMEPLAY.BP_Interactable_Item_FinalPassivePart_2'               : lambda s : s.has(el['Abyss05Top'], p),
#		                                                                           Abyss05Top
		'Abyss_05_GAMEPLAY.BP_Interactable_Item_Tip4'                             : lambda s : s.has(el['Abyss05Top'], p),
#		                                                                           Abyss05Top
		'Abyss_05_GAMEPLAY.BP_Interactable_WorldTravel_2'                         : lambda s : s.has(el['Abyss05Top'], p),
#		                                                                           Abyss05Top
		'Abyss_05_GAMEPLAY.BP_SCR_LV3S_5000_1'                                    : lambda s : s.has(el['Abyss05Top'], p),
#		                                                                           Abyss05Top
		'Abyss_05_GAMEPLAY.BP_WorldTravelVolume'                                  : lambda s : s.has(el['Abyss05Top'], p),
#		                                                                           Castle01Left | Castle01Right1 | Castle01Top | Castle01Right2
		'Castle_01_GAMEPLAY.BP_e2082_Dog'                                         : lambda s : s.has(el['Castle01Left'], p) or s.has(el['Castle01Right1'], p) or s.has(el['Castle01Top'], p) or s.has(el['Castle01Right2'], p),
#		                                                                           Castle01Right2 + (LEDGE | HORIZONTAL)
		'Castle_01_GAMEPLAY.BP_Interactable_Passive_healcountup_4'                : lambda s : s.has(el['Castle01Right2'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Castle01Right1 | Castle01Top
		'Castle_01_GAMEPLAY.BP_Interactable_Passive_Spirit_StunStaminaDamageUp_2' : lambda s : s.has(el['Castle01Right1'], p) or s.has(el['Castle01Top'], p),
#		                                                                           Dog + CHARGE
		'Castle_01_GAMEPLAY.BP_SCR_LV1L_2031_2'                                   : lambda s : s.can_reach(el['Dog'], 'Location', p) and macros['CHARGE'](s),
#		                                                                           Dog + CHARGE
		'Castle_01_GAMEPLAY.BP_SCR_LV2M_2001_2'                                   : lambda s : s.can_reach(el['Dog'], 'Location', p) and macros['CHARGE'](s),
#		                                                                           Castle01Left | Dog
		'Castle_01_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle01Left'], p) or s.can_reach(el['Dog'], 'Location', p),
#		                                                                           Castle01Right2
		'Castle_01_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Castle01Right2'], p),
#		                                                                           Castle01Right1 | Castle01Top
		'Castle_01_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Castle01Right1'], p) or s.has(el['Castle01Top'], p),
#		                                                                           Castle01Right1 + claw
		'Castle_01_GAMEPLAY.BP_WorldTravelVolume6'                                : lambda s : s.has(el['Castle01Right1'], p) and s.has(el['claw'], p),
#		                                                                           Castle02Top
		'Castle_02_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Castle02Top'], p),
#		                                                                           Castle02Top | Castle02Left2 + (hook | LEDGE | claw)
		'Castle_02_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Castle02Top'], p) or s.has(el['Castle02Left2'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Castle02Top + hook
		'Castle_02_GAMEPLAY.BP_SCR_LV1M_2000_3'                                   : lambda s : s.has(el['Castle02Top'], p) and s.has(el['hook'], p),
#		                                                                           Castle02Left2 | Castle02Left1 | Castle02Top | Castle02Bottom
		'Castle_02_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle02Left2'], p) or s.has(el['Castle02Left1'], p) or s.has(el['Castle02Top'], p) or s.has(el['Castle02Bottom'], p),
#		                                                                           Castle02Bottom | Castle02Left2
		'Castle_02_GAMEPLAY.BP_WorldTravelVolume2_5'                              : lambda s : s.has(el['Castle02Bottom'], p) or s.has(el['Castle02Left2'], p),
#		                                                                           Castle02Left1 | Castle02Left2 + (claw + LEDGE)
		'Castle_02_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle02Left1'], p) or s.has(el['Castle02Left2'], p) and (s.has(el['claw'], p) and macros['LEDGE'](s)),
#		                                                                           (Castle03Top1 | Castle03Top2) + (hook | claw | HORIZONTAL | dash | LEDGE)
		'Castle_03_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : (s.has(el['Castle03Top1'], p) or s.has(el['Castle03Top2'], p)) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['HORIZONTAL'](s) or s.has(el['dash'], p) or macros['LEDGE'](s)),
#		                                                                           (Castle03Top1 | Castle03Top2) + (hook | claw | LEDGE + HORIZONTAL)
		'Castle_03_GAMEPLAY.BP_SCR_LV1M_2001_2'                                   : lambda s : (s.has(el['Castle03Top1'], p) or s.has(el['Castle03Top2'], p)) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Castle03Bottom | Castle03Top1 | Castle03Top2
		'Castle_03_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Castle03Bottom'], p) or s.has(el['Castle03Top1'], p) or s.has(el['Castle03Top2'], p),
#		                                                                           Castle03Top1 + claw
		'Castle_03_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Castle03Top1'], p) and s.has(el['claw'], p),
#		                                                                           Castle03Top2 + claw
		'Castle_03_GAMEPLAY.BP_WorldTravelVolume6'                                : lambda s : s.has(el['Castle03Top2'], p) and s.has(el['claw'], p),
#		                                                                           Castle04Top
		'Castle_04_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle04Top'], p),
#		                                                                           Castle04Top | RuinedCastleCellar + (LEDGE | claw)
		'Castle_04_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle04Top'], p) or s.can_reach(el['RuinedCastleCellar'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Castle05Bottom | Castle05Right | Castle05Left | Castle05Top
		'Castle_05_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Castle05Bottom'], p) or s.has(el['Castle05Right'], p) or s.has(el['Castle05Left'], p) or s.has(el['Castle05Top'], p),
#		                                                                           Castle05Right | Castle05Bottom
		'Castle_05_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle05Right'], p) or s.has(el['Castle05Bottom'], p),
#		                                                                           Castle05Left | Castle05Bottom
		'Castle_05_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle05Left'], p) or s.has(el['Castle05Bottom'], p),
#		                                                                           Castle05Top
		'Castle_05_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle05Top'], p),
#		                                                                           Castle06Top
		'Castle_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Castle06Top'], p),
#		                                                                           Castle06Top | Castle06Right
		'Castle_06_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Castle06Top'], p) or s.has(el['Castle06Right'], p),
#		                                                                           Castle06Right | Castle06Top | Castle06Left
		'Castle_06_GAMEPLAY.BP_Interactable_WorldTravel2'                         : lambda s : s.has(el['Castle06Right'], p) or s.has(el['Castle06Top'], p) or s.has(el['Castle06Left'], p),
#		                                                                           Castle06Right + claw
		'Castle_06_GAMEPLAY.BP_SCR_LV1L_2030_3'                                   : lambda s : s.has(el['Castle06Right'], p) and s.has(el['claw'], p),
#		                                                                           Castle06Left | Castle06Top
		'Castle_06_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle06Left'], p) or s.has(el['Castle06Top'], p),
#		                                                                           Castle07Right | Castle07Left
		'Castle_07_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle07Right'], p) or s.has(el['Castle07Left'], p),
#		                                                                           Castle07Right | GuestChamber + (hook | 3LEDGE)
		'Castle_07_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle07Right'], p) or s.can_reach(el['GuestChamber'], 'Location', p) and (s.has(el['hook'], p) or macros['3LEDGE'](s)),
#		                                                                           Castle07Left | GuestChamber
		'Castle_07_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle07Left'], p) or s.can_reach(el['GuestChamber'], 'Location', p),
#		                                                                           Castle08Top + claw + (LEDGE | HORIZONTAL)
		'Castle_08_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                   : lambda s : s.has(el['Castle08Top'], p) and s.has(el['claw'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Castle08Top
		'Castle_08_GAMEPLAY.BP_Interactable_Passive_expup_5'                      : lambda s : s.has(el['Castle08Top'], p),
#		                                                                           Castle08Top
		'Castle_08_GAMEPLAY.BP_SCR_LV1M_2000_2'                                   : lambda s : s.has(el['Castle08Top'], p),
#		                                                                           Castle08Top
		'Castle_08_GAMEPLAY.BP_SCR_LV1M_2000_3'                                   : lambda s : s.has(el['Castle08Top'], p),
#		                                                                           Castle08Right
		'Castle_08_GAMEPLAY.BP_SCR_LV1S_2010_3'                                   : lambda s : s.has(el['Castle08Right'], p),
#		                                                                           Castle08Right | Castle08Top
		'Castle_08_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle08Right'], p) or s.has(el['Castle08Top'], p),
#		                                                                           Castle08Top | Castle08Right + (claw | LEDGE | HORIZONTAL)
		'Castle_08_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle08Top'], p) or s.has(el['Castle08Right'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Castle09Left + (2HORIZONTAL | claw + (2LEDGE | LEDGE + HORIZONTAL) | FULLSILVA | LEDGE + sinner | djump + dash + (silva | dodge))
		'Castle_09_GAMEPLAY.BP_SCR_LV2M_2000_3'                                   : lambda s : s.has(el['Castle09Left'], p) and (macros['2HORIZONTAL'](s) or s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)) or macros['FULLSILVA'](s) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['djump'], p) and s.has(el['dash'], p) and (s.has(el['silva'], p) or s.has(el['dodge'], p))),
#		                                                                           Castle09Right | Castle09Bottom
		'Castle_09_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle09Right'], p) or s.has(el['Castle09Bottom'], p),
#		                                                                           Castle09Bottom | Castle09Right | Castle09Left
		'Castle_09_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle09Bottom'], p) or s.has(el['Castle09Right'], p) or s.has(el['Castle09Left'], p),
#		                                                                           Castle09Left | Castle09Bottom
		'Castle_09_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle09Left'], p) or s.has(el['Castle09Bottom'], p),
#		                                                                           Castle10Right | Castle10Bottom
		'Castle_10_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle10Right'], p) or s.has(el['Castle10Bottom'], p),
#		                                                                           MaelstromRemparts
		'Castle_10_GAMEPLAY.BP_SCR_LV1M_2000_3'                                   : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                                           MaelstromRemparts
		'Castle_10_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                                           MaelstromRemparts
		'Castle_10_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                                           Castle11Right | Castle11Bottom2
		'Castle_11_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle11Right'], p) or s.has(el['Castle11Bottom2'], p),
#		                                                                           Castle11Left | Castle11Bottom1
		'Castle_11_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle11Left'], p) or s.has(el['Castle11Bottom1'], p),
#		                                                                           Castle11Top | Castle11Left + Castle11Right
		'Castle_11_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle11Top'], p) or s.has(el['Castle11Left'], p) and s.has(el['Castle11Right'], p),
#		                                                                           Castle11Bottom1 | Castle11Left
		'Castle_11_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Castle11Bottom1'], p) or s.has(el['Castle11Left'], p),
#		                                                                           Castle11Bottom2 | Castle11Right
		'Castle_11_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Castle11Bottom2'], p) or s.has(el['Castle11Right'], p),
#		                                                                           Castle12Bottom + (hook | (3LEDGE + claw + dodge))
		'Castle_12_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                   : lambda s : s.has(el['Castle12Bottom'], p) and (s.has(el['hook'], p) or (macros['3LEDGE'](s) and s.has(el['claw'], p) and s.has(el['dodge'], p))),
#		                                                                           Castle12Bottom
		'Castle_12_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle12Bottom'], p),
#		                                                                           Castle12Bottom
		'Castle_12_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Castle12Bottom'], p),
#		                                                                           Castle12Bottom | Castle12Left + (hook + (claw | LEDGE | HORIZONTAL) | slam)
		'Castle_12_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Castle12Bottom'], p) or s.has(el['Castle12Left'], p) and (s.has(el['hook'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.has(el['slam'], p)),
#		                                                                           Castle12Bottom + (hook | claw | HORIZONTAL)
		'Castle_12_GAMEPLAY.BP_SCR_LV1M_2001_1'                                   : lambda s : s.has(el['Castle12Bottom'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['HORIZONTAL'](s)),
#		                                                                           Castle12Left | Castle12Bottom
		'Castle_12_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle12Left'], p) or s.has(el['Castle12Bottom'], p),
#		                                                                           Castle12Right | Castle12Bottom + unlock
		'Castle_12_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle12Right'], p) or s.has(el['Castle12Bottom'], p) and s.has(el['unlock'], p),
#		                                                                           Castle13Bottom + (silva + djump + claw | (FULLSILVA | 3LEDGE) + hook | 2LEDGE + hook + claw | LEDGE + HORIZONTAL + claw + hook)
		'Castle_13_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_2'                    : lambda s : s.has(el['Castle13Bottom'], p) and (s.has(el['silva'], p) and s.has(el['djump'], p) and s.has(el['claw'], p) or (macros['FULLSILVA'](s) or macros['3LEDGE'](s)) and s.has(el['hook'], p) or macros['2LEDGE'](s) and s.has(el['hook'], p) and s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                                           Castle13Left | Castle13Bottom
		'Castle_13_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle13Left'], p) or s.has(el['Castle13Bottom'], p),
#		                                                                           Castle13Bottom | Castle13Left | Castle13Right
		'Castle_13_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle13Bottom'], p) or s.has(el['Castle13Left'], p) or s.has(el['Castle13Right'], p),
#		                                                                           Castle13Right | Castle13Bottom
		'Castle_13_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Castle13Right'], p) or s.has(el['Castle13Bottom'], p),
#		                                                                           Castle14Left + hook
		'Castle_14_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Castle14Left'], p) and s.has(el['hook'], p),
#		                                                                           Castle14Left + CHARGE + (claw | LEDGE + HORIZONTAL)
		'Castle_14_GAMEPLAY.BP_SCR_LV1L_2220_3'                                   : lambda s : s.has(el['Castle14Left'], p) and macros['CHARGE'](s) and (s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Castle14Left + (claw + (3LEDGE | FULLSILVA | sinner + 2LEDGE | silva + 2HORIZONTAL | dodge + dash + 2LEDGE))
		'Castle_14_GAMEPLAY.BP_SCR_LV2LL_0000_2'                                  : lambda s : s.has(el['Castle14Left'], p) and (s.has(el['claw'], p) and (macros['3LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['sinner'], p) and macros['2LEDGE'](s) or s.has(el['silva'], p) and macros['2HORIZONTAL'](s) or s.has(el['dodge'], p) and s.has(el['dash'], p) and macros['2LEDGE'](s))),
#		                                                                           Castle14Left | Castle14Top
		'Castle_14_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle14Left'], p) or s.has(el['Castle14Top'], p),
#		                                                                           Castle14Top | Castle14Left + (LEDGE | hook)
		'Castle_14_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle14Top'], p) or s.has(el['Castle14Left'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           TowerAlcove
		'Castle_15_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                  : lambda s : s.can_reach(el['TowerAlcove'], 'Location', p),
#		                                                                           Castle15Bottom | Castle15Left
		'Castle_15_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle15Bottom'], p) or s.has(el['Castle15Left'], p),
#		                                                                           TowerAlcove + claw + (hook | FULLSILVA + sinner | 3LEDGE)
		'Castle_15_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['TowerAlcove'], 'Location', p) and s.has(el['claw'], p) and (s.has(el['hook'], p) or macros['FULLSILVA'](s) and s.has(el['sinner'], p) or macros['3LEDGE'](s)),
#		                                                                           Castle15Bottom | TowerAlcove
		'Castle_15_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle15Bottom'], p) or s.can_reach(el['TowerAlcove'], 'Location', p),
#		                                                                           Castle16Right
		'Castle_16_GAMEPLAY.BP_e2032_BigKnight'                                   : lambda s : s.has(el['Castle16Right'], p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1M_2190_3'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1M_2190_4'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1M_2190_6'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1M_2190_7'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1M_2191_2'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1S_2100_3'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1S_2100_4'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1S_2100_6'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis
		'Castle_16_GAMEPLAY.BP_SCR_LV1S_2101_2'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Aegis + claw
		'Castle_16_GAMEPLAY.BP_SCR_LV1S_2101_4'                                   : lambda s : s.can_reach(el['Aegis'], 'Location', p) and s.has(el['claw'], p),
#		                                                                           Castle17Top | Aegis
		'Castle_16_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle17Top'], p) or s.can_reach(el['Aegis'], 'Location', p),
#		                                                                           Castle16Right | Aegis + (2LEDGE | claw)
		'Castle_16_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle16Right'], p) or s.can_reach(el['Aegis'], 'Location', p) and (macros['2LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Castle17Right + (LEDGE | claw)
		'Castle_17_GAMEPLAY.BP_SCR_LV1M_2000_3'                                   : lambda s : s.has(el['Castle17Right'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Castle17Right
		'Castle_17_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle17Right'], p),
#		                                                                           Castle17Right + LEDGE
		'Castle_17_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Castle17Right'], p) and macros['LEDGE'](s),
#		                                                                           Castle18Right + CHARGE
		'Castle_18_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Castle18Right'], p) and macros['CHARGE'](s),
#		                                                                           Castle18Bottom + (claw | hook + LEDGE) + CHARGE
		'Castle_18_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Castle18Bottom'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) and macros['CHARGE'](s),
#		                                                                           Castle18Bottom + (claw | hook + LEDGE) + CHARGE
		'Castle_18_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Castle18Bottom'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) and macros['CHARGE'](s),
#		                                                                           Castle18Bottom + hook + LEDGE + CHARGE
		'Castle_18_GAMEPLAY.BP_SCR_LV2L_2221_2'                                   : lambda s : s.has(el['Castle18Bottom'], p) and s.has(el['hook'], p) and macros['LEDGE'](s) and macros['CHARGE'](s),
#		                                                                           Castle18Right | Castle18Bottom + (claw | hook + LEDGE)
		'Castle_18_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Castle18Right'], p) or s.has(el['Castle18Bottom'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)),
#		                                                                           Castle18Bottom | Castle18Right + (claw | hook + LEDGE) | Castle18Top
		'Castle_18_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle18Bottom'], p) or s.has(el['Castle18Right'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) or s.has(el['Castle18Top'], p),
#		                                                                           Castle19Right | Castle19Left
		'Castle_19_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle19Right'], p) or s.has(el['Castle19Left'], p),
#		                                                                           KingsChamber
		'Castle_19_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['KingsChamber'], 'Location', p),
#		                                                                           KingsChamber
		'Castle_19_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.can_reach(el['KingsChamber'], 'Location', p),
#		                                                                           Castle20Left
		'Castle_20_GAMEPLAY.BP_e5030_Leader'                                      : lambda s : s.has(el['Castle20Left'], p),
#		                                                                           Julius
		'Castle_20_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['Julius'], 'Location', p),
#		                                                                           Castle21Left
		'Castle_21_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Castle21Left'], p),
#		                                                                           Castle21Left
		'Castle_21_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Castle21Left'], p),
#		                                                                           Castle21Left
		'Castle_21_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Castle21Left'], p),
#		                                                                           Castle21Left
		'Castle_21_GEO.BP_SCR_LV1L_2120_2'                                        : lambda s : s.has(el['Castle21Left'], p),
#		                                                                           Cave01Bottom | Cave01Left
		'Cave_01_GAMEPLAY.BP_Interactable_Passive_Parry_2'                        : lambda s : s.has(el['Cave01Bottom'], p) or s.has(el['Cave01Left'], p),
#		                                                                           Cave01Bottom + (claw | djump | champion | silva + dodge)  | Cave01Left + 3LEDGE + 2HORIZONTAL
		'Cave_01_GAMEPLAY.BP_SCR_LV2LL_0000_2'                                    : lambda s : s.has(el['Cave01Bottom'], p) and (s.has(el['claw'], p) or s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)) or s.has(el['Cave01Left'], p) and macros['3LEDGE'](s) and macros['2HORIZONTAL'](s),
#		                                                                           BottomOfTheWell
		'Cave_01_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.can_reach(el['BottomOfTheWell'], 'Location', p),
#		                                                                           BottomOfTheWell
		'Cave_01_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.can_reach(el['BottomOfTheWell'], 'Location', p),
#		                                                                           Cave02Right + (hook | claw + (HORIZONTAL | djump | champion + dash | silva + dash))
		'Cave_02_GAMEPLAY.BP_SCR_LV1M_2160_1'                                     : lambda s : s.has(el['Cave02Right'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['HORIZONTAL'](s) or s.has(el['djump'], p) or s.has(el['champion'], p) and s.has(el['dash'], p) or s.has(el['silva'], p) and s.has(el['dash'], p))),
#		                                                                           Cave02Right
		'Cave_02_GAMEPLAY.BP_SCR_LV1S_2020_2'                                     : lambda s : s.has(el['Cave02Right'], p),
#		                                                                           Cave02Right | Cave02Bottom | Cave02Top
		'Cave_02_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave02Right'], p) or s.has(el['Cave02Bottom'], p) or s.has(el['Cave02Top'], p),
#		                                                                           Cave02Bottom | Cave02Right + slam
		'Cave_02_GAMEPLAY.BP_WorldTravelVolume4_1'                                : lambda s : s.has(el['Cave02Bottom'], p) or s.has(el['Cave02Right'], p) and s.has(el['slam'], p),
#		                                                                           Cave02Right + claw + (FULLSILVA + dash | 3LEDGE | 2LEDGE + 2HORIZONTAL | silva + 2HORIZONTAL | silva + sinner + djump | dash + djump + champion + sinner)
		'Cave_02_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave02Right'], p) and s.has(el['claw'], p) and (macros['FULLSILVA'](s) and s.has(el['dash'], p) or macros['3LEDGE'](s) or macros['2LEDGE'](s) and macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and s.has(el['sinner'], p) and s.has(el['djump'], p) or s.has(el['dash'], p) and s.has(el['djump'], p) and s.has(el['champion'], p) and s.has(el['sinner'], p)),
#		                                                                           Cave03Left | Cave03Right | Cave03Top
		'Cave_03_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Cave03Left'], p) or s.has(el['Cave03Right'], p) or s.has(el['Cave03Top'], p),
#		                                                                           Cave03Right
		'Cave_03_GAMEPLAY.BP_Interactable_Item_Tip4'                              : lambda s : s.has(el['Cave03Right'], p),
#		                                                                           Cave03Left
		'Cave_03_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave03Left'], p),
#		                                                                           Cave03Right
		'Cave_03_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave03Right'], p),
#		                                                                           Charnel
		'Cave_03_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.can_reach(el['Charnel'], 'Location', p),
#		                                                                           Cave04Bottom
		'Cave_04_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                      : lambda s : s.has(el['Cave04Bottom'], p),
#		                                                                           Cave04Right | Cave04Bottom
		'Cave_04_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave04Right'], p) or s.has(el['Cave04Bottom'], p),
#		                                                                           Cave04Bottom | Cave04Right
		'Cave_04_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave04Bottom'], p) or s.has(el['Cave04Right'], p),
#		                                                                           Cave04Left | Cave04Bottom + unlock
		'Cave_04_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave04Left'], p) or s.has(el['Cave04Bottom'], p) and s.has(el['unlock'], p),
#		                                                                           Cave05Bottom + (hook | LEDGE | dash | HORIZONTAL)
		'Cave_05_GAMEPLAY.BP_SCR_LV1M_2161_2'                                     : lambda s : s.has(el['Cave05Bottom'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s)),
#		                                                                           Cave05Left | Cave05Bottom
		'Cave_05_GAMEPLAY.BP_WorldTravelVolume_0'                                 : lambda s : s.has(el['Cave05Left'], p) or s.has(el['Cave05Bottom'], p),
#		                                                                           Cave05Top | Cave05Bottom
		'Cave_05_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave05Top'], p) or s.has(el['Cave05Bottom'], p),
#		                                                                           Cave05Bottom | Cave05Left | Cave05Right | Cave05Top
		'Cave_05_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave05Bottom'], p) or s.has(el['Cave05Left'], p) or s.has(el['Cave05Right'], p) or s.has(el['Cave05Top'], p),
#		                                                                           Cave05Right | Cave05Bottom + (claw |  2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		'Cave_05_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave05Right'], p) or s.has(el['Cave05Bottom'], p) and (s.has(el['claw'], p) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Cave06Top
		'Cave_06_GAMEPLAY.BP_Interactable_Item_Tip4'                              : lambda s : s.has(el['Cave06Top'], p),
#		                                                                           Cave06Top
		'Cave_06_GAMEPLAY.BP_Interactable_Item_Tip5'                              : lambda s : s.has(el['Cave06Top'], p),
#		                                                                           Cave06Top
		'Cave_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                    : lambda s : s.has(el['Cave06Top'], p),
#		                                                                           Cave06Top | Cave06Bottom
		'Cave_06_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave06Top'], p) or s.has(el['Cave06Bottom'], p),
#		                                                                           Cave06Bottom | Cave06Top
		'Cave_06_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave06Bottom'], p) or s.has(el['Cave06Top'], p),
#		                                                                           Cave07Right | Cave07Top
		'Cave_07_GAMEPLAY.BP_e2162_Spider'                                        : lambda s : s.has(el['Cave07Right'], p) or s.has(el['Cave07Top'], p),
#		                                                                           Spider + swim
		'Cave_07_GAMEPLAY.BP_SCR_LV1M_2161_2'                                     : lambda s : s.can_reach(el['Spider'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Spider + claw + hook + (FULLSILVA | 3LEDGE)
		'Cave_07_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.can_reach(el['Spider'], 'Location', p) and s.has(el['claw'], p) and s.has(el['hook'], p) and (macros['FULLSILVA'](s) or macros['3LEDGE'](s)),
#		                                                                           Spider
		'Cave_07_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.can_reach(el['Spider'], 'Location', p),
#		                                                                           Cave08Left + slam
		'Cave_08_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                      : lambda s : s.has(el['Cave08Left'], p) and s.has(el['slam'], p),
#		                                                                           Cave08Top | Cave08Left + (hook | LEDGE | dash | HORIZONTAL)
		'Cave_08_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave08Top'], p) or s.has(el['Cave08Left'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s)),
#		                                                                           Cave08Left | Cave08Top | Cave08Right
		'Cave_08_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave08Left'], p) or s.has(el['Cave08Top'], p) or s.has(el['Cave08Right'], p),
#		                                                                           Cave08Bottom | Cave08Left + swim + slam
		'Cave_08_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave08Bottom'], p) or s.has(el['Cave08Left'], p) and s.has(el['swim'], p) and s.has(el['slam'], p),
#		                                                                           Cave08Right | Cave08Left
		'Cave_08_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave08Right'], p) or s.has(el['Cave08Left'], p),
#		                                                                           Cave09Top + (claw | LEDGE)
		'Cave_09_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                   : lambda s : s.has(el['Cave09Top'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Cave09Top
		'Cave_09_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                  : lambda s : s.has(el['Cave09Top'], p),
#		                                                                           Cave09Top | Cave09Bottom + (claw | LEDGE)
		'Cave_09_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave09Top'], p) or s.has(el['Cave09Bottom'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Cave09Bottom | Cave09Top | Cave09Right
		'Cave_09_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave09Bottom'], p) or s.has(el['Cave09Top'], p) or s.has(el['Cave09Right'], p),
#		                                                                           Cave09Right | Cave09Top + (sinner | dodge + (LEDGE | dash + claw) | djump + (champion | silva | dash) | claw + champion)
		'Cave_09_GAMEPLAY.BP_WorldTravelVolume6'                                  : lambda s : s.has(el['Cave09Right'], p) or s.has(el['Cave09Top'], p) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p) and s.has(el['claw'], p)) or s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['silva'], p) or s.has(el['dash'], p)) or s.has(el['claw'], p) and s.has(el['champion'], p)),
#		                                                                           Cave10Left
		'Cave_10_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                   : lambda s : s.has(el['Cave10Left'], p),
#		                                                                           Cave10Bottom
		'Cave_10_GAMEPLAY.BP_SCR_LV1S_2011_2'                                     : lambda s : s.has(el['Cave10Bottom'], p),
#		                                                                           Cave10Right | Cave10Bottom
		'Cave_10_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave10Right'], p) or s.has(el['Cave10Bottom'], p),
#		                                                                           Cave10Left | Cave10Bottom + (hook | 2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		'Cave_10_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave10Left'], p) or s.has(el['Cave10Bottom'], p) and (s.has(el['hook'], p) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Cave10Bottom | Cave10Right | Cave10Top | Cave10Left
		'Cave_10_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave10Bottom'], p) or s.has(el['Cave10Right'], p) or s.has(el['Cave10Top'], p) or s.has(el['Cave10Left'], p),
#		                                                                           Cave10Top | Cave10Bottom
		'Cave_10_GAMEPLAY.BP_WorldTravelVolume6'                                  : lambda s : s.has(el['Cave10Top'], p) or s.has(el['Cave10Bottom'], p),
#		                                                                           Cave11Left | Cave11Top | Cave11Right1 | Cave11Right2
		'Cave_11_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Cave11Left'], p) or s.has(el['Cave11Top'], p) or s.has(el['Cave11Right1'], p) or s.has(el['Cave11Right2'], p),
#		                                                                           Cave11Left + (LEDGE | HORIZONTAL | hook | dash)
		'Cave_11_GAMEPLAY.BP_SCR_LV1M_2161_2'                                     : lambda s : s.has(el['Cave11Left'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)),
#		                                                                           Cave11Tip + swim
		'Cave_11_GAMEPLAY.BP_SCR_LV2M_2050_2'                                     : lambda s : s.can_reach(el['Cave11Tip'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Cave11Left | Cave11Tip + (hook | HORIZONTAL | LEDGE | claw)
		'Cave_11_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave11Left'], p) or s.can_reach(el['Cave11Tip'], 'Location', p) and (s.has(el['hook'], p) or macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Cave11Tip + claw
		'Cave_11_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.can_reach(el['Cave11Tip'], 'Location', p) and s.has(el['claw'], p),
#		                                                                           Cave11Right1 | Cave11Tip  + (hook | claw + (LEDGE | sinner | dodge + dash) | 2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		'Cave_11_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave11Right1'], p) or s.can_reach(el['Cave11Tip'], 'Location', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['LEDGE'](s) or s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['dash'], p)) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Cave12Right
		'Cave_12_GAMEPLAY.BP_Interactable_Item_FinalPassivePart_2'                : lambda s : s.has(el['Cave12Right'], p),
#		                                                                           Cave12Right
		'Cave_12_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave12Right'], p),
#		                                                                           Cave13Top | Cave13Left | Cave13Right | Cave13Bottom
		'Cave_13_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Cave13Top'], p) or s.has(el['Cave13Left'], p) or s.has(el['Cave13Right'], p) or s.has(el['Cave13Bottom'], p),
#		                                                                           Ossuary + hook | Cave13Bottom + claw
		'Cave_13_GAMEPLAY.BP_SCR_LV2L_2091_4'                                     : lambda s : s.can_reach(el['Ossuary'], 'Location', p) and s.has(el['hook'], p) or s.has(el['Cave13Bottom'], p) and s.has(el['claw'], p),
#		                                                                           Cave13Left + (dash | LEDGE | HORIZONTAL)
		'Cave_13_GAMEPLAY.BP_SCR_LV2M_2161_5'                                     : lambda s : s.has(el['Cave13Left'], p) and (s.has(el['dash'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Ossuary
		'Cave_13_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                                           Ossuary
		'Cave_13_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                                           Cave13Left | Ossuary + (claw | 2LEDGE | sinner | LEDGE + HORIZONTAL)
		'Cave_13_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave13Left'], p) or s.can_reach(el['Ossuary'], 'Location', p) and (s.has(el['claw'], p) or macros['2LEDGE'](s) or s.has(el['sinner'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Ossuary
		'Cave_13_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                                           Cave14Right
		'Cave_14_GAMEPLAY.BP_SCR_LV1S_2020_7'                                     : lambda s : s.has(el['Cave14Right'], p),
#		                                                                           Cave14Bottom | Cave14Right | Cave14Left
		'Cave_14_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave14Bottom'], p) or s.has(el['Cave14Right'], p) or s.has(el['Cave14Left'], p),
#		                                                                           Cave14Left | Cave14Bottom + LEDGE
		'Cave_14_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave14Left'], p) or s.has(el['Cave14Bottom'], p) and macros['LEDGE'](s),
#		                                                                           Cave14Right | Cave14Bottom + (hook | claw | 2LEDGE | LEDGE + HORIZONTAL)
		'Cave_14_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave14Right'], p) or s.has(el['Cave14Bottom'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Cave15Right
		'Cave_15_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Cave15Right'], p),
#		                                                                           Cave15Right + slam
		'Cave_15_GAMEPLAY.BP_SCR_LV1L_2070_3'                                     : lambda s : s.has(el['Cave15Right'], p) and s.has(el['slam'], p),
#		                                                                           Cave15Right | Cave15Left
		'Cave_15_GAMEPLAY.BP_SCR_LV1S_2020_2'                                     : lambda s : s.has(el['Cave15Right'], p) or s.has(el['Cave15Left'], p),
#		                                                                           Cave15Right | Cave15Left + swim + (LEDGE | claw)
		'Cave_15_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave15Right'], p) or s.has(el['Cave15Left'], p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Cave15Left | Cave15Right
		'Cave_15_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave15Left'], p) or s.has(el['Cave15Right'], p),
#		                                                                           Cave16Right | Cave16Bottom | Cave16Left
		'Cave_16_GAMEPLAY.BP_Interactable_Item_Tip4'                              : lambda s : s.has(el['Cave16Right'], p) or s.has(el['Cave16Bottom'], p) or s.has(el['Cave16Left'], p),
#		                                                                           GreatHall + (hook | claw + (2LEDGE | LEDGE + HORIZONTAL))
		'Cave_16_GAMEPLAY.BP_SCR_LV1L_2091_5'                                     : lambda s : s.can_reach(el['GreatHall'], 'Location', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s))),
#		                                                                           Cave16Right | GreatHall
		'Cave_16_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave16Right'], p) or s.can_reach(el['GreatHall'], 'Location', p),
#		                                                                           Cave16Bottom
		'Cave_16_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave16Bottom'], p),
#		                                                                           Cave16Left | GreatHall
		'Cave_16_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave16Left'], p) or s.can_reach(el['GreatHall'], 'Location', p),
#		                                                                           Cave17Top + swim
		'Cave_17_GAMEPLAY.BP_SCR_LV3M_5000_2'                                     : lambda s : s.has(el['Cave17Top'], p) and s.has(el['swim'], p),
#		                                                                           Cave17Top
		'Cave_17_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave17Top'], p),
#		                                                                           Cave18Left1
		'Cave_18_GAMEPLAY.BP_Interactable_Passive_healpowerup_2'                  : lambda s : s.has(el['Cave18Left1'], p),
#		                                                                           Cave18Left1
		'Cave_18_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave18Left1'], p),
#		                                                                           Cave18Left1 + swim
		'Cave_18_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave18Left1'], p) and s.has(el['swim'], p),
#		                                                                           Cave19Top | Cave19Left
		'Cave_19_GAMEPLAY.BP_e2022_Soldier'                                       : lambda s : s.has(el['Cave19Top'], p) or s.has(el['Cave19Left'], p),
#		                                                                           Archer
		'Cave_19_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                    : lambda s : s.can_reach(el['Archer'], 'Location', p),
#		                                                                           Archer + (hook | LEDGE | HORIZONTAL)
		'Cave_19_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                  : lambda s : s.can_reach(el['Archer'], 'Location', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Cave19Top | Archer
		'Cave_19_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave19Top'], p) or s.can_reach(el['Archer'], 'Location', p),
#		                                                                           Cave19Left | Cave19Top + (HORIZONTAL + LEDGE | claw | 2LEDGE)
		'Cave_19_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave19Left'], p) or s.has(el['Cave19Top'], p) and (macros['HORIZONTAL'](s) and macros['LEDGE'](s) or s.has(el['claw'], p) or macros['2LEDGE'](s)),
#		                                                                           Cave20Top
		'Cave_20_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                   : lambda s : s.has(el['Cave20Top'], p),
#		                                                                           Cave20Top
		'Cave_20_GAMEPLAY.BP_Interactable_Item_Tip4'                              : lambda s : s.has(el['Cave20Top'], p),
#		                                                                           Cave20Top
		'Cave_20_GAMEPLAY.BP_SCR_LV1S_2011_2'                                     : lambda s : s.has(el['Cave20Top'], p),
#		                                                                           Cave20Top | Cave20Bottom + (hook | claw | LEDGE)
		'Cave_20_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave20Top'], p) or s.has(el['Cave20Bottom'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Cave20Bottom | Cave20Left | Cave20Top
		'Cave_20_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave20Bottom'], p) or s.has(el['Cave20Left'], p) or s.has(el['Cave20Top'], p),
#		                                                                           Cave20Left | Cave20Bottom | Cave20Top
		'Cave_20_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Cave20Left'], p) or s.has(el['Cave20Bottom'], p) or s.has(el['Cave20Top'], p),
#		                                                                           Cave21Right | Cave21Left
		'Cave_21_GAMEPLAY.BP_Interactable_Passive_healcountup_2'                  : lambda s : s.has(el['Cave21Right'], p) or s.has(el['Cave21Left'], p),
#		                                                                           Cave21Left | Cave21Right
		'Cave_21_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave21Left'], p) or s.has(el['Cave21Right'], p),
#		                                                                           Cave21Right | Cave21Left
		'Cave_21_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave21Right'], p) or s.has(el['Cave21Left'], p),
#		                                                                           Cave22Right
		'Cave_22_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Cave22Right'], p),
#		                                                                           Cave22Right | Cave22Bottom
		'Cave_22_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Cave22Right'], p) or s.has(el['Cave22Bottom'], p),
#		                                                                           Cave22Left | Cave22Bottom + (2LEDGE | hook | claw | LEDGE + HORIZONTAL)
		'Cave_22_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Cave22Left'], p) or s.has(el['Cave22Bottom'], p) and (macros['2LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Cave22Bottom | Cave22Right | Cave22Left
		'Cave_22_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Cave22Bottom'], p) or s.has(el['Cave22Right'], p) or s.has(el['Cave22Left'], p),
#		                                                                           Cave23Right | Cave23Left
		'Cave_23_GAMEPLAY.BP_e5021_OlderSister'                                   : lambda s : s.has(el['Cave23Right'], p) or s.has(el['Cave23Left'], p),
#		                                                                           Silva
		'Cave_23_GAMEPLAY.BP_Interactable_Item_Tip4'                              : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                                           Silva
		'Cave_23_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                                           Silva
		'Cave_23_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                                           Church01Bottom | Church01Left | Church01Top
		'Church_01_GAMEPLAY.BP_Interactable_WorldTravel'                          : lambda s : s.has(el['Church01Bottom'], p) or s.has(el['Church01Left'], p) or s.has(el['Church01Top'], p),
#		                                                                           Church01Left | Church01Bottom | Church01Top
		'Church_01_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Church01Left'], p) or s.has(el['Church01Bottom'], p) or s.has(el['Church01Top'], p),
#		                                                                           Church02Right
		'Church_02_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                 : lambda s : s.has(el['Church02Right'], p),
#		                                                                           Church02Right
		'Church_02_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Church02Right'], p),
#		                                                                           Church02Top | Church02Right + (djump | champion | silva + dodge)
		'Church_02_GAMEPLAY.BP_Interactable_WorldTravel'                          : lambda s : s.has(el['Church02Top'], p) or s.has(el['Church02Right'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)),
#		                                                                           Church02Right | Church02Top
		'Church_02_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Church02Right'], p) or s.has(el['Church02Top'], p),
#		                                                                           Church03Left
		'Church_03_GAMEPLAY.BP_e5011_YoungerSister'                               : lambda s : s.has(el['Church03Left'], p),
#		                                                                           Church03Left | Church03Right
		'Church_03_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Church03Left'], p) or s.has(el['Church03Right'], p),
#		                                                                           Church03Right | Church03Left
		'Church_03_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Church03Right'], p) or s.has(el['Church03Left'], p),
#		                                                                           Church04Right | Church04Left
		'Church_04_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Church04Right'], p) or s.has(el['Church04Left'], p),
#		                                                                           Church04Left | SaintsPassage
		'Church_04_GAMEPLAY.BP_WorldTravelVolume'                                 : lambda s : s.has(el['Church04Left'], p) or s.can_reach(el['SaintsPassage'], 'Location', p),
#		                                                                           Church04Right | SaintsPassage
		'Church_04_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Church04Right'], p) or s.can_reach(el['SaintsPassage'], 'Location', p),
#		                                                                           Church05Top | CathedralCloister + LEDGE
		'Church_05_GAMEPLAY.BP_Interactable_Passive_MaxHPUp_Lv1_2'                : lambda s : s.has(el['Church05Top'], p) or s.can_reach(el['CathedralCloister'], 'Location', p) and macros['LEDGE'](s),
#		                                                                           CathedralCloister
		'Church_05_GAMEPLAY.BP_Interactable_WorldTravel'                          : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p),
#		                                                                           CathedralCloister
		'Church_05_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p),
#		                                                                           Church05Right | Church05Bottom | Church05Top
		'CathedralCloister'                                                       : lambda s : s.has(el['Church05Right'], p) or s.has(el['Church05Bottom'], p) or s.has(el['Church05Top'], p),
#		                                                                           CathedralCloister + claw
		'Church_05_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p) and s.has(el['claw'], p),
#		                                                                           Church06Left | Church06Right
		'Church_06_GAMEPLAY.BP_WorldTravelVolume'                                 : lambda s : s.has(el['Church06Left'], p) or s.has(el['Church06Right'], p),
#		                                                                           Church06Right | Church06Left + (LEDGE | claw)
		'Church_06_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Church06Right'], p) or s.has(el['Church06Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Church07Right
		'Church_07_GAMEPLAY.BP_e2012_Slime_Unique'                                : lambda s : s.has(el['Church07Right'], p),
#		                                                                           Youth + slam
		'Church_07_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                   : lambda s : s.can_reach(el['Youth'], 'Location', p) and s.has(el['slam'], p),
#		                                                                           Church07Left | Youth + (LEDGE | claw)
		'Church_07_GAMEPLAY.BP_WorldTravelVolume_3'                               : lambda s : s.has(el['Church07Left'], p) or s.can_reach(el['Youth'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Church07Right | Church07Left + (LEDGE | claw) | Youth
		'Church_07_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Church07Right'], p) or s.has(el['Church07Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or s.can_reach(el['Youth'], 'Location', p),
#		                                                                           Crossroads + swim
		'Church_08_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.can_reach(el['Crossroads'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Church08Top | Church08Bottom | Church08Left
		'Church_08_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Church08Top'], p) or s.has(el['Church08Bottom'], p) or s.has(el['Church08Left'], p),
#		                                                                           Crossroads
		'Church_08_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                                           Crossroads
		'Church_08_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                                           Crossroads
		'Church_08_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                                           Church09Bottom | Church09Top
		'Church_09_GAMEPLAY.BP_e2092_Priest'                                      : lambda s : s.has(el['Church09Bottom'], p) or s.has(el['Church09Top'], p),
#		                                                                           Church09Bottom + CHARGE + (LEDGE + claw | 3LEDGE)
		'Church_09_GAMEPLAY.BP_Interactable_Passive_JumpHeightUp_2'               : lambda s : s.has(el['Church09Bottom'], p) and macros['CHARGE'](s) and (macros['LEDGE'](s) and s.has(el['claw'], p) or macros['3LEDGE'](s)),
#		                                                                           Chief
		'Church_09_GAMEPLAY.BP_SCR_LV2M_2001_2'                                   : lambda s : s.can_reach(el['Chief'], 'Location', p),
#		                                                                           Church09Bottom | Church09Top
		'Church_09_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Church09Bottom'], p) or s.has(el['Church09Top'], p),
#		                                                                           Chief
		'Church_09_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.can_reach(el['Chief'], 'Location', p),
#		                                                                           Church09Bottom + hook
		'Church_09_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Church09Bottom'], p) and s.has(el['hook'], p),
#		                                                                           Church10Left | Church10Right
		'Church_10_GAMEPLAY.BP_Interactable_Item_Tip_2'                           : lambda s : s.has(el['Church10Left'], p) or s.has(el['Church10Right'], p),
#		                                                                           Cellar
		'Church_10_GAMEPLAY.BP_Interactable_Item_Tip2'                            : lambda s : s.can_reach(el['Cellar'], 'Location', p),
#		                                                                           Church10Left | Cellar
		'Church_10_GAMEPLAY.BP_WorldTravelVolume_4'                               : lambda s : s.has(el['Church10Left'], p) or s.can_reach(el['Cellar'], 'Location', p),
#		                                                                           Church10Right | Cellar
		'Church_10_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Church10Right'], p) or s.can_reach(el['Cellar'], 'Location', p),
#		                                                                           Church11Left
		'Church_11_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Church11Left'], p),
#		                                                                           Church11Top
		'Church_11_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Church11Top'], p),
#		                                                                           Church11Top | Church11Left
		'Church_11_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Church11Top'], p) or s.has(el['Church11Left'], p),
#		                                                                           Church11Left
		'Church_11_GAMEPLAY.BP_WorldTravelVolume_4'                               : lambda s : s.has(el['Church11Left'], p),
#		                                                                           Church12Right
		'Church_12_GAMEPLAY.BP_Interactable_Item_Tip1'                            : lambda s : s.has(el['Church12Right'], p),
#		                                                                           Church12Right | Start
		'Church_12_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Church12Right'], p) or s.can_reach(el['Start'], 'Location', p),
#		                                                                           Church12Bottom | Start + (unlock + ( djump | champion | silva + dodge | claw ))
		'Church_12_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Church12Bottom'], p) or s.can_reach(el['Start'], 'Location', p) and (s.has(el['unlock'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p) or s.has(el['claw'], p))),
#		                                                                           Church13Top
		'Church_13_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Church13Top'], p),
#		                                                                           Church13Top
		'Church_13_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Church13Top'], p),
#		                                                                           Church14Bottom
		'Church_14_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                  : lambda s : s.has(el['Church14Bottom'], p),
#		                                                                           Church14Bottom
		'Church_14_GAMEPLAY.BP_Interactable_Item_Tip5'                            : lambda s : s.has(el['Church14Bottom'], p),
#		                                                                           Church14Bottom
		'Church_14_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Church14Bottom'], p),
#		                                                                           Forest01Top | Forest01Right + (LEDGE | claw)
		'Forest_01_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Forest01Top'], p) or s.has(el['Forest01Right'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest01Right | Forest01Top
		'Forest_01_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Forest01Right'], p) or s.has(el['Forest01Top'], p),
#		                                                                           Forest02Left | Forest02Right2 + hook
		'Forest_02_GAMEPLAY.BP_SCR_LV1S_2130_2'                                   : lambda s : s.has(el['Forest02Left'], p) or s.has(el['Forest02Right2'], p) and s.has(el['hook'], p),
#		                                                                           Forest02Left | Forest02Right1
		'Forest_02_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Forest02Left'], p) or s.has(el['Forest02Right1'], p),
#		                                                                           Forest02Right1 | Forest02Left | Forest02Right2 + (claw | LEDGE)
		'Forest_02_GAMEPLAY.BP_WorldTravelVolume6'                                : lambda s : s.has(el['Forest02Right1'], p) or s.has(el['Forest02Left'], p) or s.has(el['Forest02Right2'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Forest02Right2 | Forest02Left
		'Forest_02_GAMEPLAY.BP_WorldTravelVolume7'                                : lambda s : s.has(el['Forest02Right2'], p) or s.has(el['Forest02Left'], p),
#		                                                                           Forest03Left + swim
		'Forest_03_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Forest03Left'], p) and s.has(el['swim'], p),
#		                                                                           Forest03Left + swim
		'Forest_03_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                   : lambda s : s.has(el['Forest03Left'], p) and s.has(el['swim'], p),
#		                                                                           Forest03Right | Forest03Left + (claw | LEDGE | HORIZONTAL)
		'Forest_03_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest03Right'], p) or s.has(el['Forest03Left'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Forest03Left | Forest03Right
		'Forest_03_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Forest03Left'], p) or s.has(el['Forest03Right'], p),
#		                                                                           Forest04Right
		'Forest_04_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                 : lambda s : s.has(el['Forest04Right'], p),
#		                                                                           Forest04Left + (LEDGE | claw + HORIZONTAL)
		'Forest_04_GAMEPLAY.BP_Interactable_Passive_dmgup_swimming_2'             : lambda s : s.has(el['Forest04Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                                           Forest04Left + (slam + LEDGE)
		'Forest_04_GAMEPLAY.BP_SCR_LV1S_2100_2'                                   : lambda s : s.has(el['Forest04Left'], p) and (s.has(el['slam'], p) and macros['LEDGE'](s)),
#		                                                                           Forest04Right | Forest04Left +  (LEDGE | claw | HORIZONTAL + swim)
		'Forest_04_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest04Right'], p) or s.has(el['Forest04Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or macros['HORIZONTAL'](s) and s.has(el['swim'], p)),
#		                                                                           Forest04Left | Forest04Right + (LEDGE | claw)
		'Forest_04_GAMEPLAY.BP_WorldTravelVolume4'                                : lambda s : s.has(el['Forest04Left'], p) or s.has(el['Forest04Right'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest05Right | Forest05Left | Forest05Top
		'Forest_05_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Forest05Right'], p) or s.has(el['Forest05Left'], p) or s.has(el['Forest05Top'], p),
#		                                                                           Forest05Right | DryadLake
		'Forest_05_GAMEPLAY.BP_WorldTravelVolume5'                                : lambda s : s.has(el['Forest05Right'], p) or s.can_reach(el['DryadLake'], 'Location', p),
#		                                                                           Forest05Left | DryadLake
		'Forest_05_GAMEPLAY.BP_WorldTravelVolume6'                                : lambda s : s.has(el['Forest05Left'], p) or s.can_reach(el['DryadLake'], 'Location', p),
#		                                                                           Forest05Top | DryadLake + LEDGE
		'Forest_05_GAMEPLAY.BP_WorldTravelVolume7'                                : lambda s : s.has(el['Forest05Top'], p) or s.can_reach(el['DryadLake'], 'Location', p) and macros['LEDGE'](s),
#		                                                                           Forest06Bottom + LEDGE
		'Forest_06_GAMEPLAY.BP_e2122_Fungus'                                      : lambda s : s.has(el['Forest06Bottom'], p) and macros['LEDGE'](s),
#		                                                                           Forest06Bottom + LEDGE
		'Forest_06_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Forest06Bottom'], p) and macros['LEDGE'](s),
#		                                                                           Forest06Bottom + (hook | LEDGE + slam | 2LEDGE | LEDGE + HORIZONTAL)
		'Forest_06_GAMEPLAY.BP_SCR_LV2M_2120_3'                                   : lambda s : s.has(el['Forest06Bottom'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['slam'], p) or macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Forest06Bottom
		'Forest_06_GAMEPLAY.BP_WorldTravelVolume8'                                : lambda s : s.has(el['Forest06Bottom'], p),
#		                                                                           (Forest07Left | Forest07Bottom) + (LEDGE | hook | HORIZONTAL | claw)
		'Forest_07_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                 : lambda s : (s.has(el['Forest07Left'], p) or s.has(el['Forest07Bottom'], p)) and (macros['LEDGE'](s) or s.has(el['hook'], p) or macros['HORIZONTAL'](s) or s.has(el['claw'], p)),
#		                                                                           Forest07Right + (hook | claw +  LEDGE)
		'Forest_07_GAMEPLAY.BP_SCR_LV1S_2121_1'                                   : lambda s : s.has(el['Forest07Right'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and macros['LEDGE'](s)),
#		                                                                           Forest07Left | Forest07Right
		'Forest_07_GAMEPLAY.BP_SCR_LV1S_2130_2'                                   : lambda s : s.has(el['Forest07Left'], p) or s.has(el['Forest07Right'], p),
#		                                                                           Forest07Right | Forest07Left + (dodge + (LEDGE | dash) | 2LEDGE | hook | sinner | djump + dash)
		'Forest_07_GAMEPLAY.BP_WorldTravelVolume10_2'                             : lambda s : s.has(el['Forest07Right'], p) or s.has(el['Forest07Left'], p) and (s.has(el['dodge'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p)) or macros['2LEDGE'](s) or s.has(el['hook'], p) or s.has(el['sinner'], p) or s.has(el['djump'], p) and s.has(el['dash'], p)),
#		                                                                           Forest07Bottom | Forest07Left
		'Forest_07_GAMEPLAY.BP_WorldTravelVolume12'                               : lambda s : s.has(el['Forest07Bottom'], p) or s.has(el['Forest07Left'], p),
#		                                                                           Forest07Left | Forest07Bottom + LEDGE | Forest07Right + (LEDGE | hook | HORIZONTAL | dash)
		'Forest_07_GAMEPLAY.BP_WorldTravelVolume9_1'                              : lambda s : s.has(el['Forest07Left'], p) or s.has(el['Forest07Bottom'], p) and macros['LEDGE'](s) or s.has(el['Forest07Right'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Forest07Top | Forest07Left + LEDGE
		'Forest_07_GEO.BP_WorldTravelVolume11'                                    : lambda s : s.has(el['Forest07Top'], p) or s.has(el['Forest07Left'], p) and macros['LEDGE'](s),
#		                                                                           Forest08Top + (LEDGE | hook | claw + HORIZONTAL)
		'Forest_08_GAMEPLAY.BP_Interactable_Passive_Treasure_2'                   : lambda s : s.has(el['Forest08Top'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                                           ManisasRing + (2LEDGE | LEDGE + HORIZONTAL | claw + sinner | hook)
		'Forest_08_GAMEPLAY.BP_Interactable_Passive_Treasure2'                    : lambda s : s.can_reach(el['ManisasRing'], 'Location', p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or s.has(el['claw'], p) and s.has(el['sinner'], p) or s.has(el['hook'], p)),
#		                                                                           Forest08Top + (LEDGE | HORIZONTAL | dash)
		'Forest_08_GAMEPLAY.BP_SCR_LV2M_2120_1'                                   : lambda s : s.has(el['Forest08Top'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Forest08Top | Forest08Right + (LEDGE | claw)
		'Forest_08_GAMEPLAY.BP_WorldTravelVolume12'                               : lambda s : s.has(el['Forest08Top'], p) or s.has(el['Forest08Right'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest08Right | Forest08Top + (LEDGE | hook | claw)
		'Forest_08_GAMEPLAY.BP_WorldTravelVolume13'                               : lambda s : s.has(el['Forest08Right'], p) or s.has(el['Forest08Top'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p)),
#		                                                                           Forest10Left + swim + (LEDGE | claw)
		'Forest_09_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                  : lambda s : s.has(el['Forest10Left'], p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest10Left + swim + (LEDGE | claw)
		'Forest_09_GAMEPLAY.BP_Interactable_Item_Tip1'                            : lambda s : s.has(el['Forest10Left'], p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest09Top | Forest09Left + swim
		'Forest_09_GAMEPLAY.BP_Interactable_WorldTravel_2'                        : lambda s : s.has(el['Forest09Top'], p) or s.has(el['Forest09Left'], p) and s.has(el['swim'], p),
#		                                                                           (Forest09Top | Forest09Left) + swim
		'Forest_09_GAMEPLAY.BP_SCR_LV2S_2130_2'                                   : lambda s : (s.has(el['Forest09Top'], p) or s.has(el['Forest09Left'], p)) and s.has(el['swim'], p),
#		                                                                           Forest09Left | Forest09Top + swim + (LEDGE | claw)
		'Forest_09_GAMEPLAY.BP_WorldTravelVolume13'                               : lambda s : s.has(el['Forest09Left'], p) or s.has(el['Forest09Top'], p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Forest10Bottom2 | WitchsHermitage
		'Forest_10_DESIGN.BP_Interactable_WorldTravel10'                          : lambda s : s.has(el['Forest10Bottom2'], p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                                           Forest10Bottom1 | WitchsHermitage
		'Forest_10_DESIGN.BP_Interactable_WorldTravel9'                           : lambda s : s.has(el['Forest10Bottom1'], p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                                           Forest10Bottom2 | Forest10Bottom1 | Forest10Left | Forest10Right
		'Forest_10_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Forest10Bottom2'], p) or s.has(el['Forest10Bottom1'], p) or s.has(el['Forest10Left'], p) or s.has(el['Forest10Right'], p),
#		                                                                           Forest10Left | WitchsHermitage
		'Forest_10_GAMEPLAY.BP_WorldTravelVolume12'                               : lambda s : s.has(el['Forest10Left'], p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                                           Forest10Right | WitchsHermitage
		'Forest_10_GAMEPLAY.BP_WorldTravelVolume13'                               : lambda s : s.has(el['Forest10Right'], p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                                           Forest11Top
		'Forest_11_GAMEPLAY.BP_e2132_Mandrake'                                    : lambda s : s.has(el['Forest11Top'], p),
#		                                                                           Forest11Top
		'Forest_11_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                    : lambda s : s.has(el['Forest11Top'], p),
#		                                                                           Forest11Top
		'Forest_11_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                : lambda s : s.has(el['Forest11Top'], p),
#		                                                                           Forest11Right + (LEDGE | HORIZONTAL | dash)
		'Forest_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Forest11Right'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Forest11Top | Forest11Right
		'Forest_11_GAMEPLAY.BP_Interactable_WorldTravel11'                        : lambda s : s.has(el['Forest11Top'], p) or s.has(el['Forest11Right'], p),
#		                                                                           Forest11Right + (LEDGE + claw | hook | 2HORIZONTAL + (dash | djump | silva))
		'Forest_11_GAMEPLAY.BP_SCR_LV1M_2120_2'                                   : lambda s : s.has(el['Forest11Right'], p) and (macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p) or macros['2HORIZONTAL'](s) and (s.has(el['dash'], p) or s.has(el['djump'], p) or s.has(el['silva'], p))),
#		                                                                           Forest11Right + swim
		'Forest_11_GAMEPLAY.BP_SCR_LV1S_2130_2'                                   : lambda s : s.has(el['Forest11Right'], p) and s.has(el['swim'], p),
#		                                                                           Forest11Right | Forest11Top + swim
		'Forest_11_GAMEPLAY.BP_WorldTravelVolume12'                               : lambda s : s.has(el['Forest11Right'], p) or s.has(el['Forest11Top'], p) and s.has(el['swim'], p),
#		                                                                           Forest12Left + (LEDGE | claw | hook)
		'Forest_12_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                 : lambda s : s.has(el['Forest12Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                                           Forest12Bottom | Forest12Right
		'Forest_12_GAMEPLAY.BP_SCR_LV1M_2131_3'                                   : lambda s : s.has(el['Forest12Bottom'], p) or s.has(el['Forest12Right'], p),
#		                                                                           Forest12Left | Forest12Bottom + (LEDGE | hook)
		'Forest_12_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Forest12Left'], p) or s.has(el['Forest12Bottom'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Forest12Bottom | Forest12Right  | Forest12Left + (LEDGE | hook)
		'Forest_12_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Forest12Bottom'], p) or s.has(el['Forest12Right'], p) or s.has(el['Forest12Left'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Forest12Right | Forest12Left + (claw + (djump | champion) | claw + LEDGE + (HORIZONTAL | dash) | silva + djump | LEDGE + sinner | 2LEDGE + HORIZONTAL) | Forest12Bottom + hook
		'Forest_12_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest12Right'], p) or s.has(el['Forest12Left'], p) and (s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p)) or s.has(el['claw'], p) and macros['LEDGE'](s) and (macros['HORIZONTAL'](s) or s.has(el['dash'], p)) or s.has(el['silva'], p) and s.has(el['djump'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s)) or s.has(el['Forest12Bottom'], p) and s.has(el['hook'], p),
#		                                                                           Forest13Top
		'Forest_13_GAMEPLAY.BP_SCR_LV1S_2130_3'                                   : lambda s : s.has(el['Forest13Top'], p),
#		                                                                           Forest13Top | Forest13Bottom
		'Forest_13_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Forest13Top'], p) or s.has(el['Forest13Bottom'], p),
#		                                                                           Forest13Bottom | Forest13Top + LEDGE
		'Forest_13_GAMEPLAY.BP_WorldTravelVolume2'                                : lambda s : s.has(el['Forest13Bottom'], p) or s.has(el['Forest13Top'], p) and macros['LEDGE'](s),
#		                                                                           Forest13Right | Forest13Top + claw + unlock + (LEDGE + HORIZONTAL | 2LEDGE)
		'Forest_13_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest13Right'], p) or s.has(el['Forest13Top'], p) and s.has(el['claw'], p) and s.has(el['unlock'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)),
#		                                                                           Forest14Bottom | Forest14Top | Forest14Left
		'Forest_14_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Forest14Bottom'], p) or s.has(el['Forest14Top'], p) or s.has(el['Forest14Left'], p),
#		                                                                           CovenHalls
		'Forest_14_GAMEPLAY.BP_WorldTravelVolume10'                               : lambda s : s.can_reach(el['CovenHalls'], 'Location', p),
#		                                                                           CovenHalls
		'Forest_14_GAMEPLAY.BP_WorldTravelVolume11'                               : lambda s : s.can_reach(el['CovenHalls'], 'Location', p),
#		                                                                           Forest14Left | CovenHalls + swim
		'Forest_14_GAMEPLAY.BP_WorldTravelVolume12'                               : lambda s : s.has(el['Forest14Left'], p) or s.can_reach(el['CovenHalls'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Forest15Top
		'Forest_15_GAMEPLAY.BP_e5040_Witch'                                       : lambda s : s.has(el['Forest15Top'], p),
#		                                                                           Forest15Top
		'Forest_15_GAMEPLAY.BP_WorldTravelVolume_2'                               : lambda s : s.has(el['Forest15Top'], p),
#		                                                                           Forest16Left
		'Forest_16_GAMEPLAY.BP_Interactable_Item_Tip3'                            : lambda s : s.has(el['Forest16Left'], p),
#		                                                                           Forest16Left
		'Forest_16_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Forest16Left'], p),
#		                                                                           Forest16Left
		'Forest_16_GAMEPLAY.BP_SCR_LV1LL_0000_2'                                  : lambda s : s.has(el['Forest16Left'], p),
#		                                                                           Forest16Left
		'Forest_16_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest16Left'], p),
#		                                                                           Forest17Left + (claw | LEDGE)
		'Forest_17_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_Treasure_2'           : lambda s : s.has(el['Forest17Left'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Forest17Left + (claw | LEDGE + hook | silva + djump)
		'Forest_17_GAMEPLAY.BP_Interactable_Item_Tip4'                            : lambda s : s.has(el['Forest17Left'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) and s.has(el['hook'], p) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                                           Forest17Left + (claw | LEDGE)
		'Forest_17_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                  : lambda s : s.has(el['Forest17Left'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                                           Forest17Left
		'Forest_17_GAMEPLAY.BP_WorldTravelVolume3'                                : lambda s : s.has(el['Forest17Left'], p),
#		                                                                           Forest17Left
		'Forest_17_Map.BP_Interactable_Item_Tip5'                                 : lambda s : s.has(el['Forest17Left'], p),
#		                                                                           Fort01Left1 | Fort01Right + (LEDGE | hook)
		'Fort_01_GAMEPLAY.BP_e2192_Gargoyle'                                      : lambda s : s.has(el['Fort01Left1'], p) or s.has(el['Fort01Right'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Fort01Left1
		'Fort_01_GAMEPLAY.BP_SCR_LV1M_2190_2'                                     : lambda s : s.has(el['Fort01Left1'], p),
#		                                                                           Fort01Right | Fort01Left1 | Fort01Left2
		'Fort_01_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort01Right'], p) or s.has(el['Fort01Left1'], p) or s.has(el['Fort01Left2'], p),
#		                                                                           Fort01Left2 | Fort01Right + swim
		'Fort_01_GAMEPLAY.BP_WorldTravelVolume2'                                  : lambda s : s.has(el['Fort01Left2'], p) or s.has(el['Fort01Right'], p) and s.has(el['swim'], p),
#		                                                                           Fort01Left1 | Sentinel + hook
		'Fort_01_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort01Left1'], p) or s.can_reach(el['Sentinel'], 'Location', p) and s.has(el['hook'], p),
#		                                                                           Fort02Left
		'Fort_02_GAMEPLAY.BP_SCR_LV1S_2021_2'                                     : lambda s : s.has(el['Fort02Left'], p),
#		                                                                           Fort02Right
		'Fort_02_GAMEPLAY.BP_SCR_LV2S_2021_2'                                     : lambda s : s.has(el['Fort02Right'], p),
#		                                                                           Fort02Right | Fort02Left + (LEDGE + HORIZONTAL | 2HORIZONTAL | djump + (silva | champion))
		'Fort_02_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort02Right'], p) or s.has(el['Fort02Left'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or s.has(el['djump'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p))),
#		                                                                           Fort02Left | Fort02Right + (LEDGE + HORIZONTAL | 2HORIZONTAL | 2LEDGE | sinner | dash + LEDGE | dash + dodge)
		'Fort_02_GAMEPLAY.BP_WorldTravelVolume3_8'                                : lambda s : s.has(el['Fort02Left'], p) or s.has(el['Fort02Right'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or macros['2LEDGE'](s) or s.has(el['sinner'], p) or s.has(el['dash'], p) and macros['LEDGE'](s) or s.has(el['dash'], p) and s.has(el['dodge'], p)),
#		                                                                           Fort03Right | Fort03Left1 | Fort03Left2 | Fort03Top
		'Fort_03_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort03Right'], p) or s.has(el['Fort03Left1'], p) or s.has(el['Fort03Left2'], p) or s.has(el['Fort03Top'], p),
#		                                                                           BastionGates
		'Fort_03_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.can_reach(el['BastionGates'], 'Location', p),
#		                                                                           BastionGates + (hook | LEDGE)
		'Fort_03_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.can_reach(el['BastionGates'], 'Location', p) and (s.has(el['hook'], p) or macros['LEDGE'](s)),
#		                                                                           BastionGates
		'Fort_03_GAMEPLAY.BP_WorldTravelVolume3_8'                                : lambda s : s.can_reach(el['BastionGates'], 'Location', p),
#		                                                                           BastionGates + claw
		'Fort_03_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.can_reach(el['BastionGates'], 'Location', p) and s.has(el['claw'], p),
#		                                                                           Fort04Left + (CHARGE + (LEDGE | claw | HORIZONTAL))
		'Fort_04_GAMEPLAY.BP_SCR_LV1L_2230_8'                                     : lambda s : s.has(el['Fort04Left'], p) and (macros['CHARGE'](s) and (macros['LEDGE'](s) or s.has(el['claw'], p) or macros['HORIZONTAL'](s))),
#		                                                                           Fort04Top | Fort04Left + LEDGE
		'Fort_04_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort04Top'], p) or s.has(el['Fort04Left'], p) and macros['LEDGE'](s),
#		                                                                           Fort04Left | Fort04Top
		'Fort_04_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort04Left'], p) or s.has(el['Fort04Top'], p),
#		                                                                           Fort05Right + LEDGE
		'Fort_05_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                   : lambda s : s.has(el['Fort05Right'], p) and macros['LEDGE'](s),
#		                                                                           Fort05Bottom2 + (LEDGE + (hook | claw))
		'Fort_05_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                  : lambda s : s.has(el['Fort05Bottom2'], p) and (macros['LEDGE'](s) and (s.has(el['hook'], p) or s.has(el['claw'], p))),
#		                                                                           Fort05Bottom2 + LEDGE + slam  | Fort05Bottom1
		'Fort_05_GAMEPLAY.BP_SCR_LV1S_2020_6'                                     : lambda s : s.has(el['Fort05Bottom2'], p) and macros['LEDGE'](s) and s.has(el['slam'], p) or s.has(el['Fort05Bottom1'], p),
#		                                                                           Fort05Bottom2 | Fort05Right
		'Fort_05_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort05Bottom2'], p) or s.has(el['Fort05Right'], p),
#		                                                                           Fort05Right | Fort05Bottom2 + LEDGE
		'Fort_05_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort05Right'], p) or s.has(el['Fort05Bottom2'], p) and macros['LEDGE'](s),
#		                                                                           Fort05Bottom1 | Fort05Bottom2 + LEDGE
		'Fort_05_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort05Bottom1'], p) or s.has(el['Fort05Bottom2'], p) and macros['LEDGE'](s),
#		                                                                           Fort05Bottom2 + LEDGE + claw
		'Fort_05_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort05Bottom2'], p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                                           Fort06Right + (LEDGE +  claw)
		'Fort_06_GAMEPLAY.BP_SCR_LV1M_2190_4'                                     : lambda s : s.has(el['Fort06Right'], p) and (macros['LEDGE'](s) and s.has(el['claw'], p)),
#		                                                                           Fort06Left | Fort06Bottom | Fort06Right + (LEDGE | HORIZONTAL | dash)
		'Fort_06_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort06Left'], p) or s.has(el['Fort06Bottom'], p) or s.has(el['Fort06Right'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Fort06Right | Fort06Left + (LEDGE | HORIZONTAL | dash)
		'Fort_06_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort06Right'], p) or s.has(el['Fort06Left'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Fort06Bottom | Fort06Left | Fort06Right
		'Fort_06_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort06Bottom'], p) or s.has(el['Fort06Left'], p) or s.has(el['Fort06Right'], p),
#		                                                                           Fort07Bottom1 + (LEDGE | claw)
		'Fort_07_GAMEPLAY.BP_SCR_LV1S_2021_1'                                     : lambda s : s.has(el['Fort07Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Fort07Right | Fort07Bottom1 | Fort07Top | Fort07Bottom2  + claw
		'Fort_07_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort07Right'], p) or s.has(el['Fort07Bottom1'], p) or s.has(el['Fort07Top'], p) or s.has(el['Fort07Bottom2'], p) and s.has(el['claw'], p),
#		                                                                           Fort07Right | Fort07Top
		'Fort_07_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort07Right'], p) or s.has(el['Fort07Top'], p),
#		                                                                           Fort07Left | Fort07Top + LEDGE
		'Fort_07_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort07Left'], p) or s.has(el['Fort07Top'], p) and macros['LEDGE'](s),
#		                                                                           Fort07Top | Fort07Bottom1 | Fort07Left + (LEDGE | claw) | Fort07Right
		'Fort_07_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort07Top'], p) or s.has(el['Fort07Bottom1'], p) or s.has(el['Fort07Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or s.has(el['Fort07Right'], p),
#		                                                                           Fort07Bottom2 | Fort07Bottom1 + claw
		'Fort_07_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort07Bottom2'], p) or s.has(el['Fort07Bottom1'], p) and s.has(el['claw'], p),
#		                                                                           Fort08Left
		'Fort_08_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort08Left'], p),
#		                                                                           Fort08Left | SecondSpireChamber
		'Fort_08_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort08Left'], p) or s.can_reach(el['SecondSpireChamber'], 'Location', p),
#		                                                                           Fort09Left
		'Fort_09_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort09Left'], p),
#		                                                                           Fort09Left + CHARGE
		'Fort_09_GAMEPLAY.BP_Interactable_Passive_dmgcut_Lv3_2'                   : lambda s : s.has(el['Fort09Left'], p) and macros['CHARGE'](s),
#		                                                                           Fort09Top1
		'Fort_09_GAMEPLAY.BP_SCR_LV1S_2020_2'                                     : lambda s : s.has(el['Fort09Top1'], p),
#		                                                                           Fort09Top2
		'Fort_09_GAMEPLAY.BP_SCR_LV2M_2190_3'                                     : lambda s : s.has(el['Fort09Top2'], p),
#		                                                                           Fort09Right | Fort09Top1 + claw
		'Fort_09_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort09Right'], p) or s.has(el['Fort09Top1'], p) and s.has(el['claw'], p),
#		                                                                           Fort09Left | Fort09Right | Fort09Top1 | Fort09Top2
		'Fort_09_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort09Left'], p) or s.has(el['Fort09Right'], p) or s.has(el['Fort09Top1'], p) or s.has(el['Fort09Top2'], p),
#		                                                                           Fort09Top1 | Fort09Left + (LEDGE | hook)
		'Fort_09_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort09Top1'], p) or s.has(el['Fort09Left'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Fort09Top2 | Fort09Right + LEDGE + claw
		'Fort_09_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort09Top2'], p) or s.has(el['Fort09Right'], p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                                           Courtyard + claw + LEDGE
		'Fort_10_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                      : lambda s : s.can_reach(el['Courtyard'], 'Location', p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                                           Fort10Right | Fort10Top
		'Fort_10_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort10Right'], p) or s.has(el['Fort10Top'], p),
#		                                                                           Courtyard
		'Fort_10_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.can_reach(el['Courtyard'], 'Location', p),
#		                                                                           Courtyard + claw + LEDGE
		'Fort_10_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.can_reach(el['Courtyard'], 'Location', p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                                           slam + swim + (Fort11Stagnant | Fort11Bottom + (LEDGE + (sinner | dodge + claw) | 2LEDGE))
		'Fort_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                    : lambda s : s.has(el['slam'], p) and s.has(el['swim'], p) and (s.can_reach(el['Fort11Stagnant'], 'Location', p) or s.has(el['Fort11Bottom'], p) and (macros['LEDGE'](s) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['claw'], p)) or macros['2LEDGE'](s))),
#		                                                                           Fort11Top2 | Fort11Bottom + (LEDGE + (sinner | dodge + claw) | 2LEDGE) + (hook | 2LEDGE + claw | 3LEDGE)
		'Fort_11_GAMEPLAY.BP_SCR_LV1M_2190_4'                                     : lambda s : s.has(el['Fort11Top2'], p) or s.has(el['Fort11Bottom'], p) and (macros['LEDGE'](s) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['claw'], p)) or macros['2LEDGE'](s)) and (s.has(el['hook'], p) or macros['2LEDGE'](s) and s.has(el['claw'], p) or macros['3LEDGE'](s)),
#		                                                                           Fort11Bottom | Fort11Left | Fort11Top1 | Fort11Top2
		'Fort_11_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort11Bottom'], p) or s.has(el['Fort11Left'], p) or s.has(el['Fort11Top1'], p) or s.has(el['Fort11Top2'], p),
#		                                                                           Fort11Left | Fort11Bottom + LEDGE | Fort11Top1 + (HORIZONTAL | LEDGE | dash)
		'Fort_11_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort11Left'], p) or s.has(el['Fort11Bottom'], p) and macros['LEDGE'](s) or s.has(el['Fort11Top1'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['dash'], p)),
#		                                                                           Fort11Top1 | Fort11Left + (claw | LEDGE | HORIZONTAL | dash)
		'Fort_11_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort11Top1'], p) or s.has(el['Fort11Left'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Fort11Top2 + claw | Fort11Stagnant + claw
		'Fort_11_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort11Top2'], p) and s.has(el['claw'], p) or s.can_reach(el['Fort11Stagnant'], 'Location', p) and s.has(el['claw'], p),
#		                                                                           Fort12HP + CHARGE
		'Fort_12_GAMEPLAY.BP_e2232_Dragon'                                        : lambda s : s.can_reach(el['Fort12HP'], 'Location', p) and macros['CHARGE'](s),
#		                                                                           Fort12Top | Fort12Right  + (claw + (LEDGE + HORIZONTAL | 2LEDGE) | 3LEDGE)
		'Fort_12_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_7'                      : lambda s : s.has(el['Fort12Top'], p) or s.has(el['Fort12Right'], p) and (s.has(el['claw'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)) or macros['3LEDGE'](s)),
#		                                                                           Fort12Right | Fort12Left
		'Fort_12_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort12Right'], p) or s.has(el['Fort12Left'], p),
#		                                                                           Fort12Top + LEDGE + claw
		'Fort_12_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort12Top'], p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                                           Fort12Left | Fort12Right | Fort12Top
		'Fort_12_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort12Left'], p) or s.has(el['Fort12Right'], p) or s.has(el['Fort12Top'], p),
#		                                                                           Fort13Left
		'Fort_13_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                      : lambda s : s.has(el['Fort13Left'], p),
#		                                                                           Fort13Bottom1 + claw + LEDGE | Fort13Top
		'Fort_13_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                  : lambda s : s.has(el['Fort13Bottom1'], p) and s.has(el['claw'], p) and macros['LEDGE'](s) or s.has(el['Fort13Top'], p),
#		                                                                           Fort13Bottom1 | Fort13Bottom2 | Fort13Left | Fort13Top
		'Fort_13_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort13Bottom1'], p) or s.has(el['Fort13Bottom2'], p) or s.has(el['Fort13Left'], p) or s.has(el['Fort13Top'], p),
#		                                                                           Fort13Bottom2 | Fort13Top | Fort13Bottom1
		'Fort_13_GAMEPLAY.BP_WorldTravelVolume2'                                  : lambda s : s.has(el['Fort13Bottom2'], p) or s.has(el['Fort13Top'], p) or s.has(el['Fort13Bottom1'], p),
#		                                                                           Fort13Left | Fort13Bottom1 + (LEDGE | claw)
		'Fort_13_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort13Left'], p) or s.has(el['Fort13Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Fort13Top + claw + LEDGE | Fort13Bottom1 + claw + LEDGE
		'Fort_13_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort13Top'], p) and s.has(el['claw'], p) and macros['LEDGE'](s) or s.has(el['Fort13Bottom1'], p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                                           Fort14Right + hook + slam + unlock + swim
		'Fort_14_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort14Right'], p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                                           Fort14Right + hook + slam + unlock + swim
		'Fort_14_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                    : lambda s : s.has(el['Fort14Right'], p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                                           Fort14Bottom + CHARGE
		'Fort_14_GAMEPLAY.BP_SCR_LV1L_2231_2'                                     : lambda s : s.has(el['Fort14Bottom'], p) and macros['CHARGE'](s),
#		                                                                           Fort14Right + hook + slam + unlock + swim
		'Fort_14_GAMEPLAY.BP_SCR_LV1LL_0000_2'                                    : lambda s : s.has(el['Fort14Right'], p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                                           Fort14Right | Fort14Left | Fort14Bottom
		'Fort_14_GAMEPLAY.BP_SCR_LV2S_2020_3'                                     : lambda s : s.has(el['Fort14Right'], p) or s.has(el['Fort14Left'], p) or s.has(el['Fort14Bottom'], p),
#		                                                                           Fort14Left | Fort14Right + (dash | HORIZONTAL | LEDGE)
		'Fort_14_GAMEPLAY.BP_WorldTravelVolume_0'                                 : lambda s : s.has(el['Fort14Left'], p) or s.has(el['Fort14Right'], p) and (s.has(el['dash'], p) or macros['HORIZONTAL'](s) or macros['LEDGE'](s)),
#		                                                                           Fort14Right | Fort14Left | Fort14Bottom
		'Fort_14_GAMEPLAY.BP_WorldTravelVolume2_1'                                : lambda s : s.has(el['Fort14Right'], p) or s.has(el['Fort14Left'], p) or s.has(el['Fort14Bottom'], p),
#		                                                                           Fort14Bottom | Fort14Right | Fort14Left
		'Fort_14_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort14Bottom'], p) or s.has(el['Fort14Right'], p) or s.has(el['Fort14Left'], p),
#		                                                                           Fort15Right2
		'Fort_15_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort15Right2'], p),
#		                                                                           Fort15Top + (hook | 2LEDGE)
		'Fort_15_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                    : lambda s : s.has(el['Fort15Top'], p) and (s.has(el['hook'], p) or macros['2LEDGE'](s)),
#		                                                                           Fort15Right2 + claw | Fort15Top | Fort15Bottom
		'Fort_15_GAMEPLAY.BP_SCR_LV1M_2190_2'                                     : lambda s : s.has(el['Fort15Right2'], p) and s.has(el['claw'], p) or s.has(el['Fort15Top'], p) or s.has(el['Fort15Bottom'], p),
#		                                                                           Fort15Right2 + LEDGE
		'Fort_15_GAMEPLAY.BP_SCR_LV1S_2021_1'                                     : lambda s : s.has(el['Fort15Right2'], p) and macros['LEDGE'](s),
#		                                                                           Fort15Right2 | Fort15Right1 | Fort15Top | Fort15Bottom + LEDGE
		'Fort_15_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort15Right2'], p) or s.has(el['Fort15Right1'], p) or s.has(el['Fort15Top'], p) or s.has(el['Fort15Bottom'], p) and macros['LEDGE'](s),
#		                                                                           Fort15Right1 | Fort15Right2 + LEDGE
		'Fort_15_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort15Right1'], p) or s.has(el['Fort15Right2'], p) and macros['LEDGE'](s),
#		                                                                           Fort15Bottom | Fort15Top
		'Fort_15_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort15Bottom'], p) or s.has(el['Fort15Top'], p),
#		                                                                           Fort15Top | Fort15Right3 + LEDGE
		'Fort_15_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort15Top'], p) or s.has(el['Fort15Right3'], p) and macros['LEDGE'](s),
#		                                                                           Fort15Right3 | Fort15Bottom + LEDGE | Fort15Right2
		'Fort_15_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort15Right3'], p) or s.has(el['Fort15Bottom'], p) and macros['LEDGE'](s) or s.has(el['Fort15Right2'], p),
#		                                                                           Fort16Left1 | Fort16Top | Fort16Left2 | Fort16Right
		'Fort_16_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Fort16Left1'], p) or s.has(el['Fort16Top'], p) or s.has(el['Fort16Left2'], p) or s.has(el['Fort16Right'], p),
#		                                                                           Fort16Left1
		'Fort_16_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort16Left1'], p),
#		                                                                           Fort16Top
		'Fort_16_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort16Top'], p),
#		                                                                           Fort16Left2
		'Fort_16_GAMEPLAY.BP_WorldTravelVolume6'                                  : lambda s : s.has(el['Fort16Left2'], p),
#		                                                                           Fort16Right
		'Fort_16_GAMEPLAY.BP_WorldTravelVolume7'                                  : lambda s : s.has(el['Fort16Right'], p),
#		                                                                           Fort17Bottom
		'Fort_17_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                      : lambda s : s.has(el['Fort17Bottom'], p),
#		                                                                           Fort17Bottom
		'Fort_17_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort17Bottom'], p),
#		                                                                           Fort17Right | Fort17Bottom
		'Fort_17_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort17Right'], p) or s.has(el['Fort17Bottom'], p),
#		                                                                           Fort18Right + (claw + (sinner | dodge + LEDGE | 2LEDGE | djump + dash))
		'Fort_18_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_Treasure_2'             : lambda s : s.has(el['Fort18Right'], p) and (s.has(el['claw'], p) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and macros['LEDGE'](s) or macros['2LEDGE'](s) or s.has(el['djump'], p) and s.has(el['dash'], p))),
#		                                                                           Fort18Bottom + (LEDGE | claw)
		'Fort_18_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'                  : lambda s : s.has(el['Fort18Bottom'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Fort18Left | Fort18Right
		'Fort_18_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort18Left'], p) or s.has(el['Fort18Right'], p),
#		                                                                           Fort18Right | Fort18Left | Fort18Bottom
		'Fort_18_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort18Right'], p) or s.has(el['Fort18Left'], p) or s.has(el['Fort18Bottom'], p),
#		                                                                           Fort18Bottom | Fort18Right
		'Fort_18_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort18Bottom'], p) or s.has(el['Fort18Right'], p),
#		                                                                           Fort19Top
		'Fort_19_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                    : lambda s : s.has(el['Fort19Top'], p),
#		                                                                           Fort19Top + claw
		'Fort_19_GAMEPLAY.BP_SCR_LV2M_2190_4'                                     : lambda s : s.has(el['Fort19Top'], p) and s.has(el['claw'], p),
#		                                                                           Fort19Left + slam
		'Fort_19_GAMEPLAY.BP_SCR_LV2S_2021_2'                                     : lambda s : s.has(el['Fort19Left'], p) and s.has(el['slam'], p),
#		                                                                           Fort19Left | Fort19Top + LEDGE
		'Fort_19_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Fort19Left'], p) or s.has(el['Fort19Top'], p) and macros['LEDGE'](s),
#		                                                                           Fort19Top | Fort19Left + LEDGE
		'Fort_19_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Fort19Top'], p) or s.has(el['Fort19Left'], p) and macros['LEDGE'](s),
#		                                                                           Fort19Bottom | Fort19Top + claw
		'Fort_19_GAMEPLAY.BP_WorldTravelVolume5'                                  : lambda s : s.has(el['Fort19Bottom'], p) or s.has(el['Fort19Top'], p) and s.has(el['claw'], p),
#		                                                                           Fort20Bottom | MourningHall
		'Fort_20_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Fort20Bottom'], p) or s.can_reach(el['MourningHall'], 'Location', p),
#		                                                                           Fort20Bottom | Fort20Top
		'MourningHall'                                                            : lambda s : s.has(el['Fort20Bottom'], p) or s.has(el['Fort20Top'], p),
#		                                                                           Fort20Top | MourningHall
		'Fort_20_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort20Top'], p) or s.can_reach(el['MourningHall'], 'Location', p),
#		                                                                           Fort21Bottom
		'Fort_21_GAMEPLAY.BP_e5070_Killer'                                        : lambda s : s.has(el['Fort21Bottom'], p),
#		                                                                           Ulv + (claw | (silva + djump + (champion | dodge)))
		'Fort_21_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                    : lambda s : s.can_reach(el['Ulv'], 'Location', p) and (s.has(el['claw'], p) or (s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['dodge'], p)))),
#		                                                                           Ulv + (claw | (silva + djump + (champion | dodge)))
		'Fort_21_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.can_reach(el['Ulv'], 'Location', p) and (s.has(el['claw'], p) or (s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['dodge'], p)))),
#		                                                                           Fort21Bottom
		'Fort_21_GAMEPLAY.BP_WorldTravelVolume2_5'                                : lambda s : s.has(el['Fort21Bottom'], p),
#		                                                                           Oubliette01Left + swim
		'Oubliette_01_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_5'                 : lambda s : s.has(el['Oubliette01Left'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette01Left + swim
		'Oubliette_01_GAMEPLAY.BP_SCR_LV1S_2010_3'                                : lambda s : s.has(el['Oubliette01Left'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette01Left | Oubliette01Right + swim
		'Oubliette_01_GAMEPLAY.BP_WorldTravelVolume11'                            : lambda s : s.has(el['Oubliette01Left'], p) or s.has(el['Oubliette01Right'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette01Right | Oubliette01Left + swim
		'Oubliette_01_GAMEPLAY.BP_WorldTravelVolume12'                            : lambda s : s.has(el['Oubliette01Right'], p) or s.has(el['Oubliette01Left'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette02Left | Oubliette02Right1 | Oubliette02Right2
		'Oubliette_02_GAMEPLAY.BP_Interactable_Item_Tip3'                         : lambda s : s.has(el['Oubliette02Left'], p) or s.has(el['Oubliette02Right1'], p) or s.has(el['Oubliette02Right2'], p),
#		                                                                           Oubliette02Left | Aqueduct + (LEDGE | claw)
		'Oubliette_02_GAMEPLAY.BP_WorldTravelVolume11'                            : lambda s : s.has(el['Oubliette02Left'], p) or s.can_reach(el['Aqueduct'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Oubliette02Right1 | Aqueduct
		'Oubliette_02_GAMEPLAY.BP_WorldTravelVolume12'                            : lambda s : s.has(el['Oubliette02Right1'], p) or s.can_reach(el['Aqueduct'], 'Location', p),
#		                                                                           Oubliette02Right2 | Aqueduct
		'Oubliette_02_GAMEPLAY.BP_WorldTravelVolume13'                            : lambda s : s.has(el['Oubliette02Right2'], p) or s.can_reach(el['Aqueduct'], 'Location', p),
#		                                                                           Oubliette03Left + swim
		'Oubliette_03_GAMEPLAY.BP_SCR_LV1M_2050_2'                                : lambda s : s.has(el['Oubliette03Left'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette03Left + swim
		'Oubliette_03_GAMEPLAY.BP_SCR_LV1S_2081_2'                                : lambda s : s.has(el['Oubliette03Left'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette03Left | Oubliette03Right + swim
		'Oubliette_03_GAMEPLAY.BP_WorldTravelVolume13'                            : lambda s : s.has(el['Oubliette03Left'], p) or s.has(el['Oubliette03Right'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette03Right | Oubliette03Left + swim | Oubliette03Top + (LEDGE | claw | swim)
		'Oubliette_03_GAMEPLAY.BP_WorldTravelVolume14'                            : lambda s : s.has(el['Oubliette03Right'], p) or s.has(el['Oubliette03Left'], p) and s.has(el['swim'], p) or s.has(el['Oubliette03Top'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['swim'], p)),
#		                                                                           Oubliette03Top | Oubliette03Right + hook
		'Oubliette_03_GAMEPLAY.BP_WorldTravelVolume15'                            : lambda s : s.has(el['Oubliette03Top'], p) or s.has(el['Oubliette03Right'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette03Right + CHARGE
		'Oubliette_03_GEO.BP_SCR_LV1LL_0000_2'                                    : lambda s : s.has(el['Oubliette03Right'], p) and macros['CHARGE'](s),
#		                                                                           Oubliette04Left + (FULLSILVA | hook | 3LEDGE | sinner + silva + djump | silva + champion + dodge | 2HORIZONTAL + dash + LEDGE | djump + champion + HORIZONTAL)
		'Oubliette_04_GAMEPLAY.BP_SCR_LV1S_2020_2'                                : lambda s : s.has(el['Oubliette04Left'], p) and (macros['FULLSILVA'](s) or s.has(el['hook'], p) or macros['3LEDGE'](s) or s.has(el['sinner'], p) and s.has(el['silva'], p) and s.has(el['djump'], p) or s.has(el['silva'], p) and s.has(el['champion'], p) and s.has(el['dodge'], p) or macros['2HORIZONTAL'](s) and s.has(el['dash'], p) and macros['LEDGE'](s) or s.has(el['djump'], p) and s.has(el['champion'], p) and macros['HORIZONTAL'](s)),
#		                                                                           Oubliette04Right | Oubliette04Left
		'Oubliette_04_GAMEPLAY.BP_SCR_LV2S_2010_3'                                : lambda s : s.has(el['Oubliette04Right'], p) or s.has(el['Oubliette04Left'], p),
#		                                                                           Oubliette04Right | Oubliette04Left
		'Oubliette_04_GAMEPLAY.BP_WorldTravelVolume14'                            : lambda s : s.has(el['Oubliette04Right'], p) or s.has(el['Oubliette04Left'], p),
#		                                                                           Oubliette04Right + (claw | hook | LEDGE) | Oubliette04Left
		'Oubliette_04_GAMEPLAY.BP_WorldTravelVolume16'                            : lambda s : s.has(el['Oubliette04Right'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) or macros['LEDGE'](s)) or s.has(el['Oubliette04Left'], p),
#		                                                                           Oubliette051Bottom
		'Oubliette_05_1_GAMEPLAY.BP_Interactable_WorldTravel13'                   : lambda s : s.has(el['Oubliette051Bottom'], p),
#		                                                                           Oubliette051Bottom
		'Oubliette_05_1_GAMEPLAY.BP_SCR_LV2S_2021_2'                              : lambda s : s.has(el['Oubliette051Bottom'], p),
#		                                                                           Oubliette052Bottom1 | Oubliette052Bottom2
		'Oubliette_05_2_GAMEPLAY.BP_Interactable_WorldTravel12'                   : lambda s : s.has(el['Oubliette052Bottom1'], p) or s.has(el['Oubliette052Bottom2'], p),
#		                                                                           Oubliette052Bottom1 + (LEDGE + claw + hook)
		'Oubliette_05_2_GAMEPLAY.BP_SCR_LV1S_2010_3'                              : lambda s : s.has(el['Oubliette052Bottom1'], p) and (macros['LEDGE'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                                           Oubliette052Bottom2 | Oubliette052Bottom1 + (LEDGE + claw + hook)
		'Oubliette_05_2_GAMEPLAY.BP_WorldTravelVolume18'                          : lambda s : s.has(el['Oubliette052Bottom2'], p) or s.has(el['Oubliette052Bottom1'], p) and (macros['LEDGE'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                                           Oubliette053Top
		'Oubliette_05_3_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'           : lambda s : s.has(el['Oubliette053Top'], p),
#		                                                                           Oubliette053Top
		'Oubliette_05_3_GAMEPLAY.BP_Interactable_WorldTravel16'                   : lambda s : s.has(el['Oubliette053Top'], p),
#		                                                                           Oubliette05Top4
		'Oubliette_05_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_2'                 : lambda s : s.has(el['Oubliette05Top4'], p),
#		                                                                           Oubliette05Top2 | Oubliette05Top1
		'Oubliette_05_GAMEPLAY.BP_Interactable_WorldTravel10'                     : lambda s : s.has(el['Oubliette05Top2'], p) or s.has(el['Oubliette05Top1'], p),
#		                                                                           Oubliette05Bottom2 | Oubliette05Left
		'Oubliette_05_GAMEPLAY.BP_Interactable_WorldTravel11'                     : lambda s : s.has(el['Oubliette05Bottom2'], p) or s.has(el['Oubliette05Left'], p),
#		                                                                           Oubliette05Top3 | Oubliette05Top1
		'Oubliette_05_GAMEPLAY.BP_Interactable_WorldTravel12'                     : lambda s : s.has(el['Oubliette05Top3'], p) or s.has(el['Oubliette05Top1'], p),
#		                                                                           Oubliette05Top1 | Oubliette05Left + LEDGE
		'Oubliette_05_GAMEPLAY.BP_Interactable_WorldTravel13'                     : lambda s : s.has(el['Oubliette05Top1'], p) or s.has(el['Oubliette05Left'], p) and macros['LEDGE'](s),
#		                                                                           Oubliette05Bottom1 | Oubliette05Left
		'Oubliette_05_GAMEPLAY.BP_Interactable_WorldTravel14'                     : lambda s : s.has(el['Oubliette05Bottom1'], p) or s.has(el['Oubliette05Left'], p),
#		                                                                           Oubliette05Top1 + CHARGE
		'Oubliette_05_GAMEPLAY.BP_SCR_LV1L_2220_3'                                : lambda s : s.has(el['Oubliette05Top1'], p) and macros['CHARGE'](s),
#		                                                                           Oubliette05Top4
		'Oubliette_05_GAMEPLAY.BP_SCR_LV1S_2021_2'                                : lambda s : s.has(el['Oubliette05Top4'], p),
#		                                                                           Oubliette05Left | Oubliette05Right | Oubliette05Top1
		'Oubliette_05_GAMEPLAY.BP_WorldTravelVolume15'                            : lambda s : s.has(el['Oubliette05Left'], p) or s.has(el['Oubliette05Right'], p) or s.has(el['Oubliette05Top1'], p),
#		                                                                           Oubliette05Right | Oubliette05Top4 + slam
		'Oubliette_05_GAMEPLAY.BP_WorldTravelVolume16'                            : lambda s : s.has(el['Oubliette05Right'], p) or s.has(el['Oubliette05Top4'], p) and s.has(el['slam'], p),
#		                                                                           Oubliette05Bottom3 | Oubliette05Left
		'Oubliette_05_GAMEPLAY.BP_WorldTravelVolume17'                            : lambda s : s.has(el['Oubliette05Bottom3'], p) or s.has(el['Oubliette05Left'], p),
#		                                                                           Oubliette05Top4
		'Oubliette_05_GAMEPLAY.BP_WorldTravelVolume18'                            : lambda s : s.has(el['Oubliette05Top4'], p),
#		                                                                           Oubliette061Left
		'Oubliette_06_1_GAMEPLAY.BP_Interactable_Item_Tip3'                       : lambda s : s.has(el['Oubliette061Left'], p),
#		                                                                           Oubliette061Left | Cells
		'Oubliette_06_1_GAMEPLAY.BP_Interactable_WorldTravel14'                   : lambda s : s.has(el['Oubliette061Left'], p) or s.can_reach(el['Cells'], 'Location', p),
#		                                                                           Oubliette062Bottom2 + swim
		'Oubliette_06_2_GAMEPLAY.BP_Interactable_Passive_dmgup_maxHP_2'           : lambda s : s.has(el['Oubliette062Bottom2'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette062Bottom2
		'Oubliette_06_2_GAMEPLAY.BP_Interactable_WorldTravel13'                   : lambda s : s.has(el['Oubliette062Bottom2'], p),
#		                                                                           Oubliette063Left1
		'Oubliette_06_3_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'              : lambda s : s.has(el['Oubliette063Left1'], p),
#		                                                                           Oubliette063Left1
		'Oubliette_06_3_GAMEPLAY.BP_WorldTravelVolume16'                          : lambda s : s.has(el['Oubliette063Left1'], p),
#		                                                                           Oubliette064Top
		'Oubliette_06_4_GAMEPLAY.BP_Interactable_Item_FinalPassivePart_2'         : lambda s : s.has(el['Oubliette064Top'], p),
#		                                                                           Oubliette064Top
		'Oubliette_06_4_GAMEPLAY.BP_Interactable_WorldTravel16'                   : lambda s : s.has(el['Oubliette064Top'], p),
#		                                                                           Oubliette06Bottom
		'Oubliette_06_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'              : lambda s : s.has(el['Oubliette06Bottom'], p),
#		                                                                           Oubliette06Bottom + hook
		'Oubliette_06_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                : lambda s : s.has(el['Oubliette06Bottom'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette06Bottom
		'Oubliette_06_GAMEPLAY.BP_SCR_LV1S_2021_2'                                : lambda s : s.has(el['Oubliette06Bottom'], p),
#		                                                                           Oubliette06Left | Oubliette06Bottom + hook
		'Oubliette_06_GAMEPLAY.BP_WorldTravelVolume20'                            : lambda s : s.has(el['Oubliette06Left'], p) or s.has(el['Oubliette06Bottom'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette06Right | Oubliette06Bottom + hook
		'Oubliette_06_GAMEPLAY.BP_WorldTravelVolume21'                            : lambda s : s.has(el['Oubliette06Right'], p) or s.has(el['Oubliette06Bottom'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette06Bottom | Oubliette06Right | Oubliette06Left
		'Oubliette_06_GAMEPLAY.BP_WorldTravelVolume22'                            : lambda s : s.has(el['Oubliette06Bottom'], p) or s.has(el['Oubliette06Right'], p) or s.has(el['Oubliette06Left'], p),
#		                                                                           Oubliette071Top
		'Oubliette_07_1_GAMEPLAY.BP_Interactable_Item_Tip3'                       : lambda s : s.has(el['Oubliette071Top'], p),
#		                                                                           Oubliette071Top
		'Oubliette_07_1_GAMEPLAY.BP_Interactable_WorldTravel14'                   : lambda s : s.has(el['Oubliette071Top'], p),
#		                                                                           Oubliette072Bottom
		'Oubliette_07_2_GAMEPLAY.BP_e2072_Mimic'                                  : lambda s : s.has(el['Oubliette072Bottom'], p),
#		                                                                           Oubliette072Bottom
		'Oubliette_07_2_GAMEPLAY.BP_Interactable_WorldTravel14'                   : lambda s : s.has(el['Oubliette072Bottom'], p),
#		                                                                           Oubliette07Right1 | Oubliette07Bottom1 + (hook | LEDGE)
		'Oubliette_07_GAMEPLAY.BP_Interactable_WorldTravel17'                     : lambda s : s.has(el['Oubliette07Right1'], p) or s.has(el['Oubliette07Bottom1'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s)),
#		                                                                           Oubliette07Left1 | Oubliette07Bottom1 + (hook + (LEDGE | HORIZONTAL) | silva + djump)
		'Oubliette_07_GAMEPLAY.BP_Interactable_WorldTravel18'                     : lambda s : s.has(el['Oubliette07Left1'], p) or s.has(el['Oubliette07Bottom1'], p) and (s.has(el['hook'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                                           Oubliette07Bottom2 | Oubliette07Bottom1
		'Oubliette_07_GAMEPLAY.BP_Interactable_WorldTravel19'                     : lambda s : s.has(el['Oubliette07Bottom2'], p) or s.has(el['Oubliette07Bottom1'], p),
#		                                                                           Oubliette07Top | Oubliette07Left1 + unlock + (hook | claw + (3LEDGE | FULLSILVA))
		'Oubliette_07_GAMEPLAY.BP_Interactable_WorldTravel20'                     : lambda s : s.has(el['Oubliette07Top'], p) or s.has(el['Oubliette07Left1'], p) and s.has(el['unlock'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['3LEDGE'](s) or macros['FULLSILVA'](s))),
#		                                                                           Oubliette07Left2
		'Oubliette_07_GAMEPLAY.BP_WorldTravelVolume19'                            : lambda s : s.has(el['Oubliette07Left2'], p),
#		                                                                           Oubliette07Right2 | Oubliette07Bottom1
		'Oubliette_07_GAMEPLAY.BP_WorldTravelVolume20'                            : lambda s : s.has(el['Oubliette07Right2'], p) or s.has(el['Oubliette07Bottom1'], p),
#		                                                                           Oubliette07Bottom1 | Oubliette07Left1 | Oubliette07Left2 | Oubliette07Bottom2 | Oubliette07Right1 | Oubliette07Right2
		'Oubliette_07_GAMEPLAY.BP_WorldTravelVolume21'                            : lambda s : s.has(el['Oubliette07Bottom1'], p) or s.has(el['Oubliette07Left1'], p) or s.has(el['Oubliette07Left2'], p) or s.has(el['Oubliette07Bottom2'], p) or s.has(el['Oubliette07Right1'], p) or s.has(el['Oubliette07Right2'], p),
#		                                                                           slam + (Oubliette08Top | Oubliette08Right + (hook | LEDGE | HORIZONTAL))
		'Oubliette_08_GAMEPLAY.BP_SCR_LV2M_2050_3'                                : lambda s : s.has(el['slam'], p) and (s.has(el['Oubliette08Top'], p) or s.has(el['Oubliette08Right'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s))),
#		                                                                           Oubliette08Left + hook
		'Oubliette_08_GAMEPLAY.BP_SCR_LV2S_2081_2'                                : lambda s : s.has(el['Oubliette08Left'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette08Right | Oubliette08Left + LEDGE
		'Oubliette_08_GAMEPLAY.BP_WorldTravelVolume15'                            : lambda s : s.has(el['Oubliette08Right'], p) or s.has(el['Oubliette08Left'], p) and macros['LEDGE'](s),
#		                                                                           Oubliette08Left | Oubliette08Right | Oubliette08Top
		'Oubliette_08_GAMEPLAY.BP_WorldTravelVolume16'                            : lambda s : s.has(el['Oubliette08Left'], p) or s.has(el['Oubliette08Right'], p) or s.has(el['Oubliette08Top'], p),
#		                                                                           Oubliette08Top | Oubliette08Right + hook
		'Oubliette_08_GAMEPLAY.BP_WorldTravelVolume17'                            : lambda s : s.has(el['Oubliette08Top'], p) or s.has(el['Oubliette08Right'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette09Top + claw
		'Oubliette_09_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                 : lambda s : s.has(el['Oubliette09Top'], p) and s.has(el['claw'], p),
#		                                                                           Oubliette09Top + claw
		'Oubliette_09_GAMEPLAY.BP_Interactable_Item_MaxHPUp_5'                    : lambda s : s.has(el['Oubliette09Top'], p) and s.has(el['claw'], p),
#		                                                                           Oubliette09Top + swim
		'Oubliette_09_GAMEPLAY.BP_SCR_LV1M_2050_2'                                : lambda s : s.has(el['Oubliette09Top'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette09Right | Oubliette09Top + swim + HORIZONTAL
		'Oubliette_09_GAMEPLAY.BP_WorldTravelVolume17'                            : lambda s : s.has(el['Oubliette09Right'], p) or s.has(el['Oubliette09Top'], p) and s.has(el['swim'], p) and macros['HORIZONTAL'](s),
#		                                                                           Oubliette09Left | Oubliette09Top + swim
		'Oubliette_09_GAMEPLAY.BP_WorldTravelVolume18'                            : lambda s : s.has(el['Oubliette09Left'], p) or s.has(el['Oubliette09Top'], p) and s.has(el['swim'], p),
#		                                                                           Oubliette09Top | Oubliette09Left
		'Oubliette_09_GAMEPLAY.BP_WorldTravelVolume19'                            : lambda s : s.has(el['Oubliette09Top'], p) or s.has(el['Oubliette09Left'], p),
#		                                                                           Oubliette10Left1 | Oubliette10Right | Oubliette10Left2 | Oubliette10Top
		'Oubliette_10_GAMEPLAY.BP_Interactable_Item_Tip3'                         : lambda s : s.has(el['Oubliette10Left1'], p) or s.has(el['Oubliette10Right'], p) or s.has(el['Oubliette10Left2'], p) or s.has(el['Oubliette10Top'], p),
#		                                                                           Oubliette10Right | DarkChamber
		'Oubliette_10_GAMEPLAY.BP_WorldTravelVolume17'                            : lambda s : s.has(el['Oubliette10Right'], p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                                           Oubliette10Left1 | DarkChamber
		'Oubliette_10_GAMEPLAY.BP_WorldTravelVolume18'                            : lambda s : s.has(el['Oubliette10Left1'], p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                                           Oubliette10Left2 | DarkChamber + CHARGE
		'Oubliette_10_GAMEPLAY.BP_WorldTravelVolume19'                            : lambda s : s.has(el['Oubliette10Left2'], p) or s.can_reach(el['DarkChamber'], 'Location', p) and macros['CHARGE'](s),
#		                                                                           Oubliette10Top | DarkChamber
		'Oubliette_10_GAMEPLAY.BP_WorldTravelVolume20'                            : lambda s : s.has(el['Oubliette10Top'], p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                                           Oubliette11Left1 + (LEDGE | dash | HORIZONTAL | hook) | Oubliette11Left2 + hook
		'Oubliette_11_GAMEPLAY.BP_SCR_LV2S_2020_2'                                : lambda s : s.has(el['Oubliette11Left1'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s) or s.has(el['hook'], p)) or s.has(el['Oubliette11Left2'], p) and s.has(el['hook'], p),
#		                                                                           Oubliette11Right1 | Oubliette11Left1 | Oubliette11Top
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume19'                            : lambda s : s.has(el['Oubliette11Right1'], p) or s.has(el['Oubliette11Left1'], p) or s.has(el['Oubliette11Top'], p),
#		                                                                           Oubliette11Left2 | Oubliette11Left1 | Oubliette11Right1 | Oubliette11Top | Oubliette11Right2
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume20'                            : lambda s : s.has(el['Oubliette11Left2'], p) or s.has(el['Oubliette11Left1'], p) or s.has(el['Oubliette11Right1'], p) or s.has(el['Oubliette11Top'], p) or s.has(el['Oubliette11Right2'], p),
#		                                                                           Oubliette11Right2 | Oubliette11Left2
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume21'                            : lambda s : s.has(el['Oubliette11Right2'], p) or s.has(el['Oubliette11Left2'], p),
#		                                                                           Oubliette11Left1 | Oubliette11Left2 + hook | Oubliette11Right2 + (HORIZONTAL | LEDGE)
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume22'                            : lambda s : s.has(el['Oubliette11Left1'], p) or s.has(el['Oubliette11Left2'], p) and s.has(el['hook'], p) or s.has(el['Oubliette11Right2'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s)),
#		                                                                           Oubliette11Bottom | Oubliette11Left1 + slam
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume23'                            : lambda s : s.has(el['Oubliette11Bottom'], p) or s.has(el['Oubliette11Left1'], p) and s.has(el['slam'], p),
#		                                                                           Oubliette11Top | Oubliette11Left1 + claw + (FULLSILVA | (hook + (HORIZONTAL | LEDGE)))
		'Oubliette_11_GAMEPLAY.BP_WorldTravelVolume24'                            : lambda s : s.has(el['Oubliette11Top'], p) or s.has(el['Oubliette11Left1'], p) and s.has(el['claw'], p) and (macros['FULLSILVA'](s) or (s.has(el['hook'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s)))),
#		                                                                           Oubliette12Left
		'Oubliette_12_GAMEPLAY.BP_e2182_Shadow'                                   : lambda s : s.has(el['Oubliette12Left'], p),
#		                                                                           Oubliette12Left | Executioner
		'Oubliette_12_GAMEPLAY.BP_WorldTravelVolume22_0'                          : lambda s : s.has(el['Oubliette12Left'], p) or s.can_reach(el['Executioner'], 'Location', p),
#		                                                                           Oubliette131Bottom
		'Oubliette_13_1_GAMEPLAY.BP_Interactable_Passives_Treasure_2'             : lambda s : s.has(el['Oubliette131Bottom'], p),
#		                                                                           Oubliette131Bottom
		'Oubliette_13_1_GAMEPLAY.BP_WorldTravelVolume24'                          : lambda s : s.has(el['Oubliette131Bottom'], p),
#		                                                                           Oubliette132Top
		'Oubliette_13_2_GAMEPLAY.BP_SCR_LV3S_5000_1'                              : lambda s : s.has(el['Oubliette132Top'], p),
#		                                                                           Oubliette132Top
		'Oubliette_13_2_GAMEPLAY.BP_WorldTravelVolume23'                          : lambda s : s.has(el['Oubliette132Top'], p),
#		                                                                           Oubliette13Right + (claw + LEDGE | 2LEDGE | hook)
		'Oubliette_13_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                : lambda s : s.has(el['Oubliette13Right'], p) and (s.has(el['claw'], p) and macros['LEDGE'](s) or macros['2LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Oubliette13Left
		'Oubliette_13_GAMEPLAY.BP_Interactable_Item_Tip3'                         : lambda s : s.has(el['Oubliette13Left'], p),
#		                                                                           Oubliette13Left
		'Oubliette_13_GAMEPLAY.BP_SCR_LV1M_2001_3'                                : lambda s : s.has(el['Oubliette13Left'], p),
#		                                                                           Oubliette13Left + CHARGE + (LEDGE | HORIZONTAL | hook | dash | claw)
		'Oubliette_13_GAMEPLAY.BP_SCR_LV1M_2180_2'                                : lambda s : s.has(el['Oubliette13Left'], p) and macros['CHARGE'](s) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p) or s.has(el['claw'], p)),
#		                                                                           Oubliette13Bottom | Oubliette13Right
		'Oubliette_13_GAMEPLAY.BP_WorldTravelVolume21'                            : lambda s : s.has(el['Oubliette13Bottom'], p) or s.has(el['Oubliette13Right'], p),
#		                                                                           Oubliette13Right | Oubliette13Left
		'Oubliette_13_GAMEPLAY.BP_WorldTravelVolume22'                            : lambda s : s.has(el['Oubliette13Right'], p) or s.has(el['Oubliette13Left'], p),
#		                                                                           Oubliette13Left | Oubliette13Right + (hook | LEDGE + claw + HORIZONTAL)
		'Oubliette_13_GAMEPLAY.BP_WorldTravelVolume23'                            : lambda s : s.has(el['Oubliette13Left'], p) or s.has(el['Oubliette13Right'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                                           Oubliette14Left | Oubliette14Right
		'Oubliette_14_GAMEPLAY.BP_Interactable_Item_Tip3'                         : lambda s : s.has(el['Oubliette14Left'], p) or s.has(el['Oubliette14Right'], p),
#		                                                                           Oubliette14Left | ExecutionGrounds
		'Oubliette_14_GAMEPLAY.BP_WorldTravelVolume13'                            : lambda s : s.has(el['Oubliette14Left'], p) or s.can_reach(el['ExecutionGrounds'], 'Location', p),
#		                                                                           Oubliette14Right | ExecutionGrounds
		'Oubliette_14_GAMEPLAY.BP_WorldTravelVolume14'                            : lambda s : s.has(el['Oubliette14Right'], p) or s.can_reach(el['ExecutionGrounds'], 'Location', p),
#		                                                                           Oubliette15Left | Oubliette15Right
		'Oubliette_15_GAMEPLAY.BP_e5060_Assassin'                                 : lambda s : s.has(el['Oubliette15Left'], p) or s.has(el['Oubliette15Right'], p),
#		                                                                           Oubliette15Left | Oubliette15Right
		'Oubliette_15_GAMEPLAY.BP_WorldTravelVolume15'                            : lambda s : s.has(el['Oubliette15Left'], p) or s.has(el['Oubliette15Right'], p),
#		                                                                           Oubliette15Right | Oubliette15Left
		'Oubliette_15_GAMEPLAY.BP_WorldTravelVolume16'                            : lambda s : s.has(el['Oubliette15Right'], p) or s.has(el['Oubliette15Left'], p),
#		                                                                           Oubliette16Right
		'Oubliette_16_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'               : lambda s : s.has(el['Oubliette16Right'], p),
#		                                                                           Oubliette16Left
		'Oubliette_16_GAMEPLAY.BP_SCR_LV1L_2180_3'                                : lambda s : s.has(el['Oubliette16Left'], p),
#		                                                                           Oubliette16Left | Oubliette16Right
		'Oubliette_16_GAMEPLAY.BP_WorldTravelVolume17'                            : lambda s : s.has(el['Oubliette16Left'], p) or s.has(el['Oubliette16Right'], p),
#		                                                                           Oubliette16Right | Oubliette16Left + (hook + (sinner + (LEDGE | dash | dodge) | silva + (djump | dodge | champion + dash) | djump + (dodge | champion)) | silva + djump + (claw | champion | dodge))
		'Oubliette_16_GAMEPLAY.BP_WorldTravelVolume18'                            : lambda s : s.has(el['Oubliette16Right'], p) or s.has(el['Oubliette16Left'], p) and (s.has(el['hook'], p) and (s.has(el['sinner'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p) or s.has(el['dodge'], p)) or s.has(el['silva'], p) and (s.has(el['djump'], p) or s.has(el['dodge'], p) or s.has(el['champion'], p) and s.has(el['dash'], p)) or s.has(el['djump'], p) and (s.has(el['dodge'], p) or s.has(el['champion'], p))) or s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['claw'], p) or s.has(el['champion'], p) or s.has(el['dodge'], p))),
#		                                                                           Oubliette17Right
		'Oubliette_17_GAMEPLAY.BP_WorldTravelVolume19'                            : lambda s : s.has(el['Oubliette17Right'], p),
#		                                                                           Oubliette17Bottom | Oubliette17Right +  (CHARGE + slam + (dodge + claw | hook))
		'Oubliette_17_GAMEPLAY.BP_WorldTravelVolume20'                            : lambda s : s.has(el['Oubliette17Bottom'], p) or s.has(el['Oubliette17Right'], p) and (macros['CHARGE'](s) and s.has(el['slam'], p) and (s.has(el['dodge'], p) and s.has(el['claw'], p) or s.has(el['hook'], p))),
#		                                                                           Outside01Right | Outside01Left1 | Outside01Left2
		'Outside_01_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Outside01Right'], p) or s.has(el['Outside01Left1'], p) or s.has(el['Outside01Left2'], p),
#		                                                                           Outside01Left1 | Outside01Right + claw + (djump | champion | 2LEDGE)
		'Outside_01_GAMEPLAY.BP_WorldTravelVolume3_8'                             : lambda s : s.has(el['Outside01Left1'], p) or s.has(el['Outside01Right'], p) and s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or macros['2LEDGE'](s)),
#		                                                                           Outside01Left2
		'Outside_01_GAMEPLAY.BP_WorldTravelVolume4'                               : lambda s : s.has(el['Outside01Left2'], p),
#		                                                                           Outside02Left
		'Outside_02_GAMEPLAY.BP_WorldTravelVolume3_8'                             : lambda s : s.has(el['Outside02Left'], p),
#		                                                                           Outside03Right + (claw + (2LEDGE | LEDGE + HORIZONTAL | champion))
		'Outside_03_GAMEPLAY.BP_Interactable_Item_Tip3'                           : lambda s : s.has(el['Outside03Right'], p) and (s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or s.has(el['champion'], p))),
#		                                                                           Grotto
		'Outside_03_GAMEPLAY.BP_Interactable_Item_Tip4'                           : lambda s : s.can_reach(el['Grotto'], 'Location', p),
#		                                                                           Outside03Right + swim
		'Outside_03_GAMEPLAY.BP_Interactable_Passive_ShortHeal_2'                 : lambda s : s.has(el['Outside03Right'], p) and s.has(el['swim'], p),
#		                                                                           Grotto
		'Outside_03_GAMEPLAY.BP_SCR_LV2L_2230_2'                                  : lambda s : s.can_reach(el['Grotto'], 'Location', p),
#		                                                                           Outside03Right | Outside03Top
		'Outside_03_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Outside03Right'], p) or s.has(el['Outside03Top'], p),
#		                                                                           Outside03Top
		'Outside_03_GAMEPLAY.BP_WorldTravelVolume3_8'                             : lambda s : s.has(el['Outside03Top'], p),
#		                                                                           Swamp04Bottom + unlock
		'Swamp_04_GAMEPLAY.BP_e2172_Inferior'                                     : lambda s : s.has(el['Swamp04Bottom'], p) and s.has(el['unlock'], p),
#		                                                                           Swamp04Left
		'Swamp_04_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                    : lambda s : s.has(el['Swamp04Left'], p),
#		                                                                           Swamp04Bottom | Swamp04Left + LEDGE
		'Swamp_04_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp04Bottom'], p) or s.has(el['Swamp04Left'], p) and macros['LEDGE'](s),
#		                                                                           Swamp04Left | Swamp04Bottom + LEDGE
		'Swamp_04_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp04Left'], p) or s.has(el['Swamp04Bottom'], p) and macros['LEDGE'](s),
#		                                                                           Swamp05Left + swim
		'Swamp_05_GAMEPLAY.BP_SCR_LV2M_2171_2'                                    : lambda s : s.has(el['Swamp05Left'], p) and s.has(el['swim'], p),
#		                                                                           Swamp05Top | Swamp05Right + (LEDGE | claw)
		'Swamp_05_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp05Top'], p) or s.has(el['Swamp05Right'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Swamp05Right | Swamp05Top | Swamp05Left + (LEDGE | claw)
		'Swamp_05_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp05Right'], p) or s.has(el['Swamp05Top'], p) or s.has(el['Swamp05Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Swamp05Bottom | Swamp05Left + swim + CHARGE
		'Swamp_05_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp05Bottom'], p) or s.has(el['Swamp05Left'], p) and s.has(el['swim'], p) and macros['CHARGE'](s),
#		                                                                           Swamp05Left | Swamp05Right
		'Swamp_05_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Swamp05Left'], p) or s.has(el['Swamp05Right'], p),
#		                                                                           Swamp05Left + swim
		'Swamp_05_GEO.BP_SCR_LV1M_2051_2'                                         : lambda s : s.has(el['Swamp05Left'], p) and s.has(el['swim'], p),
#		                                                                           Swamp06Left | Swamp06Top
		'Swamp_06_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Swamp06Left'], p) or s.has(el['Swamp06Top'], p),
#		                                                                           Swamp06Top
		'Swamp_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                   : lambda s : s.has(el['Swamp06Top'], p),
#		                                                                           Swamp06Top
		'Swamp_06_GAMEPLAY.BP_SCR_LV1L_2180_3'                                    : lambda s : s.has(el['Swamp06Top'], p),
#		                                                                           Swamp06Left | Lab2
		'Swamp_06_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp06Left'], p) or s.can_reach(el['Lab2'], 'Location', p),
#		                                                                           Swamp06Top
		'Swamp_06_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp06Top'], p),
#		                                                                           Swamp07Right + claw
		'Swamp_07_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                     : lambda s : s.has(el['Swamp07Right'], p) and s.has(el['claw'], p),
#		                                                                           Swamp07Left + (claw + LEDGE)
		'Swamp_07_GAMEPLAY.BP_Interactable_Passive_RecastTimeCut_Lv2_2'           : lambda s : s.has(el['Swamp07Left'], p) and (s.has(el['claw'], p) and macros['LEDGE'](s)),
#		                                                                           Swamp07Bottom | Swamp07Right + Swamp07Left + Swamp07Top
		'Swamp_07_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp07Bottom'], p) or s.has(el['Swamp07Right'], p) and s.has(el['Swamp07Left'], p) and s.has(el['Swamp07Top'], p),
#		                                                                           Swamp07Right
		'Swamp_07_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp07Right'], p),
#		                                                                           Swamp07Left
		'Swamp_07_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp07Left'], p),
#		                                                                           Swamp07Top
		'Swamp_07_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Swamp07Top'], p),
#		                                                                           Swamp08Right2 + swim
		'Swamp_08_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_2'                     : lambda s : s.has(el['Swamp08Right2'], p) and s.has(el['swim'], p),
#		                                                                           Swamp08Right2 + swim
		'Swamp_08_GAMEPLAY.BP_SCR_LV1M_2051_2'                                    : lambda s : s.has(el['Swamp08Right2'], p) and s.has(el['swim'], p),
#		                                                                           Swamp08Right2 + swim
		'Swamp_08_GAMEPLAY.BP_SCR_LV2M_2051_2'                                    : lambda s : s.has(el['Swamp08Right2'], p) and s.has(el['swim'], p),
#		                                                                           Swamp08Right1 | Swamp08Right2 + (hook | (claw + (djump | champion | silva + dodge))) + (djump | HORIZONTAL)
		'Swamp_08_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp08Right1'], p) or s.has(el['Swamp08Right2'], p) and (s.has(el['hook'], p) or (s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)))) and (s.has(el['djump'], p) or macros['HORIZONTAL'](s)),
#		                                                                           Swamp08Right2 | Swamp08Top | Swamp08Right1
		'Swamp_08_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp08Right2'], p) or s.has(el['Swamp08Top'], p) or s.has(el['Swamp08Right1'], p),
#		                                                                           Swamp08Top | Swamp08Right2 + LEDGE
		'Swamp_08_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp08Top'], p) or s.has(el['Swamp08Right2'], p) and macros['LEDGE'](s),
#		                                                                           Swamp09Right2 + (LEDGE | HORIZONTAL)
		'Swamp_09_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                   : lambda s : s.has(el['Swamp09Right2'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Swamp09Right1 + (LEDGE + HORIZONTAL | 2LEDGE)
		'Swamp_09_GAMEPLAY.BP_SCR_LV2M_2170_2'                                    : lambda s : s.has(el['Swamp09Right1'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)),
#		                                                                           Swamp09Bottom1 | Swamp09Right1 + CHARGE
		'Swamp_09_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp09Bottom1'], p) or s.has(el['Swamp09Right1'], p) and macros['CHARGE'](s),
#		                                                                           Swamp09Right1 | Swamp09Right2 + (LEDGE | HORIZONTAL)
		'Swamp_09_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp09Right1'], p) or s.has(el['Swamp09Right2'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Swamp09Bottom2 | Swamp09Right2
		'Swamp_09_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp09Bottom2'], p) or s.has(el['Swamp09Right2'], p),
#		                                                                           Swamp09Right2 | Swamp09Right1
		'Swamp_09_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Swamp09Right2'], p) or s.has(el['Swamp09Right1'], p),
#		                                                                           Swamp1Bottom | Swamp1Left
		'Swamp_1_GAMEPLAY.BP_Interactable_Item_Tip3'                              : lambda s : s.has(el['Swamp1Bottom'], p) or s.has(el['Swamp1Left'], p),
#		                                                                           Swamp1Bottom | Lab1
		'Swamp_1_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Swamp1Bottom'], p) or s.can_reach(el['Lab1'], 'Location', p),
#		                                                                           Swamp1Left | Lab1
		'Swamp_1_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Swamp1Left'], p) or s.can_reach(el['Lab1'], 'Location', p),
#		                                                                           Swamp10Right
		'Swamp_10_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Swamp10Right'], p),
#		                                                                           Lab3 + swim
		'Swamp_10_GAMEPLAY.BP_SCR_LV1M_2051_2'                                    : lambda s : s.can_reach(el['Lab3'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Swamp10Right | Lab3
		'Swamp_10_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp10Right'], p) or s.can_reach(el['Lab3'], 'Location', p),
#		                                                                           Swamp11Left + (LEDGE + HORIZONTAL | 2HORIZONTAL | silva + djump)
		'Swamp_11_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                     : lambda s : s.has(el['Swamp11Left'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                                           Swamp11Left
		'Swamp_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                   : lambda s : s.has(el['Swamp11Left'], p),
#		                                                                           Swamp11Bottom | Swamp11Left
		'Swamp_11_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp11Bottom'], p) or s.has(el['Swamp11Left'], p),
#		                                                                           Swamp11Left | Swamp11Bottom + (hook | claw | 2LEDGE) + (djump | champion | (silva + dodge))
		'Swamp_11_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp11Left'], p) or s.has(el['Swamp11Bottom'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['2LEDGE'](s)) and (s.has(el['djump'], p) or s.has(el['champion'], p) or (s.has(el['silva'], p) and s.has(el['dodge'], p))),
#		                                                                           Lab4 + slam
		'Swamp_12_GAMEPLAY.BP_Interactable_Item_HealPower_Up_2'                   : lambda s : s.can_reach(el['Lab4'], 'Location', p) and s.has(el['slam'], p),
#		                                                                           Swamp12Left | Swamp12Bottom | Swamp12TP
		'Swamp_12_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Swamp12Left'], p) or s.has(el['Swamp12Bottom'], p) or s.has(el['Swamp12TP'], p),
#		                                                                           Swamp12Left | Lab4
		'Swamp_12_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp12Left'], p) or s.can_reach(el['Lab4'], 'Location', p),
#		                                                                           Swamp12Bottom | Lab4 + slam + unlock
		'Swamp_12_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp12Bottom'], p) or s.can_reach(el['Lab4'], 'Location', p) and s.has(el['slam'], p) and s.has(el['unlock'], p),
#		                                                                           Swamp13Top2
		'Swamp_13_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                     : lambda s : s.has(el['Swamp13Top2'], p),
#		                                                                           Swamp13Top1 + slam | Swamp13Top2 + CHARGE + slam
		'Swamp_13_GAMEPLAY.BP_SCR_LV1L_2170_3'                                    : lambda s : s.has(el['Swamp13Top1'], p) and s.has(el['slam'], p) or s.has(el['Swamp13Top2'], p) and macros['CHARGE'](s) and s.has(el['slam'], p),
#		                                                                           Swamp13Bottom + (hook | claw)
		'Swamp_13_GAMEPLAY.BP_SCR_LV2L_2170_3'                                    : lambda s : s.has(el['Swamp13Bottom'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p)),
#		                                                                           Swamp13Left | Swamp13Top1 + slam | Swamp13Top2 + CHARGE + slam
		'Swamp_13_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp13Left'], p) or s.has(el['Swamp13Top1'], p) and s.has(el['slam'], p) or s.has(el['Swamp13Top2'], p) and macros['CHARGE'](s) and s.has(el['slam'], p),
#		                                                                           Swamp13Top1 | Swamp13Bottom + claw + 3LEDGE
		'Swamp_13_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp13Top1'], p) or s.has(el['Swamp13Bottom'], p) and s.has(el['claw'], p) and macros['3LEDGE'](s),
#		                                                                           Swamp13Top2
		'Swamp_13_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp13Top2'], p),
#		                                                                           Swamp13Bottom | slam + (Swamp13Top1 | Swamp13Left)
		'Swamp_13_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Swamp13Bottom'], p) or s.has(el['slam'], p) and (s.has(el['Swamp13Top1'], p) or s.has(el['Swamp13Left'], p)),
#		                                                                           Swamp14Top | Swamp14Bottom + (LEDGE | claw | hook)
		'Swamp_14_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                    : lambda s : s.has(el['Swamp14Top'], p) or s.has(el['Swamp14Bottom'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                                           Swamp14Top + (2LEDGE | hook)
		'Swamp_14_GAMEPLAY.BP_SCR_LV1L_2170_3'                                    : lambda s : s.has(el['Swamp14Top'], p) and (macros['2LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Swamp14Top | Swamp14Bottom + claw + 3LEDGE
		'Swamp_14_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp14Top'], p) or s.has(el['Swamp14Bottom'], p) and s.has(el['claw'], p) and macros['3LEDGE'](s),
#		                                                                           Swamp14Right | Swamp14Top | Swamp14Bottom + (LEDGE | claw | hook)
		'Swamp_14_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp14Right'], p) or s.has(el['Swamp14Top'], p) or s.has(el['Swamp14Bottom'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                                           Swamp14Bottom | Swamp14Right
		'Swamp_14_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp14Bottom'], p) or s.has(el['Swamp14Right'], p),
#		                                                                           Swamp15Left + swim + mask
		'Swamp_15_GAMEPLAY.BP_e2052_Toad'                                         : lambda s : s.has(el['Swamp15Left'], p) and s.has(el['swim'], p) and s.has(el['mask'], p),
#		                                                                           Swamp15Top
		'Swamp_15_GAMEPLAY.BP_SCR_LV1M_2171_2'                                    : lambda s : s.has(el['Swamp15Top'], p),
#		                                                                           Swamp15Top | Swamp15Right + (champion | djump | silva + dodge)
		'Swamp_15_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp15Top'], p) or s.has(el['Swamp15Right'], p) and (s.has(el['champion'], p) or s.has(el['djump'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)),
#		                                                                           Swamp15Left | Swamp15Right + LEDGE
		'Swamp_15_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp15Left'], p) or s.has(el['Swamp15Right'], p) and macros['LEDGE'](s),
#		                                                                           Swamp15Right | Swamp15Left + (claw | hook) | Swamp15Top
		'Swamp_15_GAMEPLAY.BP_WorldTravelVolume4'                                 : lambda s : s.has(el['Swamp15Right'], p) or s.has(el['Swamp15Left'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p)) or s.has(el['Swamp15Top'], p),
#		                                                                           Swamp16Top | Swamp16Left
		'Swamp_16_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.has(el['Swamp16Top'], p) or s.has(el['Swamp16Left'], p),
#		                                                                           Swamp16Top | Lab5
		'Swamp_16_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp16Top'], p) or s.can_reach(el['Lab5'], 'Location', p),
#		                                                                           Swamp16Left | Lab5
		'Swamp_16_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp16Left'], p) or s.can_reach(el['Lab5'], 'Location', p),
#		                                                                           Swamp17Left | Swamp17Right
		'Swamp_17_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp17Left'], p) or s.has(el['Swamp17Right'], p),
#		                                                                           Swamp17Right | Swamp17Left
		'Swamp_17_GAMEPLAY.BP_WorldTravelVolume2'                                 : lambda s : s.has(el['Swamp17Right'], p) or s.has(el['Swamp17Left'], p),
#		                                                                           Faden
		'Swamp_18_GAMEPLAY.BP_Interactable_Item_Tip3'                             : lambda s : s.can_reach(el['Faden'], 'Location', p),
#		                                                                           Faden
		'Swamp_18_GAMEPLAY.BP_Interactable_Item_Tip4'                             : lambda s : s.can_reach(el['Faden'], 'Location', p),
#		                                                                           Swamp18Right
		'Swamp_18_GAMEPLAY.BP_Interactable_Spirit_s5080_2'                        : lambda s : s.has(el['Swamp18Right'], p),
#		                                                                           Faden + claw + (3LEDGE | sinner + 2LEDGE | FULLSILVA | dodge + silva + champion | 2HORIZONTAL + champion + djump)
		'Swamp_18_GAMEPLAY.BP_SCR_LV1LL_miliel_2'                                 : lambda s : s.can_reach(el['Faden'], 'Location', p) and s.has(el['claw'], p) and (macros['3LEDGE'](s) or s.has(el['sinner'], p) and macros['2LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['dodge'], p) and s.has(el['silva'], p) and s.has(el['champion'], p) or macros['2HORIZONTAL'](s) and s.has(el['champion'], p) and s.has(el['djump'], p)),
#		                                                                           Swamp18Bottom | Faden + unlock
		'Swamp_18_GAMEPLAY.BP_WorldTravelVolume_2'                                : lambda s : s.has(el['Swamp18Bottom'], p) or s.can_reach(el['Faden'], 'Location', p) and s.has(el['unlock'], p),
#		                                                                           Swamp18Right | Faden
		'Swamp_18_GAMEPLAY.BP_WorldTravelVolume3'                                 : lambda s : s.has(el['Swamp18Right'], p) or s.can_reach(el['Faden'], 'Location', p),
#		                                                                           Swamp2Top
		'Swamp_2_GAMEPLAY.BP_SCR_LV2S_2010_2'                                     : lambda s : s.has(el['Swamp2Top'], p),
#		                                                                           Swamp2Top + (claw | LEDGE + hook)
		'Swamp_2_GAMEPLAY.BP_SCR_LV2S_2121_1'                                     : lambda s : s.has(el['Swamp2Top'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) and s.has(el['hook'], p)),
#		                                                                           Swamp2Right | Swamp2Top + (dash | dodge)
		'Swamp_2_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Swamp2Right'], p) or s.has(el['Swamp2Top'], p) and (s.has(el['dash'], p) or s.has(el['dodge'], p)),
#		                                                                           Swamp2Top | Swamp2Right
		'Swamp_2_GAMEPLAY.BP_WorldTravelVolume2'                                  : lambda s : s.has(el['Swamp2Top'], p) or s.has(el['Swamp2Right'], p),
#		                                                                           Swamp3Top + LEDGE
		'Swamp_3_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                   : lambda s : s.has(el['Swamp3Top'], p) and macros['LEDGE'](s),
#		                                                                           Swamp3Top
		'Swamp_3_GAMEPLAY.BP_SCR_LV1L_2170_3'                                     : lambda s : s.has(el['Swamp3Top'], p),
#		                                                                           Swamp3Left | Swamp3Bottom
		'Swamp_3_GAMEPLAY.BP_WorldTravelVolume_2'                                 : lambda s : s.has(el['Swamp3Left'], p) or s.has(el['Swamp3Bottom'], p),
#		                                                                           Swamp3Top | Swamp3Left + LEDGE
		'Swamp_3_GAMEPLAY.BP_WorldTravelVolume2'                                  : lambda s : s.has(el['Swamp3Top'], p) or s.has(el['Swamp3Left'], p) and macros['LEDGE'](s),
#		                                                                           Swamp3Right | Swamp3Bottom | Swamp3Top
		'Swamp_3_GAMEPLAY.BP_WorldTravelVolume3'                                  : lambda s : s.has(el['Swamp3Right'], p) or s.has(el['Swamp3Bottom'], p) or s.has(el['Swamp3Top'], p),
#		                                                                           Swamp3Bottom | Swamp3Top | Swamp3Right
		'Swamp_3_GAMEPLAY.BP_WorldTravelVolume4'                                  : lambda s : s.has(el['Swamp3Bottom'], p) or s.has(el['Swamp3Top'], p) or s.has(el['Swamp3Right'], p),
#		                                                                           Village01Right | Village01Bottom
		'Village_01_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village01Right'], p) or s.has(el['Village01Bottom'], p),
#		                                                                           Village01Bottom | Village01Right
		'Village_01_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village01Bottom'], p) or s.has(el['Village01Right'], p),
#		                                                                           Village02Left
		'Village_02_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_Drop'                : lambda s : s.has(el['Village02Left'], p),
#		                                                                           Village02Left + (djump + (silva | champion) | (djump | silva) + HORIZONTAL | hook)
		'Village_02_GAMEPLAY.BP_SCR_LV1S_2020_2'                                  : lambda s : s.has(el['Village02Left'], p) and (s.has(el['djump'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p)) or (s.has(el['djump'], p) or s.has(el['silva'], p)) and macros['HORIZONTAL'](s) or s.has(el['hook'], p)),
#		                                                                           Village02Left + (2LEDGE | silva + dodge | hook +  (LEDGE | claw))
		'Village_02_GAMEPLAY.BP_SCR_LV1S_2100_2'                                  : lambda s : s.has(el['Village02Left'], p) and (macros['2LEDGE'](s) or s.has(el['silva'], p) and s.has(el['dodge'], p) or s.has(el['hook'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p))),
#		                                                                           Village02Right | Village02Bottom | Village02Left + (LEDGE | claw)
		'Village_02_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village02Right'], p) or s.has(el['Village02Bottom'], p) or s.has(el['Village02Left'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Village02Left | Village02Bottom
		'Village_02_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village02Left'], p) or s.has(el['Village02Bottom'], p),
#		                                                                           Village02Bottom | Village02Right
		'Village_02_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village02Bottom'], p) or s.has(el['Village02Right'], p),
#		                                                                           slam + (Village03Right + (LEDGE | HORIZONTAL) | Village03Bottom1 + (LEDGE | claw))
		'Village_03_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                   : lambda s : s.has(el['slam'], p) and (s.has(el['Village03Right'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.has(el['Village03Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p))),
#		                                                                           Village03Right + (claw | hook | LEDGE | HORIZONTAL | dash)
		'Village_03_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                 : lambda s : s.has(el['Village03Right'], p) and (s.has(el['claw'], p) or s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                                           Village03Right + (LEDGE | HORIZONTAL | hook | dash) | Village03Bottom1 + (LEDGE | claw)
		'Village_03_GAMEPLAY.BP_SCR_LV1S_2021_2'                                  : lambda s : s.has(el['Village03Right'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)) or s.has(el['Village03Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           slam + (Village03Right + (LEDGE | HORIZONTAL | hook | dash) | Village03Bottom1 + (LEDGE | claw))
		'Village_03_GAMEPLAY.BP_SCR_LV2S_2020_2'                                  : lambda s : s.has(el['slam'], p) and (s.has(el['Village03Right'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)) or s.has(el['Village03Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p))),
#		                                                                           Village03Bottom1 | Village03Right + (HORIZONTAL | LEDGE | hook | dash)
		'Village_03_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village03Bottom1'], p) or s.has(el['Village03Right'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)),
#		                                                                           Village03Right | Village03Bottom1 + (LEDGE | claw)
		'Village_03_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village03Right'], p) or s.has(el['Village03Bottom1'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                                           Village03Bottom2 | Village03Right + slam
		'Village_03_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village03Bottom2'], p) or s.has(el['Village03Right'], p) and s.has(el['slam'], p),
#		                                                                           Village041Bottom
		'Village_04_1_GAMEPLAY.BP_e2102_Crow'                                     : lambda s : s.has(el['Village041Bottom'], p),
#		                                                                           Village041Bottom
		'Village_04_1_GAMEPLAY.BP_WorldTravelVolume_2'                            : lambda s : s.has(el['Village041Bottom'], p),
#		                                                                           Village04Top
		'Village_04_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                   : lambda s : s.has(el['Village04Top'], p),
#		                                                                           Village04Right + (hook + (LEDGE | claw) | LEDGE + HORIZONTAL | 2LEDGE | LEDGE + claw)
		'Village_04_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                 : lambda s : s.has(el['Village04Right'], p) and (s.has(el['hook'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p)),
#		                                                                           Village04Top | Village04Right
		'Village_04_GAMEPLAY.BP_Interactable_WorldTravel_2'                       : lambda s : s.has(el['Village04Top'], p) or s.has(el['Village04Right'], p),
#		                                                                           Village04Top
		'Village_04_GAMEPLAY.BP_SCR_LV1S_2010_1'                                  : lambda s : s.has(el['Village04Top'], p),
#		                                                                           Village04Right | Village04Top
		'Village_04_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village04Right'], p) or s.has(el['Village04Top'], p),
#		                                                                           Village05Top | Village05Left | Village05Right
		'Village_05_GAMEPLAY.BP_Interactable_Item_Tip4'                           : lambda s : s.has(el['Village05Top'], p) or s.has(el['Village05Left'], p) or s.has(el['Village05Right'], p),
#		                                                                           Village05Top | CollapsedShack
		'Village_05_GAMEPLAY.BP_Interactable_WorldTravel_2'                       : lambda s : s.has(el['Village05Top'], p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                                           Village05Left | CollapsedShack
		'Village_05_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village05Left'], p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                                           Village05Right | CollapsedShack
		'Village_05_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village05Right'], p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                                           Village06Left
		'Village_06_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                   : lambda s : s.has(el['Village06Left'], p),
#		                                                                           Village06Right2 + (2LEDGE | LEDGE + claw | (silva | djump) + HORIZONTAL | champion + sinner)
		'Village_06_GAMEPLAY.BP_SCR_LV1M_2000_3'                                  : lambda s : s.has(el['Village06Right2'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or (s.has(el['silva'], p) or s.has(el['djump'], p)) and macros['HORIZONTAL'](s) or s.has(el['champion'], p) and s.has(el['sinner'], p)),
#		                                                                           Village06Left + slam + (2LEDGE | LEDGE + claw | hook)
		'Village_06_GAMEPLAY.BP_SCR_LV1S_2020_2'                                  : lambda s : s.has(el['Village06Left'], p) and s.has(el['slam'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                                           Village06Left + slam + (2LEDGE | LEDGE + claw | hook)
		'Village_06_GAMEPLAY.BP_SCR_LV1S_2021_2'                                  : lambda s : s.has(el['Village06Left'], p) and s.has(el['slam'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                                           Village06Left + (LEDGE | hook)
		'Village_06_GAMEPLAY.BP_SCR_LV2S_2010_3'                                  : lambda s : s.has(el['Village06Left'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Village06Left + slam + (LEDGE | hook)
		'Village_06_GAMEPLAY.BP_SCR_LV2S_2021_2'                                  : lambda s : s.has(el['Village06Left'], p) and s.has(el['slam'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Village06Left | Village06Right2 + LEDGE + claw
		'Village_06_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village06Left'], p) or s.has(el['Village06Right2'], p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                                           Village06Right1 | Village06Right2 + (LEDGE | HORIZONTAL)
		'Village_06_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village06Right1'], p) or s.has(el['Village06Right2'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                                           Village06Bottom | Village06Left + slam
		'Village_06_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village06Bottom'], p) or s.has(el['Village06Left'], p) and s.has(el['slam'], p),
#		                                                                           Village06Right2 | Village06Left + (hook | LEDGE) | Village06Right1
		'Village_06_GAMEPLAY.BP_WorldTravelVolume4'                               : lambda s : s.has(el['Village06Right2'], p) or s.has(el['Village06Left'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s)) or s.has(el['Village06Right1'], p),
#		                                                                           Village07Left
		'Village_07_GAMEPLAY.BP_Interactable_Item_PassiveSlot_2'                  : lambda s : s.has(el['Village07Left'], p),
#		                                                                           Village07Left
		'Village_07_GAMEPLAY.BP_SCR_LV1S_2100_3'                                  : lambda s : s.has(el['Village07Left'], p),
#		                                                                           Village07Left + (hook | 2LEDGE)
		'Village_07_GAMEPLAY.BP_SCR_LV2S_2080_3'                                  : lambda s : s.has(el['Village07Left'], p) and (s.has(el['hook'], p) or macros['2LEDGE'](s)),
#		                                                                           Village07Left | Village07Right
		'Village_07_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village07Left'], p) or s.has(el['Village07Right'], p),
#		                                                                           Village07Right | Village07Left | Village07Top
		'Village_07_GAMEPLAY.BP_WorldTravelVolume2_5'                             : lambda s : s.has(el['Village07Right'], p) or s.has(el['Village07Left'], p) or s.has(el['Village07Top'], p),
#		                                                                           Village07Top | Village07Right + (hook | LEDGE + sinner | djump + (dodge | silva | champion) | dodge + (silva | champion + dash))
		'Village_07_GAMEPLAY.BP_WorldTravelVolume3_8'                             : lambda s : s.has(el['Village07Top'], p) or s.has(el['Village07Right'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['djump'], p) and (s.has(el['dodge'], p) or s.has(el['silva'], p) or s.has(el['champion'], p)) or s.has(el['dodge'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p) and s.has(el['dash'], p))),
#		                                                                           Village08Left
		'Village_08_GAMEPLAY.BP_e2002_Knight'                                     : lambda s : s.has(el['Village08Left'], p),
#		                                                                           Village08Left
		'Village_08_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_2'                   : lambda s : s.has(el['Village08Left'], p),
#		                                                                           Village08Left + swim
		'Village_08_GAMEPLAY.BP_SCR_LV1S_2021_2'                                  : lambda s : s.has(el['Village08Left'], p) and s.has(el['swim'], p),
#		                                                                           Village08Left | Village08Right
		'Village_08_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village08Left'], p) or s.has(el['Village08Right'], p),
#		                                                                           Village08Right | Village08Left
		'Village_08_GAMEPLAY.BP_WorldTravelVolume2_5'                             : lambda s : s.has(el['Village08Right'], p) or s.has(el['Village08Left'], p),
#		                                                                           BridgeHead
		'Village_09_GAMEPLAY.BP_Interactable_Item_Tip3'                           : lambda s : s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                                           Village09Right1 | Village09Right2 | Village09Left1 | Village09Left2
		'Village_09_GAMEPLAY.BP_Interactable_Item_Tip4'                           : lambda s : s.has(el['Village09Right1'], p) or s.has(el['Village09Right2'], p) or s.has(el['Village09Left1'], p) or s.has(el['Village09Left2'], p),
#		                                                                           Village09Right1 | BridgeHead
		'Village_09_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village09Right1'], p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                                           Village09Right2 | BridgeHead + swim
		'Village_09_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village09Right2'], p) or s.can_reach(el['BridgeHead'], 'Location', p) and s.has(el['swim'], p),
#		                                                                           Village09Left1 | BridgeHead
		'Village_09_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village09Left1'], p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                                           Village09Left2 | BridgeHead
		'Village_09_GAMEPLAY.BP_WorldTravelVolume4'                               : lambda s : s.has(el['Village09Left2'], p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                                           Village10Left | Village10Right
		'Village_10_GAMEPLAY.BP_e5050_Giant'                                      : lambda s : s.has(el['Village10Left'], p) or s.has(el['Village10Right'], p),
#		                                                                           Gerrod
		'Village_10_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.can_reach(el['Gerrod'], 'Location', p),
#		                                                                           Gerrod
		'Village_10_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.can_reach(el['Gerrod'], 'Location', p),
#		                                                                           Village111Bottom + slam
		'Village_11_1_GAMEPLAY.BP_Interactable_Item_HealPower_Up_5'               : lambda s : s.has(el['Village111Bottom'], p) and s.has(el['slam'], p),
#		                                                                           Village111Bottom
		'Village_11_1_GAMEPLAY.BP_WorldTravelVolume_2'                            : lambda s : s.has(el['Village111Bottom'], p),
#		                                                                           Village11Left
		'Village_11_GAMEPLAY.BP_Interactable_Item_Tip1'                           : lambda s : s.has(el['Village11Left'], p),
#		                                                                           Village11Left
		'Village_11_GAMEPLAY.BP_Interactable_Item_Tip4'                           : lambda s : s.has(el['Village11Left'], p),
#		                                                                           Village11Top | Village11Left
		'Village_11_GAMEPLAY.BP_Interactable_WorldTravel_2'                       : lambda s : s.has(el['Village11Top'], p) or s.has(el['Village11Left'], p),
#		                                                                           Village11Left
		'Village_11_GAMEPLAY.BP_SCR_LV2S_2020_3'                                  : lambda s : s.has(el['Village11Left'], p),
#		                                                                           Village11Left | Village11Right + claw
		'Village_11_GAMEPLAY.BP_WorldTravelVolume_4'                              : lambda s : s.has(el['Village11Left'], p) or s.has(el['Village11Right'], p) and s.has(el['claw'], p),
#		                                                                           Village11Right | Village11Left + claw
		'Village_11_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village11Right'], p) or s.has(el['Village11Left'], p) and s.has(el['claw'], p),
#		                                                                           Village12Left1
		'Village_12_GAMEPLAY.BP_SCR_LV1S_2021_2'                                  : lambda s : s.has(el['Village12Left1'], p),
#		                                                                           Village12Top
		'Village_12_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village12Top'], p),
#		                                                                           Village12Left1 | Village12Right + Village12Top
		'Village_12_GAMEPLAY.BP_WorldTravelVolume2'                               : lambda s : s.has(el['Village12Left1'], p) or s.has(el['Village12Right'], p) and s.has(el['Village12Top'], p),
#		                                                                           Village12Right | Village12Left1 + Village12Top + swim
		'Village_12_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village12Right'], p) or s.has(el['Village12Left1'], p) and s.has(el['Village12Top'], p) and s.has(el['swim'], p),
#		                                                                           Village12Left2 | Village12Left1 + CHARGE
		'Village_12_GAMEPLAY.BP_WorldTravelVolume4'                               : lambda s : s.has(el['Village12Left2'], p) or s.has(el['Village12Left1'], p) and macros['CHARGE'](s),
#		                                                                           Village13Right + (djump | 2LEDGE | LEDGE + HORIZONTAL)
		'Village_13_GAMEPLAY.BP_Interactable_Item_MaxHPUp_02_Treasure_2'          : lambda s : s.has(el['Village13Right'], p) and (s.has(el['djump'], p) or macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                                           Village13Right
		'Village_13_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop'               : lambda s : s.has(el['Village13Right'], p),
#		                                                                           Village13Left + swim
		'Village_13_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                 : lambda s : s.has(el['Village13Left'], p) and s.has(el['swim'], p),
#		                                                                           Village13Left
		'Village_13_GAMEPLAY.BP_SCR_LV1S_2021_2'                                  : lambda s : s.has(el['Village13Left'], p),
#		                                                                           Village13Top | Village13Right + LEDGE
		'Village_13_GAMEPLAY.BP_WorldTravelVolume4'                               : lambda s : s.has(el['Village13Top'], p) or s.has(el['Village13Right'], p) and macros['LEDGE'](s),
#		                                                                           Village13Left | Village13Right
		'Village_13_GAMEPLAY.BP_WorldTravelVolume5'                               : lambda s : s.has(el['Village13Left'], p) or s.has(el['Village13Right'], p),
#		                                                                           Village13Right | Village13Top
		'Village_13_GAMEPLAY.BP_WorldTravelVolume6'                               : lambda s : s.has(el['Village13Right'], p) or s.has(el['Village13Top'], p),
#		                                                                           Village14Bottom + (LEDGE | hook)
		'Village_14_GAMEPLAY.BP_e2112_Ork'                                        : lambda s : s.has(el['Village14Bottom'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                                           Elder + (slam + (hook | LEDGE + sinner | silva + (djump | dodge) | champion + (dash | claw) + (silva | djump)))
		'Village_14_GAMEPLAY.BP_SCR_LV1L_2111_2'                                  : lambda s : s.can_reach(el['Elder'], 'Location', p) and (s.has(el['slam'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['silva'], p) and (s.has(el['djump'], p) or s.has(el['dodge'], p)) or s.has(el['champion'], p) and (s.has(el['dash'], p) or s.has(el['claw'], p)) and (s.has(el['silva'], p) or s.has(el['djump'], p)))),
#		                                                                           Elder + (slam + (hook | 3LEDGE | FULLSILVA | claw + LEDGE) )
		'Village_14_GAMEPLAY.BP_SCR_LV2L_2110_3'                                  : lambda s : s.can_reach(el['Elder'], 'Location', p) and (s.has(el['slam'], p) and (s.has(el['hook'], p) or macros['3LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['claw'], p) and macros['LEDGE'](s))),
#		                                                                           Village14Bottom
		'Village_14_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village14Bottom'], p),
#		                                                                           Village15Left + swim + (claw + (sinner + (djump | champion) | dodge + silva | 2LEDGE + HORIZONTAL) | hook + (2LEDGE | claw + (LEDGE | HORIZONTAL))) | Village15Right + claw + djump + silva
		'Village_15_GAMEPLAY.BP_SCR_LV1LL_0000_2'                                 : lambda s : s.has(el['Village15Left'], p) and s.has(el['swim'], p) and (s.has(el['claw'], p) and (s.has(el['sinner'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p)) or s.has(el['dodge'], p) and s.has(el['silva'], p) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s)) or s.has(el['hook'], p) and (macros['2LEDGE'](s) or s.has(el['claw'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)))) or s.has(el['Village15Right'], p) and s.has(el['claw'], p) and s.has(el['djump'], p) and s.has(el['silva'], p),
#		                                                                           Village15Right + swim
		'Village_15_GAMEPLAY.BP_SCR_LV1M_2050_3'                                  : lambda s : s.has(el['Village15Right'], p) and s.has(el['swim'], p),
#		                                                                           Village15Left + swim
		'Village_15_GAMEPLAY.BP_SCR_LV2M_2050_2'                                  : lambda s : s.has(el['Village15Left'], p) and s.has(el['swim'], p),
#		                                                                           Village15Left | Village15Right + swim
		'Village_15_GAMEPLAY.BP_WorldTravelVolume_2'                              : lambda s : s.has(el['Village15Left'], p) or s.has(el['Village15Right'], p) and s.has(el['swim'], p),
#		                                                                           Village15Right | Village15Left + Village800
		'Village_15_GAMEPLAY.BP_WorldTravelVolume2_5'                             : lambda s : s.has(el['Village15Right'], p) or s.has(el['Village15Left'], p) and s.can_reach(el['Village800'], 'Location', p),
#		                                                                           Village16Right
		'Village_16_GAMEPLAY.BP_Interactable_Item_Tip4'                           : lambda s : s.has(el['Village16Right'], p),
#		                                                                           Village16Right
		'Village_16_GAMEPLAY.BP_Interactable_Passives_Treasure_2'                 : lambda s : s.has(el['Village16Right'], p),
#		                                                                           Village16Right
		'Village_16_GAMEPLAY.BP_WorldTravelVolume3'                               : lambda s : s.has(el['Village16Right'], p),

		'starting_weapon'                                                         : lambda s : True,
		'Ending_A'                                                                : lambda s : s.has(el['Outside02Left'], p),
		'Ending_B'                                                                : lambda s : s.has(el['Abyss03Left'], p),
		'Ending_C'                                                                : lambda s : s.has(el['Abyss03Left'], p) and (s.count("Generic.i_FinalPassivePart_Up", p) == 7),

	}

	items_rules : Dict[str, ItemRule] = {
		'starting_weapon' : lambda item : item.player == p and item.name.startswith('Spirit.'),
	}

	return (locations_rules, items_rules)
