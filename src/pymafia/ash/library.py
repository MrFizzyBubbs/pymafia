"""Automatically generated Python implementations of KoLmafia's ASH functions.

See `scripts/generate_ash_library.py` for more information.
"""

__all__ = [
    "abort",
    "absorbed_monsters",
    "add_item_condition",
    "adv1",
    "adv_cost",
    "adventure",
    "all_monsters_with_id",
    "all_normal_outfits",
    "appearance_rates",
    "append",
    "append_replacement",
    "append_tail",
    "attack",
    "autosell",
    "autosell_price",
    "available_amount",
    "available_choice_options",
    "available_choice_select_inputs",
    "available_choice_text_inputs",
    "available_pocket",
    "banished_by",
    "batch_close",
    "batch_open",
    "bjornify_familiar",
    "black_market_available",
    "boolean_modifier",
    "buffed_hit_stat",
    "buffer_to_file",
    "buy",
    "buy_price",
    "buy_using_storage",
    "buys_item",
    "can_adventure",
    "can_drink",
    "can_eat",
    "can_equip",
    "can_faxbot",
    "can_interact",
    "can_still_steal",
    "canadia_available",
    "candy_for_tier",
    "ceil",
    "change_mcd",
    "char_at",
    "chat_clan",
    "chat_macro",
    "chat_notify",
    "chat_private",
    "chew",
    "choice_follows_fight",
    "class_modifier",
    "clear",
    "clear_booze_helper",
    "clear_food_helper",
    "cli_execute",
    "cli_execute_output",
    "closet_amount",
    "combat_mana_cost_modifier",
    "combat_rate_modifier",
    "combat_skill_available",
    "concoction_price",
    "contains_text",
    "council",
    "count",
    "craft",
    "craft_type",
    "creatable_amount",
    "creatable_turns",
    "create",
    "create_matcher",
    "current_hit_stat",
    "current_mcd",
    "current_pvp_stances",
    "current_rad_sickness",
    "current_round",
    "curse",
    "dad_sea_monkee_weakness",
    "daily_special",
    "damage_absorption_percent",
    "damage_reduction",
    "dart_parts_to_skills",
    "dart_skills_to_parts",
    "date_to_timestamp",
    "daycount",
    "debugprint",
    "delete",
    "desc_to_effect",
    "desc_to_item",
    "disable",
    "dispensary_available",
    "display_amount",
    "drink",
    "drinksilent",
    "dump",
    "eat",
    "eatsilent",
    "effect_fact",
    "effect_modifier",
    "effect_pockets",
    "eight_bit_points",
    "elemental_resistance",
    "empty_closet",
    "enable",
    "end",
    "ends_with",
    "enthrone_familiar",
    "entity_decode",
    "entity_encode",
    "equip",
    "equip_all_familiars",
    "equipped_amount",
    "equipped_item",
    "eudora",
    "eudora_item",
    "every_card_name",
    "expected_cold_medicine_cabinet",
    "expected_damage",
    "experience_bonus",
    "expression_eval",
    "extract_items",
    "extract_meat",
    "fact_type",
    "familiar_equipment",
    "familiar_equipped_equipment",
    "familiar_weight",
    "favorite_familiars",
    "faxbot",
    "fight_follows_choice",
    "file_to_array",
    "file_to_buffer",
    "file_to_map",
    "find",
    "floor",
    "florist_available",
    "flush_monster_manuel_cache",
    "form_field",
    "form_fields",
    "format_date_time",
    "friars_available",
    "fuel_cost",
    "fullness_limit",
    "gameday_to_int",
    "gameday_to_string",
    "gametime_to_int",
    "get_all_properties",
    "get_auto_attack",
    "get_autumnaton_locations",
    "get_campground",
    "get_ccs_action",
    "get_chateau",
    "get_clan_id",
    "get_clan_lounge",
    "get_clan_name",
    "get_clan_rumpus",
    "get_closet",
    "get_counter",
    "get_counters",
    "get_custom_outfits",
    "get_display",
    "get_dwelling",
    "get_fishing_locations",
    "get_florist_plants",
    "get_free_pulls",
    "get_fuel",
    "get_goals",
    "get_ignore_zone_warnings",
    "get_ingredients",
    "get_inventory",
    "get_location_monsters",
    "get_locket_monsters",
    "get_monster_mapping",
    "get_monsters",
    "get_moods",
    "get_outfits",
    "get_path",
    "get_path_full",
    "get_path_variables",
    "get_permed_skills",
    "get_player_id",
    "get_player_name",
    "get_power",
    "get_property",
    "get_related",
    "get_revision",
    "get_shop",
    "get_shop_log",
    "get_stack_trace",
    "get_stash",
    "get_storage",
    "get_version",
    "get_workshed",
    "get_zap_wand",
    "git_at_head",
    "git_exists",
    "git_info",
    "git_list",
    "gnomads_available",
    "goal_exists",
    "group",
    "group_count",
    "group_names",
    "group_string",
    "guild_available",
    "guild_store_available",
    "handling_choice",
    "has_queued_commands",
    "have_bartender",
    "have_chef",
    "have_display",
    "have_effect",
    "have_equipped",
    "have_familiar",
    "have_mushroom_plot",
    "have_outfit",
    "have_servant",
    "have_shop",
    "have_skill",
    "hedge_maze",
    "heist",
    "heist_targets",
    "hermit",
    "hidden_temple_unlocked",
    "hippy_stone_broken",
    "hippy_store_available",
    "historical_age",
    "historical_price",
    "holiday",
    "hp_cost",
    "image_to_monster",
    "in_bad_moon",
    "in_casual",
    "in_hardcore",
    "in_moxie_sign",
    "in_multi_fight",
    "in_muscle_sign",
    "in_mysticality_sign",
    "in_terrarium",
    "inaccessible_reason",
    "index_of",
    "inebriety_limit",
    "initiative_modifier",
    "insert",
    "is_accessible",
    "is_adventuring",
    "is_banished",
    "is_coinmaster_item",
    "is_dark_mode",
    "is_discardable",
    "is_displayable",
    "is_familiar_equipment_locked",
    "is_giftable",
    "is_goal",
    "is_headless",
    "is_integer",
    "is_npc_item",
    "is_online",
    "is_removable",
    "is_shruggable",
    "is_tradeable",
    "is_trendy",
    "is_unrestricted",
    "is_wearing_outfit",
    "item_amount",
    "item_drop_modifier",
    "item_drops",
    "item_drops_array",
    "item_fact",
    "item_pockets",
    "item_type",
    "join_strings",
    "joke_pockets",
    "jump_chance",
    "knoll_available",
    "last_choice",
    "last_decision",
    "last_index_of",
    "last_item_message",
    "last_monster",
    "last_skill_message",
    "leetify",
    "length",
    "lightning_cost",
    "limit_mode",
    "load_html",
    "lock_familiar_equipment",
    "log_n",
    "logprint",
    "make_url",
    "mall_price",
    "mall_prices",
    "mana_cost_modifier",
    "map_to_file",
    "max",
    "maximize",
    "meat_drop",
    "meat_drop_modifier",
    "meat_pockets",
    "min",
    "minstrel_instrument",
    "minstrel_level",
    "minstrel_quest",
    "modifier_eval",
    "monkey_paw",
    "monster_attack",
    "monster_defense",
    "monster_element",
    "monster_eval",
    "monster_factoids_available",
    "monster_hp",
    "monster_initiative",
    "monster_level_adjustment",
    "monster_manuel_text",
    "monster_modifier",
    "monster_phylum",
    "monster_pockets",
    "mood_execute",
    "mood_list",
    "moon_light",
    "moon_phase",
    "mp_cost",
    "my_absorbs",
    "my_adventures",
    "my_ascensions",
    "my_audience",
    "my_basestat",
    "my_bjorned_familiar",
    "my_buffedstat",
    "my_class",
    "my_closet_meat",
    "my_companion",
    "my_daycount",
    "my_discomomentum",
    "my_effective_familiar",
    "my_effects",
    "my_enthroned_familiar",
    "my_familiar",
    "my_fullness",
    "my_fury",
    "my_garden_type",
    "my_hash",
    "my_hp",
    "my_id",
    "my_inebriety",
    "my_level",
    "my_lightning",
    "my_location",
    "my_mask",
    "my_maxfury",
    "my_maxhp",
    "my_maxmp",
    "my_maxpp",
    "my_meat",
    "my_mp",
    "my_name",
    "my_path",
    "my_path_id",
    "my_poke_fam",
    "my_pp",
    "my_primestat",
    "my_rain",
    "my_robot_energy",
    "my_robot_scraps",
    "my_servant",
    "my_session_adv",
    "my_session_items",
    "my_session_meat",
    "my_session_results",
    "my_sign",
    "my_soulsauce",
    "my_spleen_use",
    "my_storage_meat",
    "my_thrall",
    "my_thunder",
    "my_total_turns_spent",
    "my_turncount",
    "my_vykea_companion",
    "my_wildfire_water",
    "now_to_int",
    "now_to_string",
    "npc_price",
    "numberology_prize",
    "numeric_fact",
    "numeric_modifier",
    "outfit",
    "outfit_pieces",
    "outfit_tattoo",
    "outfit_treats",
    "overdrink",
    "path_id_to_name",
    "path_name_to_id",
    "pick_pocket",
    "picked_pockets",
    "picked_scraps",
    "ping",
    "pocket_effects",
    "pocket_items",
    "pocket_joke",
    "pocket_meat",
    "pocket_monster",
    "pocket_poem",
    "pocket_scrap",
    "pocket_stats",
    "poem_pockets",
    "potential_pockets",
    "pre_validate_adventure",
    "prepare_for_adventure",
    "print",
    "print_html",
    "property_default_value",
    "property_exists",
    "property_has_default",
    "pulls_remaining",
    "put_closet",
    "put_display",
    "put_shop",
    "put_shop_using_storage",
    "put_stash",
    "pvp_attacks_left",
    "rain_cost",
    "random",
    "raw_damage_absorption",
    "read_ccs",
    "receive_fax",
    "refresh_shop",
    "refresh_stash",
    "refresh_status",
    "remove_item_condition",
    "remove_property",
    "rename_property",
    "replace",
    "replace_all",
    "replace_first",
    "replace_string",
    "reprice_shop",
    "reset",
    "restoration_pockets",
    "restore_hp",
    "restore_mp",
    "retrieve_item",
    "retrieve_price",
    "reverse_numberology",
    "rollover",
    "round",
    "run_choice",
    "run_combat",
    "run_turn",
    "runaway",
    "sausage_goblin_chance",
    "scrap_pockets",
    "sell",
    "sell_price",
    "sells_item",
    "send_fax",
    "session_logs",
    "set_auto_attack",
    "set_ccs",
    "set_length",
    "set_location",
    "set_property",
    "shop_amount",
    "shop_limit",
    "shop_price",
    "skill_modifier",
    "slash_count",
    "soulsauce_cost",
    "spleen_limit",
    "split_modifiers",
    "split_string",
    "square_root",
    "start",
    "starts_with",
    "stash_amount",
    "stat_bonus_today",
    "stat_bonus_tomorrow",
    "stat_modifier",
    "stats_pockets",
    "steal",
    "stills_available",
    "stop_counter",
    "storage_amount",
    "string_fact",
    "string_modifier",
    "stun_skill",
    "substring",
    "svn_at_head",
    "svn_exists",
    "svn_info",
    "svn_list",
    "sweet_synthesis",
    "sweet_synthesis_pair",
    "sweet_synthesis_pairing",
    "sweet_synthesis_result",
    "take_closet",
    "take_display",
    "take_shop",
    "take_stash",
    "take_storage",
    "tavern",
    "throw_item",
    "throw_items",
    "thunder_cost",
    "time_to_string",
    "timestamp_to_date",
    "to_boolean",
    "to_bounty",
    "to_buffer",
    "to_class",
    "to_coinmaster",
    "to_effect",
    "to_element",
    "to_familiar",
    "to_float",
    "to_int",
    "to_item",
    "to_json",
    "to_location",
    "to_lower_case",
    "to_modifier",
    "to_monster",
    "to_path",
    "to_phylum",
    "to_plural",
    "to_servant",
    "to_skill",
    "to_slot",
    "to_stat",
    "to_string",
    "to_thrall",
    "to_upper_case",
    "to_url",
    "to_vykea",
    "to_wiki_url",
    "today_to_string",
    "total_free_rests",
    "total_turns_played",
    "tower_door",
    "traceprint",
    "track_copy_count",
    "track_ignore_queue",
    "tracked_by",
    "truncate",
    "turns_per_cast",
    "turns_played",
    "twiddle",
    "unusual_construct_disc",
    "update_candy_prices",
    "url_decode",
    "url_encode",
    "use",
    "use_familiar",
    "use_servant",
    "use_skill",
    "user_confirm",
    "user_notify",
    "user_prompt",
    "visit",
    "visit_url",
    "voting_booth_initiatives",
    "wait",
    "waitq",
    "weapon_hands",
    "weapon_type",
    "weight_adjustment",
    "well_stocked",
    "white_citadel_available",
    "who_clan",
    "will_usually_dodge",
    "will_usually_miss",
    "write",
    "write_ccs",
    "writeln",
    "xpath",
    "zap",
]

from typing import Any, overload

from pymafia.ash.function import LibraryFunction
from pymafia.datatypes import (
    Bounty,
    Class,
    Coinmaster,
    Effect,
    Element,
    Familiar,
    Item,
    Location,
    Matcher,
    Modifier,
    Monster,
    Path,
    Phylum,
    Servant,
    Skill,
    Slot,
    Stat,
    Thrall,
    Vykea,
)


@overload
def abort() -> None: ...


@overload
def abort(string: str) -> None: ...


def abort(*args):
    return LibraryFunction("abort")(*args)


def absorbed_monsters() -> dict[Monster, bool]:
    return LibraryFunction("absorbed_monsters")()


@overload
def add_item_condition(item: Item, count: int) -> None: ...


@overload
def add_item_condition(count: int, item: Item) -> None: ...


def add_item_condition(*args):
    return LibraryFunction("add_item_condition")(*args)


@overload
def adv1(locationValue: Location) -> bool: ...


@overload
def adv1(locationValue: Location, adventuresUsedValue: int) -> bool: ...


@overload
def adv1(
    locationValue: Location, adventuresUsedValue: int, filterFunction: str
) -> bool: ...


def adv1(*args):
    return LibraryFunction("adv1")(*args)


def adv_cost(skill: Skill) -> int:
    return LibraryFunction("adv_cost")(skill)


@overload
def adventure(count: int, location: Location, filterFunction: str) -> bool: ...


@overload
def adventure(count: int, location: Location) -> bool: ...


@overload
def adventure(location: Location, count: int, filterFunction: str) -> bool: ...


@overload
def adventure(location: Location, count: int) -> bool: ...


def adventure(*args):
    return LibraryFunction("adventure")(*args)


def all_monsters_with_id() -> dict[Monster, bool]:
    return LibraryFunction("all_monsters_with_id")()


def all_normal_outfits() -> dict[int, str]:
    return LibraryFunction("all_normal_outfits")()


@overload
def appearance_rates(
    location: Location, includeQueue: bool
) -> dict[Monster, float]: ...


@overload
def appearance_rates(location: Location) -> dict[Monster, float]: ...


def appearance_rates(*args):
    return LibraryFunction("appearance_rates")(*args)


def append(buffer: str, s: str) -> str:
    return LibraryFunction("append")(buffer, s)


def append_replacement(matcher: Matcher, buffer: str, replacement: str) -> str:
    return LibraryFunction("append_replacement")(matcher, buffer, replacement)


def append_tail(matcher: Matcher, buffer: str) -> str:
    return LibraryFunction("append_tail")(matcher, buffer)


def attack() -> str:
    return LibraryFunction("attack")()


@overload
def autosell(count: int, item: Item) -> bool: ...


@overload
def autosell(item: Item, count: int) -> bool: ...


def autosell(*args):
    return LibraryFunction("autosell")(*args)


def autosell_price(item: Item) -> int:
    return LibraryFunction("autosell_price")(item)


def available_amount(item: Item) -> int:
    return LibraryFunction("available_amount")(item)


@overload
def available_choice_options(spoilers: bool) -> dict[int, str]: ...


@overload
def available_choice_options() -> dict[int, str]: ...


def available_choice_options(*args):
    return LibraryFunction("available_choice_options")(*args)


def available_choice_select_inputs(decision: int) -> dict[str, dict[str, str]]:
    return LibraryFunction("available_choice_select_inputs")(decision)


def available_choice_text_inputs(decision: int) -> dict[str, str]:
    return LibraryFunction("available_choice_text_inputs")(decision)


@overload
def available_pocket(stat: Stat) -> int: ...


@overload
def available_pocket(item: Item) -> int: ...


@overload
def available_pocket(effect: Effect) -> int: ...


@overload
def available_pocket(monster: Monster) -> int: ...


def available_pocket(*args):
    return LibraryFunction("available_pocket")(*args)


def banished_by(monster: Monster) -> dict[int, str]:
    return LibraryFunction("banished_by")(monster)


def batch_close() -> bool:
    return LibraryFunction("batch_close")()


def batch_open() -> None:
    return LibraryFunction("batch_open")()


def bjornify_familiar(familiar: Familiar) -> bool:
    return LibraryFunction("bjornify_familiar")(familiar)


def black_market_available() -> bool:
    return LibraryFunction("black_market_available")()


@overload
def boolean_modifier(effect: Effect, modifier: Modifier) -> bool: ...


@overload
def boolean_modifier(effect: Effect, modifier: str) -> bool: ...


@overload
def boolean_modifier(item: Item, modifier: Modifier) -> bool: ...


@overload
def boolean_modifier(item: Item, modifier: str) -> bool: ...


@overload
def boolean_modifier(type: str, modifier: Modifier) -> bool: ...


@overload
def boolean_modifier(type: str, modifier: str) -> bool: ...


@overload
def boolean_modifier(modifier: Modifier) -> bool: ...


@overload
def boolean_modifier(modifier: str) -> bool: ...


def boolean_modifier(*args):
    return LibraryFunction("boolean_modifier")(*args)


def buffed_hit_stat() -> int:
    return LibraryFunction("buffed_hit_stat")()


def buffer_to_file(buffer: str, filename: str) -> bool:
    return LibraryFunction("buffer_to_file")(buffer, filename)


@overload
def buy(coinmaster: Coinmaster, quantity: int, item: Item) -> bool: ...


@overload
def buy(quantity: int, item: Item, price: int) -> int: ...


@overload
def buy(quantity: int, item: Item) -> bool: ...


@overload
def buy(item: Item, quantity: int, price: int) -> int: ...


@overload
def buy(item: Item, quantity: int) -> bool: ...


@overload
def buy(item: Item) -> bool: ...


def buy(*args):
    return LibraryFunction("buy")(*args)


def buy_price(master: Coinmaster, item: Item) -> int:
    return LibraryFunction("buy_price")(master, item)


@overload
def buy_using_storage(quantity: int, item: Item, price: int) -> int: ...


@overload
def buy_using_storage(quantity: int, item: Item) -> bool: ...


@overload
def buy_using_storage(item: Item, quantity: int, price: int) -> int: ...


@overload
def buy_using_storage(item: Item, quantity: int) -> bool: ...


@overload
def buy_using_storage(item: Item) -> bool: ...


def buy_using_storage(*args):
    return LibraryFunction("buy_using_storage")(*args)


def buys_item(master: Coinmaster, item: Item) -> bool:
    return LibraryFunction("buys_item")(master, item)


def can_adventure(location: Location) -> bool:
    return LibraryFunction("can_adventure")(location)


def can_drink() -> bool:
    return LibraryFunction("can_drink")()


def can_eat() -> bool:
    return LibraryFunction("can_eat")()


@overload
def can_equip(familiar: Familiar, item: Item) -> bool: ...


@overload
def can_equip(familiar: Familiar) -> bool: ...


@overload
def can_equip(equipment: Item) -> bool: ...


def can_equip(*args):
    return LibraryFunction("can_equip")(*args)


@overload
def can_faxbot(monster: Monster, faxbot: str) -> bool: ...


@overload
def can_faxbot(monster: Monster) -> bool: ...


def can_faxbot(*args):
    return LibraryFunction("can_faxbot")(*args)


def can_interact() -> bool:
    return LibraryFunction("can_interact")()


def can_still_steal() -> bool:
    return LibraryFunction("can_still_steal")()


def canadia_available() -> bool:
    return LibraryFunction("canadia_available")()


@overload
def candy_for_tier(tier: int, flags: int) -> dict[int, Item]: ...


@overload
def candy_for_tier(tier: int) -> dict[int, Item]: ...


def candy_for_tier(*args):
    return LibraryFunction("candy_for_tier")(*args)


def ceil(val: float) -> int:
    return LibraryFunction("ceil")(val)


def change_mcd(level: int) -> bool:
    return LibraryFunction("change_mcd")(level)


def char_at(source: str, index: int) -> str:
    return LibraryFunction("char_at")(source, index)


@overload
def chat_clan(messageValue: str, recipientValue: str) -> None: ...


@overload
def chat_clan(messageValue: str) -> None: ...


def chat_clan(*args):
    return LibraryFunction("chat_clan")(*args)


def chat_macro(macroValue: str) -> None:
    return LibraryFunction("chat_macro")(macroValue)


def chat_notify(messageValue: str, colorValue: str) -> None:
    return LibraryFunction("chat_notify")(messageValue, colorValue)


def chat_private(recipientValue: str, messageValue: str) -> None:
    return LibraryFunction("chat_private")(recipientValue, messageValue)


@overload
def chew(count: int, item: Item) -> bool: ...


@overload
def chew(item: Item, count: int) -> bool: ...


@overload
def chew(item: Item) -> bool: ...


def chew(*args):
    return LibraryFunction("chew")(*args)


def choice_follows_fight() -> bool:
    return LibraryFunction("choice_follows_fight")()


@overload
def class_modifier(item: Item, modifier: Modifier) -> Class: ...


@overload
def class_modifier(item: Item, modifier: str) -> Class: ...


@overload
def class_modifier(type: str, modifier: Modifier) -> Class: ...


@overload
def class_modifier(type: str, modifier: str) -> Class: ...


def class_modifier(*args):
    return LibraryFunction("class_modifier")(*args)


def clear(agg: dict[Any, Any]) -> None:
    return LibraryFunction("clear")(agg)


def clear_booze_helper() -> None:
    return LibraryFunction("clear_booze_helper")()


def clear_food_helper() -> None:
    return LibraryFunction("clear_food_helper")()


def cli_execute(string: str) -> bool:
    return LibraryFunction("cli_execute")(string)


def cli_execute_output(string: str) -> str:
    return LibraryFunction("cli_execute_output")(string)


def closet_amount(item: Item) -> int:
    return LibraryFunction("closet_amount")(item)


def combat_mana_cost_modifier() -> int:
    return LibraryFunction("combat_mana_cost_modifier")()


def combat_rate_modifier() -> float:
    return LibraryFunction("combat_rate_modifier")()


def combat_skill_available(skill: Skill) -> bool:
    return LibraryFunction("combat_skill_available")(skill)


@overload
def concoction_price(value: Vykea) -> int: ...


@overload
def concoction_price(value: Item) -> int: ...


def concoction_price(*args):
    return LibraryFunction("concoction_price")(*args)


def contains_text(source: str, search: str) -> bool:
    return LibraryFunction("contains_text")(source, search)


def council() -> None:
    return LibraryFunction("council")()


def count(agg: dict[Any, Any]) -> int:
    return LibraryFunction("count")(agg)


def craft(modeValue: str, countValue: int, item1: Item, item2: Item) -> int:
    return LibraryFunction("craft")(modeValue, countValue, item1, item2)


def craft_type(item: Item) -> str:
    return LibraryFunction("craft_type")(item)


def creatable_amount(item: Item) -> int:
    return LibraryFunction("creatable_amount")(item)


@overload
def creatable_turns(itemId: Item, count: int, freeCrafting: bool) -> int: ...


@overload
def creatable_turns(itemId: Item, count: int) -> int: ...


@overload
def creatable_turns(itemId: Item) -> int: ...


def creatable_turns(*args):
    return LibraryFunction("creatable_turns")(*args)


@overload
def create(count: int, item: Item) -> bool: ...


@overload
def create(item: Item, count: int) -> bool: ...


@overload
def create(item: Item) -> bool: ...


def create(*args):
    return LibraryFunction("create")(*args)


def create_matcher(patternValue: str, stringValue: str) -> Matcher:
    return LibraryFunction("create_matcher")(patternValue, stringValue)


def current_hit_stat() -> Stat:
    return LibraryFunction("current_hit_stat")()


def current_mcd() -> int:
    return LibraryFunction("current_mcd")()


def current_pvp_stances() -> dict[str, int]:
    return LibraryFunction("current_pvp_stances")()


def current_rad_sickness() -> int:
    return LibraryFunction("current_rad_sickness")()


def current_round() -> int:
    return LibraryFunction("current_round")()


@overload
def curse(quantity: int, itemId: Item, target: str, message: str) -> bool: ...


@overload
def curse(itemId: Item, target: str, message: str) -> bool: ...


@overload
def curse(itemId: Item, target: str) -> bool: ...


def curse(*args):
    return LibraryFunction("curse")(*args)


def dad_sea_monkee_weakness(round: int) -> Element:
    return LibraryFunction("dad_sea_monkee_weakness")(round)


def daily_special() -> Item:
    return LibraryFunction("daily_special")()


def damage_absorption_percent() -> float:
    return LibraryFunction("damage_absorption_percent")()


def damage_reduction() -> int:
    return LibraryFunction("damage_reduction")()


def dart_parts_to_skills() -> dict[str, Skill]:
    return LibraryFunction("dart_parts_to_skills")()


def dart_skills_to_parts() -> dict[Skill, str]:
    return LibraryFunction("dart_skills_to_parts")()


def date_to_timestamp(inFormat: str, dateTimeString: str) -> int:
    return LibraryFunction("date_to_timestamp")(inFormat, dateTimeString)


def daycount() -> int:
    return LibraryFunction("daycount")()


def debugprint(string: str) -> None:
    return LibraryFunction("debugprint")(string)


def delete(buffer: str, start: int, finish: int) -> str:
    return LibraryFunction("delete")(buffer, start, finish)


def desc_to_effect(value: str) -> Effect:
    return LibraryFunction("desc_to_effect")(value)


def desc_to_item(value: str) -> Item:
    return LibraryFunction("desc_to_item")(value)


def disable(name: str) -> None:
    return LibraryFunction("disable")(name)


def dispensary_available() -> bool:
    return LibraryFunction("dispensary_available")()


def display_amount(item: Item) -> int:
    return LibraryFunction("display_amount")(item)


@overload
def drink(count: int, item: Item) -> bool: ...


@overload
def drink(item: Item, count: int) -> bool: ...


@overload
def drink(item: Item) -> bool: ...


def drink(*args):
    return LibraryFunction("drink")(*args)


@overload
def drinksilent(count: int, item: Item) -> bool: ...


@overload
def drinksilent(item: Item, count: int) -> bool: ...


@overload
def drinksilent(item: Item) -> bool: ...


def drinksilent(*args):
    return LibraryFunction("drinksilent")(*args)


@overload
def dump(arg: Any, color: str) -> None: ...


@overload
def dump(arg: Any) -> None: ...


def dump(*args):
    return LibraryFunction("dump")(*args)


@overload
def eat(count: int, item: Item) -> bool: ...


@overload
def eat(item: Item, count: int) -> bool: ...


@overload
def eat(item: Item) -> bool: ...


def eat(*args):
    return LibraryFunction("eat")(*args)


@overload
def eatsilent(count: int, item: Item) -> bool: ...


@overload
def eatsilent(item: Item, count: int) -> bool: ...


@overload
def eatsilent(item: Item) -> bool: ...


def eatsilent(*args):
    return LibraryFunction("eatsilent")(*args)


@overload
def effect_fact(monster: Monster) -> Effect: ...


@overload
def effect_fact(cls: Class, path: Path, monster: Monster) -> Effect: ...


def effect_fact(*args):
    return LibraryFunction("effect_fact")(*args)


@overload
def effect_modifier(item: Item, modifier: Modifier) -> Effect: ...


@overload
def effect_modifier(item: Item, modifier: str) -> Effect: ...


@overload
def effect_modifier(type: str, modifier: Modifier) -> Effect: ...


@overload
def effect_modifier(type: str, modifier: str) -> Effect: ...


def effect_modifier(*args):
    return LibraryFunction("effect_modifier")(*args)


def effect_pockets() -> dict[int, bool]:
    return LibraryFunction("effect_pockets")()


@overload
def eight_bit_points(
    locationValue: Location, colorValue: str, modValue: float
) -> int: ...


@overload
def eight_bit_points(locationValue: Location) -> int: ...


def eight_bit_points(*args):
    return LibraryFunction("eight_bit_points")(*args)


@overload
def elemental_resistance(monster: Monster) -> float: ...


@overload
def elemental_resistance() -> float: ...


@overload
def elemental_resistance(element: Element) -> float: ...


def elemental_resistance(*args):
    return LibraryFunction("elemental_resistance")(*args)


def empty_closet() -> bool:
    return LibraryFunction("empty_closet")()


def enable(name: str) -> None:
    return LibraryFunction("enable")(name)


@overload
def end(matcher: Matcher, group: int) -> int: ...


@overload
def end(matcher: Matcher) -> int: ...


def end(*args):
    return LibraryFunction("end")(*args)


def ends_with(source: str, suffix: str) -> bool:
    return LibraryFunction("ends_with")(source, suffix)


def enthrone_familiar(familiar: Familiar) -> bool:
    return LibraryFunction("enthrone_familiar")(familiar)


def entity_decode(string: str) -> str:
    return LibraryFunction("entity_decode")(string)


def entity_encode(string: str) -> str:
    return LibraryFunction("entity_encode")(string)


@overload
def equip(familiar: Familiar, item: Item) -> bool: ...


@overload
def equip(item: Item, familiar: Familiar) -> bool: ...


@overload
def equip(slot: Slot, item: Item) -> bool: ...


@overload
def equip(item: Item, slot: Slot) -> bool: ...


@overload
def equip(item: Item) -> bool: ...


def equip(*args):
    return LibraryFunction("equip")(*args)


def equip_all_familiars() -> bool:
    return LibraryFunction("equip_all_familiars")()


@overload
def equipped_amount(item: Item, includeAllFamiliars: bool) -> int: ...


@overload
def equipped_amount(item: Item) -> int: ...


def equipped_amount(*args):
    return LibraryFunction("equipped_amount")(*args)


def equipped_item(slot: Slot) -> Item:
    return LibraryFunction("equipped_item")(slot)


@overload
def eudora(newEudora: str) -> bool: ...


@overload
def eudora() -> str: ...


def eudora(*args):
    return LibraryFunction("eudora")(*args)


def eudora_item() -> Item:
    return LibraryFunction("eudora_item")()


def every_card_name(name: str) -> str:
    return LibraryFunction("every_card_name")(name)


def expected_cold_medicine_cabinet() -> dict[str, Item]:
    return LibraryFunction("expected_cold_medicine_cabinet")()


@overload
def expected_damage(monster: Monster) -> int: ...


@overload
def expected_damage() -> int: ...


def expected_damage(*args):
    return LibraryFunction("expected_damage")(*args)


def experience_bonus() -> float:
    return LibraryFunction("experience_bonus")()


def expression_eval(expr: str) -> float:
    return LibraryFunction("expression_eval")(expr)


def extract_items(string: str) -> dict[Item, int]:
    return LibraryFunction("extract_items")(string)


def extract_meat(string: str) -> int:
    return LibraryFunction("extract_meat")(string)


@overload
def fact_type(monster: Monster) -> str: ...


@overload
def fact_type(cls: Class, path: Path, monster: Monster) -> str: ...


def fact_type(*args):
    return LibraryFunction("fact_type")(*args)


def familiar_equipment(familiar: Familiar) -> Item:
    return LibraryFunction("familiar_equipment")(familiar)


def familiar_equipped_equipment(familiar: Familiar) -> Item:
    return LibraryFunction("familiar_equipped_equipment")(familiar)


def familiar_weight(familiar: Familiar) -> int:
    return LibraryFunction("familiar_weight")(familiar)


def favorite_familiars() -> dict[Familiar, bool]:
    return LibraryFunction("favorite_familiars")()


@overload
def faxbot(monsterName: Monster, botName: str) -> bool: ...


@overload
def faxbot(monsterName: Monster) -> bool: ...


def faxbot(*args):
    return LibraryFunction("faxbot")(*args)


def fight_follows_choice() -> bool:
    return LibraryFunction("fight_follows_choice")()


def file_to_array(filename: str) -> dict[int, str]:
    return LibraryFunction("file_to_array")(filename)


def file_to_buffer(filename: str) -> str:
    return LibraryFunction("file_to_buffer")(filename)


@overload
def file_to_map(filename: str, result: dict[Any, Any], compact: bool) -> bool: ...


@overload
def file_to_map(filename: str, result: dict[Any, Any]) -> bool: ...


def file_to_map(*args):
    return LibraryFunction("file_to_map")(*args)


def find(matcher: Matcher) -> bool:
    return LibraryFunction("find")(matcher)


def floor(val: float) -> int:
    return LibraryFunction("floor")(val)


def florist_available() -> bool:
    return LibraryFunction("florist_available")()


def flush_monster_manuel_cache() -> bool:
    return LibraryFunction("flush_monster_manuel_cache")()


def form_field(key: str) -> str:
    return LibraryFunction("form_field")(key)


def form_fields() -> dict[str, str]:
    return LibraryFunction("form_fields")()


def format_date_time(inFormat: str, dateTimeString: str, outFormat: str) -> str:
    return LibraryFunction("format_date_time")(inFormat, dateTimeString, outFormat)


def friars_available() -> bool:
    return LibraryFunction("friars_available")()


def fuel_cost(skill: Skill) -> int:
    return LibraryFunction("fuel_cost")(skill)


def fullness_limit() -> int:
    return LibraryFunction("fullness_limit")()


def gameday_to_int() -> int:
    return LibraryFunction("gameday_to_int")()


def gameday_to_string() -> str:
    return LibraryFunction("gameday_to_string")()


def gametime_to_int() -> int:
    return LibraryFunction("gametime_to_int")()


def get_all_properties(filterValue: str, globalValue: bool) -> dict[str, bool]:
    return LibraryFunction("get_all_properties")(filterValue, globalValue)


def get_auto_attack() -> int:
    return LibraryFunction("get_auto_attack")()


def get_autumnaton_locations() -> dict[int, Location]:
    return LibraryFunction("get_autumnaton_locations")()


def get_campground() -> dict[Item, int]:
    return LibraryFunction("get_campground")()


def get_ccs_action(index: int) -> str:
    return LibraryFunction("get_ccs_action")(index)


def get_chateau() -> dict[Item, int]:
    return LibraryFunction("get_chateau")()


def get_clan_id() -> int:
    return LibraryFunction("get_clan_id")()


def get_clan_lounge() -> dict[Item, int]:
    return LibraryFunction("get_clan_lounge")()


def get_clan_name() -> str:
    return LibraryFunction("get_clan_name")()


def get_clan_rumpus() -> dict[str, int]:
    return LibraryFunction("get_clan_rumpus")()


def get_closet() -> dict[Item, int]:
    return LibraryFunction("get_closet")()


def get_counter(label: str) -> int:
    return LibraryFunction("get_counter")(label)


def get_counters(label: str, min: int, max: int) -> str:
    return LibraryFunction("get_counters")(label, min, max)


def get_custom_outfits() -> dict[int, str]:
    return LibraryFunction("get_custom_outfits")()


def get_display() -> dict[Item, int]:
    return LibraryFunction("get_display")()


def get_dwelling() -> Item:
    return LibraryFunction("get_dwelling")()


def get_fishing_locations() -> dict[str, Location]:
    return LibraryFunction("get_fishing_locations")()


def get_florist_plants() -> dict[Location, dict[int, str]]:
    return LibraryFunction("get_florist_plants")()


def get_free_pulls() -> dict[Item, int]:
    return LibraryFunction("get_free_pulls")()


def get_fuel() -> int:
    return LibraryFunction("get_fuel")()


def get_goals() -> dict[int, str]:
    return LibraryFunction("get_goals")()


def get_ignore_zone_warnings() -> bool:
    return LibraryFunction("get_ignore_zone_warnings")()


def get_ingredients(item: Item) -> dict[Item, int]:
    return LibraryFunction("get_ingredients")(item)


def get_inventory() -> dict[Item, int]:
    return LibraryFunction("get_inventory")()


def get_location_monsters(location: Location) -> dict[Monster, bool]:
    return LibraryFunction("get_location_monsters")(location)


def get_locket_monsters() -> dict[Monster, bool]:
    return LibraryFunction("get_locket_monsters")()


@overload
def get_monster_mapping(path: str) -> dict[Monster, Monster]: ...


@overload
def get_monster_mapping() -> dict[Monster, Monster]: ...


def get_monster_mapping(*args):
    return LibraryFunction("get_monster_mapping")(*args)


def get_monsters(location: Location) -> dict[int, Monster]:
    return LibraryFunction("get_monsters")(location)


def get_moods() -> dict[int, str]:
    return LibraryFunction("get_moods")()


def get_outfits() -> dict[int, str]:
    return LibraryFunction("get_outfits")()


def get_path() -> str:
    return LibraryFunction("get_path")()


def get_path_full() -> str:
    return LibraryFunction("get_path_full")()


def get_path_variables() -> str:
    return LibraryFunction("get_path_variables")()


def get_permed_skills() -> dict[Skill, bool]:
    return LibraryFunction("get_permed_skills")()


def get_player_id(playerNameValue: str) -> str:
    return LibraryFunction("get_player_id")(playerNameValue)


def get_player_name(playerIdValue: int) -> str:
    return LibraryFunction("get_player_name")(playerIdValue)


def get_power(item: Item) -> int:
    return LibraryFunction("get_power")(item)


@overload
def get_property(name: str, globalValue: bool) -> str: ...


@overload
def get_property(name: str) -> str: ...


def get_property(*args):
    return LibraryFunction("get_property")(*args)


def get_related(item: Item, type: str) -> dict[Item, int]:
    return LibraryFunction("get_related")(item, type)


def get_revision() -> int:
    return LibraryFunction("get_revision")()


def get_shop() -> dict[Item, int]:
    return LibraryFunction("get_shop")()


def get_shop_log() -> dict[int, str]:
    return LibraryFunction("get_shop_log")()


def get_stack_trace() -> dict[int, dict[str, Any]]:
    return LibraryFunction("get_stack_trace")()


def get_stash() -> dict[Item, int]:
    return LibraryFunction("get_stash")()


def get_storage() -> dict[Item, int]:
    return LibraryFunction("get_storage")()


def get_version() -> str:
    return LibraryFunction("get_version")()


def get_workshed() -> Item:
    return LibraryFunction("get_workshed")()


def get_zap_wand() -> Item:
    return LibraryFunction("get_zap_wand")()


def git_at_head(project: str) -> bool:
    return LibraryFunction("git_at_head")(project)


def git_exists(project: str) -> bool:
    return LibraryFunction("git_exists")(project)


def git_info(script: str) -> dict[str, Any]:
    return LibraryFunction("git_info")(script)


def git_list() -> dict[int, str]:
    return LibraryFunction("git_list")()


def gnomads_available() -> bool:
    return LibraryFunction("gnomads_available")()


def goal_exists(check: str) -> bool:
    return LibraryFunction("goal_exists")(check)


@overload
def group(matcher: Matcher, group: str) -> str: ...


@overload
def group(matcher: Matcher, group: int) -> str: ...


@overload
def group(matcher: Matcher) -> str: ...


def group(*args):
    return LibraryFunction("group")(*args)


def group_count(matcher: Matcher) -> int:
    return LibraryFunction("group_count")(matcher)


def group_names(matcher: Matcher) -> dict[str, bool]:
    return LibraryFunction("group_names")(matcher)


def group_string(string: str, regex: str) -> dict[int, dict[int, str]]:
    return LibraryFunction("group_string")(string, regex)


def guild_available() -> bool:
    return LibraryFunction("guild_available")()


def guild_store_available() -> bool:
    return LibraryFunction("guild_store_available")()


def handling_choice() -> bool:
    return LibraryFunction("handling_choice")()


def has_queued_commands() -> bool:
    return LibraryFunction("has_queued_commands")()


def have_bartender() -> bool:
    return LibraryFunction("have_bartender")()


def have_chef() -> bool:
    return LibraryFunction("have_chef")()


def have_display() -> bool:
    return LibraryFunction("have_display")()


def have_effect(effect: Effect) -> int:
    return LibraryFunction("have_effect")(effect)


def have_equipped(item: Item) -> bool:
    return LibraryFunction("have_equipped")(item)


def have_familiar(familiar: Familiar) -> bool:
    return LibraryFunction("have_familiar")(familiar)


def have_mushroom_plot() -> bool:
    return LibraryFunction("have_mushroom_plot")()


def have_outfit(outfit: str) -> bool:
    return LibraryFunction("have_outfit")(outfit)


def have_servant(servant: Servant) -> bool:
    return LibraryFunction("have_servant")(servant)


def have_shop() -> bool:
    return LibraryFunction("have_shop")()


def have_skill(skill: Skill) -> bool:
    return LibraryFunction("have_skill")(skill)


def hedge_maze(goal: str) -> bool:
    return LibraryFunction("hedge_maze")(goal)


@overload
def heist(num: int, item: Item) -> bool: ...


@overload
def heist(item: Item) -> bool: ...


def heist(*args):
    return LibraryFunction("heist")(*args)


def heist_targets() -> dict[Monster, dict[int, Item]]:
    return LibraryFunction("heist_targets")()


@overload
def hermit(count: int, item: Item) -> bool: ...


@overload
def hermit(item: Item, count: int) -> bool: ...


def hermit(*args):
    return LibraryFunction("hermit")(*args)


def hidden_temple_unlocked() -> bool:
    return LibraryFunction("hidden_temple_unlocked")()


def hippy_stone_broken() -> bool:
    return LibraryFunction("hippy_stone_broken")()


def hippy_store_available() -> bool:
    return LibraryFunction("hippy_store_available")()


def historical_age(item: Item) -> float:
    return LibraryFunction("historical_age")(item)


def historical_price(item: Item) -> int:
    return LibraryFunction("historical_price")(item)


def holiday() -> str:
    return LibraryFunction("holiday")()


def hp_cost(skill: Skill) -> int:
    return LibraryFunction("hp_cost")(skill)


def image_to_monster(value: str) -> Monster:
    return LibraryFunction("image_to_monster")(value)


def in_bad_moon() -> bool:
    return LibraryFunction("in_bad_moon")()


def in_casual() -> bool:
    return LibraryFunction("in_casual")()


def in_hardcore() -> bool:
    return LibraryFunction("in_hardcore")()


def in_moxie_sign() -> bool:
    return LibraryFunction("in_moxie_sign")()


def in_multi_fight() -> bool:
    return LibraryFunction("in_multi_fight")()


def in_muscle_sign() -> bool:
    return LibraryFunction("in_muscle_sign")()


def in_mysticality_sign() -> bool:
    return LibraryFunction("in_mysticality_sign")()


def in_terrarium(familiar: Familiar) -> bool:
    return LibraryFunction("in_terrarium")(familiar)


def inaccessible_reason(master: Coinmaster) -> str:
    return LibraryFunction("inaccessible_reason")(master)


@overload
def index_of(source: str, search: str, start: int) -> int: ...


@overload
def index_of(source: str, search: str) -> int: ...


def index_of(*args):
    return LibraryFunction("index_of")(*args)


def inebriety_limit() -> int:
    return LibraryFunction("inebriety_limit")()


def initiative_modifier() -> float:
    return LibraryFunction("initiative_modifier")()


def insert(buffer: str, index: int, s: str) -> str:
    return LibraryFunction("insert")(buffer, index, s)


def is_accessible(master: Coinmaster) -> bool:
    return LibraryFunction("is_accessible")(master)


def is_adventuring() -> bool:
    return LibraryFunction("is_adventuring")()


def is_banished(monster: Monster) -> bool:
    return LibraryFunction("is_banished")(monster)


def is_coinmaster_item(item: Item) -> bool:
    return LibraryFunction("is_coinmaster_item")(item)


def is_dark_mode() -> bool:
    return LibraryFunction("is_dark_mode")()


def is_discardable(item: Item) -> bool:
    return LibraryFunction("is_discardable")(item)


def is_displayable(item: Item) -> bool:
    return LibraryFunction("is_displayable")(item)


def is_familiar_equipment_locked() -> bool:
    return LibraryFunction("is_familiar_equipment_locked")()


def is_giftable(item: Item) -> bool:
    return LibraryFunction("is_giftable")(item)


def is_goal(item: Item) -> bool:
    return LibraryFunction("is_goal")(item)


def is_headless() -> bool:
    return LibraryFunction("is_headless")()


def is_integer(string: str) -> bool:
    return LibraryFunction("is_integer")(string)


def is_npc_item(item: Item) -> bool:
    return LibraryFunction("is_npc_item")(item)


def is_online(name: str) -> bool:
    return LibraryFunction("is_online")(name)


def is_removable(effect: Effect) -> bool:
    return LibraryFunction("is_removable")(effect)


def is_shruggable(effect: Effect) -> bool:
    return LibraryFunction("is_shruggable")(effect)


def is_tradeable(item: Item) -> bool:
    return LibraryFunction("is_tradeable")(item)


@overload
def is_trendy(thing: str) -> bool: ...


@overload
def is_trendy(thing: Familiar) -> bool: ...


@overload
def is_trendy(thing: Skill) -> bool: ...


@overload
def is_trendy(thing: Item) -> bool: ...


def is_trendy(*args):
    return LibraryFunction("is_trendy")(*args)


@overload
def is_unrestricted(thing: str) -> bool: ...


@overload
def is_unrestricted(thing: Familiar) -> bool: ...


@overload
def is_unrestricted(thing: Skill) -> bool: ...


@overload
def is_unrestricted(thing: Item) -> bool: ...


def is_unrestricted(*args):
    return LibraryFunction("is_unrestricted")(*args)


def is_wearing_outfit(outfit: str) -> bool:
    return LibraryFunction("is_wearing_outfit")(outfit)


def item_amount(item: Item) -> int:
    return LibraryFunction("item_amount")(item)


def item_drop_modifier() -> float:
    return LibraryFunction("item_drop_modifier")()


@overload
def item_drops(monster: Monster) -> dict[Item, float]: ...


@overload
def item_drops() -> dict[Item, float]: ...


def item_drops(*args):
    return LibraryFunction("item_drops")(*args)


@overload
def item_drops_array(monster: Monster) -> dict[int, dict[str, Any]]: ...


@overload
def item_drops_array() -> dict[int, dict[str, Any]]: ...


def item_drops_array(*args):
    return LibraryFunction("item_drops_array")(*args)


@overload
def item_fact(monster: Monster) -> Item: ...


@overload
def item_fact(cls: Class, path: Path, monster: Monster) -> Item: ...


def item_fact(*args):
    return LibraryFunction("item_fact")(*args)


def item_pockets() -> dict[int, bool]:
    return LibraryFunction("item_pockets")()


def item_type(item: Item) -> str:
    return LibraryFunction("item_type")(item)


@overload
def join_strings(strings: dict[int, str], joiner: str) -> str: ...


@overload
def join_strings(strings: dict[int, str]) -> str: ...


def join_strings(*args):
    return LibraryFunction("join_strings")(*args)


def joke_pockets() -> dict[int, bool]:
    return LibraryFunction("joke_pockets")()


@overload
def jump_chance(location: Location, init: int, ml: int) -> int: ...


@overload
def jump_chance(location: Location, init: int) -> int: ...


@overload
def jump_chance(location: Location) -> int: ...


@overload
def jump_chance(monster: Monster, init: int, ml: int) -> int: ...


@overload
def jump_chance(monster: Monster, init: int) -> int: ...


@overload
def jump_chance(monster: Monster) -> int: ...


@overload
def jump_chance() -> int: ...


def jump_chance(*args):
    return LibraryFunction("jump_chance")(*args)


def knoll_available() -> bool:
    return LibraryFunction("knoll_available")()


def last_choice() -> int:
    return LibraryFunction("last_choice")()


def last_decision() -> int:
    return LibraryFunction("last_decision")()


@overload
def last_index_of(source: str, search: str, start: int) -> int: ...


@overload
def last_index_of(source: str, search: str) -> int: ...


def last_index_of(*args):
    return LibraryFunction("last_index_of")(*args)


def last_item_message() -> str:
    return LibraryFunction("last_item_message")()


def last_monster() -> Monster:
    return LibraryFunction("last_monster")()


def last_skill_message() -> str:
    return LibraryFunction("last_skill_message")()


def leetify(string: str) -> str:
    return LibraryFunction("leetify")(string)


def length(string: str) -> int:
    return LibraryFunction("length")(string)


def lightning_cost(skill: Skill) -> int:
    return LibraryFunction("lightning_cost")(skill)


def limit_mode() -> str:
    return LibraryFunction("limit_mode")()


def load_html(string: str) -> str:
    return LibraryFunction("load_html")(string)


def lock_familiar_equipment(lock: bool) -> None:
    return LibraryFunction("lock_familiar_equipment")(lock)


@overload
def log_n(val: float, base: float) -> float: ...


@overload
def log_n(val: float) -> float: ...


def log_n(*args):
    return LibraryFunction("log_n")(*args)


def logprint(string: str) -> None:
    return LibraryFunction("logprint")(string)


def make_url(string: str, usePostMethod: bool, encoded: bool) -> str:
    return LibraryFunction("make_url")(string, usePostMethod, encoded)


@overload
def mall_price(item: Item, maxAge: float) -> int: ...


@overload
def mall_price(item: Item) -> int: ...


def mall_price(*args):
    return LibraryFunction("mall_price")(*args)


@overload
def mall_prices(category: str, tiers: str) -> int: ...


@overload
def mall_prices(category: str) -> int: ...


@overload
def mall_prices(items: dict[int, bool]) -> int: ...


def mall_prices(*args):
    return LibraryFunction("mall_prices")(*args)


def mana_cost_modifier() -> int:
    return LibraryFunction("mana_cost_modifier")()


@overload
def map_to_file(map: dict[Any, Any], filename: str, compact: bool) -> bool: ...


@overload
def map_to_file(map: dict[Any, Any], filename: str) -> bool: ...


def map_to_file(*args):
    return LibraryFunction("map_to_file")(*args)


@overload
def max(val: int, otherVal: dict[int, int]) -> int: ...


@overload
def max(val: float, otherVal: dict[int, float]) -> float: ...


def max(*args):
    return LibraryFunction("max")(*args)


@overload
def maximize(
    maximizerStringValue: str,
    maxPriceValue: int,
    priceLevelValue: int,
    isSpeculateOnlyValue: bool,
    showEquipment: bool,
) -> dict[int, dict[str, Any]]: ...


@overload
def maximize(
    maximizerStringValue: str,
    maxPriceValue: int,
    priceLevelValue: int,
    isSpeculateOnlyValue: bool,
) -> bool: ...


@overload
def maximize(maximizerStringValue: str, isSpeculateOnlyValue: bool) -> bool: ...


def maximize(*args):
    return LibraryFunction("maximize")(*args)


@overload
def meat_drop(monster: Monster) -> int: ...


@overload
def meat_drop() -> int: ...


def meat_drop(*args):
    return LibraryFunction("meat_drop")(*args)


def meat_drop_modifier() -> float:
    return LibraryFunction("meat_drop_modifier")()


def meat_pockets() -> dict[int, int]:
    return LibraryFunction("meat_pockets")()


@overload
def min(val: int, otherVal: dict[int, int]) -> int: ...


@overload
def min(val: float, otherVal: dict[int, float]) -> float: ...


def min(*args):
    return LibraryFunction("min")(*args)


def minstrel_instrument() -> Item:
    return LibraryFunction("minstrel_instrument")()


def minstrel_level() -> int:
    return LibraryFunction("minstrel_level")()


def minstrel_quest() -> bool:
    return LibraryFunction("minstrel_quest")()


def modifier_eval(expr: str) -> float:
    return LibraryFunction("modifier_eval")(expr)


@overload
def monkey_paw(wish: str) -> bool: ...


@overload
def monkey_paw(effect: Effect) -> bool: ...


@overload
def monkey_paw(item: Item) -> bool: ...


def monkey_paw(*args):
    return LibraryFunction("monkey_paw")(*args)


@overload
def monster_attack(monster: Monster) -> int: ...


@overload
def monster_attack() -> int: ...


def monster_attack(*args):
    return LibraryFunction("monster_attack")(*args)


@overload
def monster_defense(monster: Monster) -> int: ...


@overload
def monster_defense() -> int: ...


def monster_defense(*args):
    return LibraryFunction("monster_defense")(*args)


@overload
def monster_element(monster: Monster) -> Element: ...


@overload
def monster_element() -> Element: ...


def monster_element(*args):
    return LibraryFunction("monster_element")(*args)


def monster_eval(expr: str) -> float:
    return LibraryFunction("monster_eval")(expr)


def monster_factoids_available(monster: Monster, cachedOnly: bool) -> int:
    return LibraryFunction("monster_factoids_available")(monster, cachedOnly)


@overload
def monster_hp(monster: Monster) -> int: ...


@overload
def monster_hp() -> int: ...


def monster_hp(*args):
    return LibraryFunction("monster_hp")(*args)


@overload
def monster_initiative(monster: Monster) -> int: ...


@overload
def monster_initiative() -> int: ...


def monster_initiative(*args):
    return LibraryFunction("monster_initiative")(*args)


def monster_level_adjustment() -> int:
    return LibraryFunction("monster_level_adjustment")()


def monster_manuel_text(monster: Monster) -> str:
    return LibraryFunction("monster_manuel_text")(monster)


@overload
def monster_modifier(effect: Effect, modifier: Modifier) -> Monster: ...


@overload
def monster_modifier(effect: Effect, modifier: str) -> Monster: ...


def monster_modifier(*args):
    return LibraryFunction("monster_modifier")(*args)


@overload
def monster_phylum(monster: Monster) -> Phylum: ...


@overload
def monster_phylum() -> Phylum: ...


def monster_phylum(*args):
    return LibraryFunction("monster_phylum")(*args)


def monster_pockets() -> dict[int, bool]:
    return LibraryFunction("monster_pockets")()


def mood_execute(multiplicity: int) -> None:
    return LibraryFunction("mood_execute")(multiplicity)


def mood_list() -> dict[int, str]:
    return LibraryFunction("mood_list")()


def moon_light() -> int:
    return LibraryFunction("moon_light")()


def moon_phase() -> int:
    return LibraryFunction("moon_phase")()


def mp_cost(skill: Skill) -> int:
    return LibraryFunction("mp_cost")(skill)


def my_absorbs() -> int:
    return LibraryFunction("my_absorbs")()


def my_adventures() -> int:
    return LibraryFunction("my_adventures")()


def my_ascensions() -> int:
    return LibraryFunction("my_ascensions")()


def my_audience() -> int:
    return LibraryFunction("my_audience")()


def my_basestat(stat: Stat) -> int:
    return LibraryFunction("my_basestat")(stat)


def my_bjorned_familiar() -> Familiar:
    return LibraryFunction("my_bjorned_familiar")()


def my_buffedstat(stat: Stat) -> int:
    return LibraryFunction("my_buffedstat")(stat)


def my_class() -> Class:
    return LibraryFunction("my_class")()


def my_closet_meat() -> int:
    return LibraryFunction("my_closet_meat")()


def my_companion() -> str:
    return LibraryFunction("my_companion")()


def my_daycount() -> int:
    return LibraryFunction("my_daycount")()


def my_discomomentum() -> int:
    return LibraryFunction("my_discomomentum")()


def my_effective_familiar() -> Familiar:
    return LibraryFunction("my_effective_familiar")()


def my_effects() -> dict[Effect, int]:
    return LibraryFunction("my_effects")()


def my_enthroned_familiar() -> Familiar:
    return LibraryFunction("my_enthroned_familiar")()


def my_familiar() -> Familiar:
    return LibraryFunction("my_familiar")()


def my_fullness() -> int:
    return LibraryFunction("my_fullness")()


def my_fury() -> int:
    return LibraryFunction("my_fury")()


def my_garden_type() -> str:
    return LibraryFunction("my_garden_type")()


def my_hash() -> str:
    return LibraryFunction("my_hash")()


def my_hp() -> int:
    return LibraryFunction("my_hp")()


def my_id() -> str:
    return LibraryFunction("my_id")()


def my_inebriety() -> int:
    return LibraryFunction("my_inebriety")()


def my_level() -> int:
    return LibraryFunction("my_level")()


def my_lightning() -> int:
    return LibraryFunction("my_lightning")()


def my_location() -> Location:
    return LibraryFunction("my_location")()


def my_mask() -> str:
    return LibraryFunction("my_mask")()


def my_maxfury() -> int:
    return LibraryFunction("my_maxfury")()


def my_maxhp() -> int:
    return LibraryFunction("my_maxhp")()


def my_maxmp() -> int:
    return LibraryFunction("my_maxmp")()


def my_maxpp() -> int:
    return LibraryFunction("my_maxpp")()


def my_meat() -> int:
    return LibraryFunction("my_meat")()


def my_mp() -> int:
    return LibraryFunction("my_mp")()


def my_name() -> str:
    return LibraryFunction("my_name")()


def my_path() -> Path:
    return LibraryFunction("my_path")()


def my_path_id() -> int:
    return LibraryFunction("my_path_id")()


def my_poke_fam(slot: int) -> Familiar:
    return LibraryFunction("my_poke_fam")(slot)


def my_pp() -> int:
    return LibraryFunction("my_pp")()


def my_primestat() -> Stat:
    return LibraryFunction("my_primestat")()


def my_rain() -> int:
    return LibraryFunction("my_rain")()


def my_robot_energy() -> int:
    return LibraryFunction("my_robot_energy")()


def my_robot_scraps() -> int:
    return LibraryFunction("my_robot_scraps")()


def my_servant() -> Servant:
    return LibraryFunction("my_servant")()


def my_session_adv() -> int:
    return LibraryFunction("my_session_adv")()


@overload
def my_session_items(item: Item) -> int: ...


@overload
def my_session_items() -> dict[Item, int]: ...


def my_session_items(*args):
    return LibraryFunction("my_session_items")(*args)


def my_session_meat() -> int:
    return LibraryFunction("my_session_meat")()


def my_session_results() -> dict[str, int]:
    return LibraryFunction("my_session_results")()


def my_sign() -> str:
    return LibraryFunction("my_sign")()


def my_soulsauce() -> int:
    return LibraryFunction("my_soulsauce")()


def my_spleen_use() -> int:
    return LibraryFunction("my_spleen_use")()


def my_storage_meat() -> int:
    return LibraryFunction("my_storage_meat")()


def my_thrall() -> Thrall:
    return LibraryFunction("my_thrall")()


def my_thunder() -> int:
    return LibraryFunction("my_thunder")()


def my_total_turns_spent() -> int:
    return LibraryFunction("my_total_turns_spent")()


def my_turncount() -> int:
    return LibraryFunction("my_turncount")()


def my_vykea_companion() -> Vykea:
    return LibraryFunction("my_vykea_companion")()


def my_wildfire_water() -> int:
    return LibraryFunction("my_wildfire_water")()


def now_to_int() -> int:
    return LibraryFunction("now_to_int")()


def now_to_string(dateFormatValue: str) -> str:
    return LibraryFunction("now_to_string")(dateFormatValue)


def npc_price(item: Item) -> int:
    return LibraryFunction("npc_price")(item)


def numberology_prize(num: int) -> str:
    return LibraryFunction("numberology_prize")(num)


@overload
def numeric_fact(monster: Monster) -> int: ...


@overload
def numeric_fact(cls: Class, path: Path, monster: Monster) -> int: ...


def numeric_fact(*args):
    return LibraryFunction("numeric_fact")(*args)


@overload
def numeric_modifier(thrall: Thrall, modifier: Modifier) -> float: ...


@overload
def numeric_modifier(thrall: Thrall, modifier: str) -> float: ...


@overload
def numeric_modifier(
    familiar: Familiar, modifier: str, weight: int, item: Item
) -> float: ...


@overload
def numeric_modifier(skill: Skill, modifier: Modifier) -> float: ...


@overload
def numeric_modifier(skill: Skill, modifier: str) -> float: ...


@overload
def numeric_modifier(effect: Effect, modifier: Modifier) -> float: ...


@overload
def numeric_modifier(effect: Effect, modifier: str) -> float: ...


@overload
def numeric_modifier(item: Item, modifier: Modifier) -> float: ...


@overload
def numeric_modifier(item: Item, modifier: str) -> float: ...


@overload
def numeric_modifier(type: str, modifier: Modifier) -> float: ...


@overload
def numeric_modifier(type: str, modifier: str) -> float: ...


@overload
def numeric_modifier(modifier: Modifier) -> float: ...


@overload
def numeric_modifier(modifier: str) -> float: ...


def numeric_modifier(*args):
    return LibraryFunction("numeric_modifier")(*args)


def outfit(outfit: str) -> bool:
    return LibraryFunction("outfit")(outfit)


def outfit_pieces(outfit: str) -> dict[int, Item]:
    return LibraryFunction("outfit_pieces")(outfit)


def outfit_tattoo(outfit: str) -> str:
    return LibraryFunction("outfit_tattoo")(outfit)


def outfit_treats(outfit: str) -> dict[Item, float]:
    return LibraryFunction("outfit_treats")(outfit)


@overload
def overdrink(count: int, item: Item) -> bool: ...


@overload
def overdrink(item: Item, count: int) -> bool: ...


@overload
def overdrink(item: Item) -> bool: ...


def overdrink(*args):
    return LibraryFunction("overdrink")(*args)


def path_id_to_name(value: int) -> str:
    return LibraryFunction("path_id_to_name")(value)


def path_name_to_id(value: str) -> int:
    return LibraryFunction("path_name_to_id")(value)


@overload
def pick_pocket(pocketNumber: int) -> bool: ...


@overload
def pick_pocket(stat: Stat) -> dict[Stat, int]: ...


@overload
def pick_pocket(item: Item) -> dict[Item, int]: ...


@overload
def pick_pocket(effect: Effect) -> dict[Effect, int]: ...


@overload
def pick_pocket(monster: Monster) -> bool: ...


def pick_pocket(*args):
    return LibraryFunction("pick_pocket")(*args)


def picked_pockets() -> dict[int, bool]:
    return LibraryFunction("picked_pockets")()


def picked_scraps() -> dict[int, bool]:
    return LibraryFunction("picked_scraps")()


@overload
def ping(pingTest: str) -> dict[str, Any]: ...


@overload
def ping(count: int, page: str) -> dict[str, Any]: ...


@overload
def ping() -> dict[str, Any]: ...


def ping(*args):
    return LibraryFunction("ping")(*args)


def pocket_effects(pocket: int) -> dict[Effect, int]:
    return LibraryFunction("pocket_effects")(pocket)


def pocket_items(pocket: int) -> dict[Item, int]:
    return LibraryFunction("pocket_items")(pocket)


def pocket_joke(pocket: int) -> str:
    return LibraryFunction("pocket_joke")(pocket)


def pocket_meat(pocket: int) -> dict[int, str]:
    return LibraryFunction("pocket_meat")(pocket)


def pocket_monster(pocket: int) -> Monster:
    return LibraryFunction("pocket_monster")(pocket)


def pocket_poem(pocket: int) -> dict[int, str]:
    return LibraryFunction("pocket_poem")(pocket)


def pocket_scrap(pocket: int) -> dict[int, str]:
    return LibraryFunction("pocket_scrap")(pocket)


def pocket_stats(pocket: int) -> dict[Stat, int]:
    return LibraryFunction("pocket_stats")(pocket)


def poem_pockets() -> dict[int, int]:
    return LibraryFunction("poem_pockets")()


@overload
def potential_pockets(stat: Stat) -> dict[int, int]: ...


@overload
def potential_pockets(item: Item) -> dict[int, int]: ...


@overload
def potential_pockets(effect: Effect) -> dict[int, int]: ...


@overload
def potential_pockets(monster: Monster) -> dict[int, int]: ...


def potential_pockets(*args):
    return LibraryFunction("potential_pockets")(*args)


def pre_validate_adventure(location: Location) -> bool:
    return LibraryFunction("pre_validate_adventure")(location)


def prepare_for_adventure(location: Location) -> bool:
    return LibraryFunction("prepare_for_adventure")(location)


@overload
def print(string: str, color: str) -> None: ...


@overload
def print(string: str) -> None: ...


@overload
def print() -> None: ...


def print(*args):
    return LibraryFunction("print")(*args)


@overload
def print_html(string: str) -> None: ...


@overload
def print_html(string: str, logToSession: bool) -> None: ...


def print_html(*args):
    return LibraryFunction("print_html")(*args)


def property_default_value(nameValue: str) -> str:
    return LibraryFunction("property_default_value")(nameValue)


@overload
def property_exists(nameValue: str, globalValue: bool) -> bool: ...


@overload
def property_exists(nameValue: str) -> bool: ...


def property_exists(*args):
    return LibraryFunction("property_exists")(*args)


def property_has_default(nameValue: str) -> bool:
    return LibraryFunction("property_has_default")(nameValue)


def pulls_remaining() -> int:
    return LibraryFunction("pulls_remaining")()


@overload
def put_closet(count: int, item: Item) -> bool: ...


@overload
def put_closet(item: Item, count: int) -> bool: ...


@overload
def put_closet(item: Item) -> bool: ...


@overload
def put_closet(meat: int) -> bool: ...


def put_closet(*args):
    return LibraryFunction("put_closet")(*args)


@overload
def put_display(item: Item, count: int) -> bool: ...


@overload
def put_display(count: int, item: Item) -> bool: ...


def put_display(*args):
    return LibraryFunction("put_display")(*args)


@overload
def put_shop(
    priceValue: int, limitValue: int, qtyValue: int, itemValue: Item
) -> bool: ...


@overload
def put_shop(priceValue: int, limitValue: int, itemValue: Item) -> bool: ...


def put_shop(*args):
    return LibraryFunction("put_shop")(*args)


@overload
def put_shop_using_storage(
    priceValue: int, limitValue: int, qtyValue: int, itemValue: Item
) -> bool: ...


@overload
def put_shop_using_storage(
    priceValue: int, limitValue: int, itemValue: Item
) -> bool: ...


def put_shop_using_storage(*args):
    return LibraryFunction("put_shop_using_storage")(*args)


@overload
def put_stash(count: int, item: Item) -> bool: ...


@overload
def put_stash(item: Item, count: int) -> bool: ...


def put_stash(*args):
    return LibraryFunction("put_stash")(*args)


def pvp_attacks_left() -> int:
    return LibraryFunction("pvp_attacks_left")()


def rain_cost(skill: Skill) -> int:
    return LibraryFunction("rain_cost")(skill)


def random(range: int) -> int:
    return LibraryFunction("random")(range)


def raw_damage_absorption() -> int:
    return LibraryFunction("raw_damage_absorption")()


def read_ccs(name: str) -> str:
    return LibraryFunction("read_ccs")(name)


def receive_fax() -> None:
    return LibraryFunction("receive_fax")()


def refresh_shop() -> bool:
    return LibraryFunction("refresh_shop")()


def refresh_stash() -> bool:
    return LibraryFunction("refresh_stash")()


def refresh_status() -> bool:
    return LibraryFunction("refresh_status")()


@overload
def remove_item_condition(item: Item, count: int) -> None: ...


@overload
def remove_item_condition(count: int, item: Item) -> None: ...


def remove_item_condition(*args):
    return LibraryFunction("remove_item_condition")(*args)


@overload
def remove_property(nameValue: str, globalValue: bool) -> str: ...


@overload
def remove_property(nameValue: str) -> str: ...


def remove_property(*args):
    return LibraryFunction("remove_property")(*args)


def rename_property(oldNameValue: str, newNameValue: str) -> bool:
    return LibraryFunction("rename_property")(oldNameValue, newNameValue)


def replace(buffer: str, start: int, finish: int, s: str) -> str:
    return LibraryFunction("replace")(buffer, start, finish, s)


def replace_all(matcher: Matcher, replacement: str) -> str:
    return LibraryFunction("replace_all")(matcher, replacement)


def replace_first(matcher: Matcher, replacement: str) -> str:
    return LibraryFunction("replace_first")(matcher, replacement)


@overload
def replace_string(source: str, searchValue: str, replaceValue: str) -> str: ...


@overload
def replace_string(source: str, searchValue: str, replaceValue: str) -> str: ...


def replace_string(*args):
    return LibraryFunction("replace_string")(*args)


@overload
def reprice_shop(priceValue: int, limitValue: int, itemValue: Item) -> bool: ...


@overload
def reprice_shop(priceValue: int, itemValue: Item) -> bool: ...


def reprice_shop(*args):
    return LibraryFunction("reprice_shop")(*args)


@overload
def reset(matcher: Matcher, input: str) -> Matcher: ...


@overload
def reset(matcher: Matcher) -> Matcher: ...


def reset(*args):
    return LibraryFunction("reset")(*args)


def restoration_pockets() -> dict[int, bool]:
    return LibraryFunction("restoration_pockets")()


def restore_hp(amount: int) -> bool:
    return LibraryFunction("restore_hp")(amount)


def restore_mp(amount: int) -> bool:
    return LibraryFunction("restore_mp")(amount)


@overload
def retrieve_item(count: int, item: Item) -> bool: ...


@overload
def retrieve_item(item: Item, count: int) -> bool: ...


@overload
def retrieve_item(item: Item) -> bool: ...


def retrieve_item(*args):
    return LibraryFunction("retrieve_item")(*args)


@overload
def retrieve_price(count: int, item: Item, exact: bool) -> int: ...


@overload
def retrieve_price(item: Item, count: int, exact: bool) -> int: ...


@overload
def retrieve_price(count: int, item: Item) -> int: ...


@overload
def retrieve_price(item: Item, count: int) -> int: ...


@overload
def retrieve_price(item: Item) -> int: ...


def retrieve_price(*args):
    return LibraryFunction("retrieve_price")(*args)


@overload
def reverse_numberology(advDelta: int, spleenDelta: int) -> dict[int, int]: ...


@overload
def reverse_numberology() -> dict[int, int]: ...


def reverse_numberology(*args):
    return LibraryFunction("reverse_numberology")(*args)


def rollover() -> int:
    return LibraryFunction("rollover")()


def round(val: float) -> int:
    return LibraryFunction("round")(val)


@overload
def run_choice(decision: int, custom: bool, more: str) -> str: ...


@overload
def run_choice(decision: int, extra: bool) -> str: ...


@overload
def run_choice(decision: int, extra: str) -> str: ...


@overload
def run_choice(decision: int) -> str: ...


def run_choice(*args):
    return LibraryFunction("run_choice")(*args)


@overload
def run_combat(filterFunction: str) -> str: ...


@overload
def run_combat() -> str: ...


def run_combat(*args):
    return LibraryFunction("run_combat")(*args)


def run_turn() -> str:
    return LibraryFunction("run_turn")()


def runaway() -> str:
    return LibraryFunction("runaway")()


def sausage_goblin_chance() -> float:
    return LibraryFunction("sausage_goblin_chance")()


def scrap_pockets() -> dict[int, int]:
    return LibraryFunction("scrap_pockets")()


def sell(master: Coinmaster, countValue: int, itemValue: Item) -> bool:
    return LibraryFunction("sell")(master, countValue, itemValue)


def sell_price(master: Coinmaster, item: Item) -> int:
    return LibraryFunction("sell_price")(master, item)


def sells_item(master: Coinmaster, item: Item) -> bool:
    return LibraryFunction("sells_item")(master, item)


def send_fax() -> None:
    return LibraryFunction("send_fax")()


@overload
def session_logs(playerName: str, baseDate: str, count: int) -> dict[int, str]: ...


@overload
def session_logs(player: str, dayCount: int) -> dict[int, str]: ...


@overload
def session_logs(dayCount: int) -> dict[int, str]: ...


def session_logs(*args):
    return LibraryFunction("session_logs")(*args)


@overload
def set_auto_attack(attackValue: str) -> None: ...


@overload
def set_auto_attack(attackValue: int) -> None: ...


def set_auto_attack(*args):
    return LibraryFunction("set_auto_attack")(*args)


def set_ccs(name: str) -> bool:
    return LibraryFunction("set_ccs")(name)


def set_length(buffer: str, i: int) -> None:
    return LibraryFunction("set_length")(buffer, i)


def set_location(location: Location) -> None:
    return LibraryFunction("set_location")(location)


def set_property(nameValue: str, value: str) -> None:
    return LibraryFunction("set_property")(nameValue, value)


def shop_amount(item: Item) -> int:
    return LibraryFunction("shop_amount")(item)


def shop_limit(item: Item) -> int:
    return LibraryFunction("shop_limit")(item)


def shop_price(item: Item) -> int:
    return LibraryFunction("shop_price")(item)


@overload
def skill_modifier(item: Item, modifier: Modifier) -> Skill: ...


@overload
def skill_modifier(item: Item, modifier: str) -> Skill: ...


@overload
def skill_modifier(type: str, modifier: Modifier) -> Skill: ...


@overload
def skill_modifier(type: str, modifier: str) -> Skill: ...


def skill_modifier(*args):
    return LibraryFunction("skill_modifier")(*args)


def slash_count(item: Item) -> int:
    return LibraryFunction("slash_count")(item)


def soulsauce_cost(skill: Skill) -> int:
    return LibraryFunction("soulsauce_cost")(skill)


def spleen_limit() -> int:
    return LibraryFunction("spleen_limit")()


def split_modifiers(modifiers: str) -> dict[Modifier, str]:
    return LibraryFunction("split_modifiers")(modifiers)


@overload
def split_string(string: str, regex: str) -> dict[int, str]: ...


@overload
def split_string(string: str) -> dict[int, str]: ...


def split_string(*args):
    return LibraryFunction("split_string")(*args)


def square_root(val: float) -> float:
    return LibraryFunction("square_root")(val)


@overload
def start(matcher: Matcher, group: int) -> int: ...


@overload
def start(matcher: Matcher) -> int: ...


def start(*args):
    return LibraryFunction("start")(*args)


def starts_with(source: str, prefix: str) -> bool:
    return LibraryFunction("starts_with")(source, prefix)


def stash_amount(item: Item) -> int:
    return LibraryFunction("stash_amount")(item)


def stat_bonus_today() -> Stat:
    return LibraryFunction("stat_bonus_today")()


def stat_bonus_tomorrow() -> Stat:
    return LibraryFunction("stat_bonus_tomorrow")()


@overload
def stat_modifier(effect: Effect, modifier: Modifier) -> Stat: ...


@overload
def stat_modifier(effect: Effect, modifier: str) -> Stat: ...


def stat_modifier(*args):
    return LibraryFunction("stat_modifier")(*args)


def stats_pockets() -> dict[int, bool]:
    return LibraryFunction("stats_pockets")()


def steal() -> str:
    return LibraryFunction("steal")()


def stills_available() -> int:
    return LibraryFunction("stills_available")()


def stop_counter(label: str) -> None:
    return LibraryFunction("stop_counter")(label)


def storage_amount(item: Item) -> int:
    return LibraryFunction("storage_amount")(item)


@overload
def string_fact(monster: Monster) -> str: ...


@overload
def string_fact(cls: Class, path: Path, monster: Monster) -> str: ...


def string_fact(*args):
    return LibraryFunction("string_fact")(*args)


@overload
def string_modifier(effect: Effect, modifier: Modifier) -> str: ...


@overload
def string_modifier(effect: Effect, modifier: str) -> str: ...


@overload
def string_modifier(item: Item, modifier: Modifier) -> str: ...


@overload
def string_modifier(item: Item, modifier: str) -> str: ...


@overload
def string_modifier(type: str, modifier: Modifier) -> str: ...


@overload
def string_modifier(type: str, modifier: str) -> str: ...


@overload
def string_modifier(modifier: Modifier) -> str: ...


@overload
def string_modifier(modifier: str) -> str: ...


def string_modifier(*args):
    return LibraryFunction("string_modifier")(*args)


def stun_skill() -> Skill:
    return LibraryFunction("stun_skill")()


@overload
def substring(source: str, start: int, finish: int) -> str: ...


@overload
def substring(source: str, start: int) -> str: ...


def substring(*args):
    return LibraryFunction("substring")(*args)


def svn_at_head(project: str) -> bool:
    return LibraryFunction("svn_at_head")(project)


def svn_exists(project: str) -> bool:
    return LibraryFunction("svn_exists")(project)


def svn_info(script: str) -> dict[str, Any]:
    return LibraryFunction("svn_info")(script)


def svn_list() -> dict[int, str]:
    return LibraryFunction("svn_list")()


@overload
def sweet_synthesis(count: int, item1: Item, item2: Item) -> bool: ...


@overload
def sweet_synthesis(item1: Item, item2: Item) -> bool: ...


@overload
def sweet_synthesis(count: int, effect: Effect, flags: int) -> bool: ...


@overload
def sweet_synthesis(effect: Effect, count: int) -> bool: ...


@overload
def sweet_synthesis(count: int, effect: Effect) -> bool: ...


@overload
def sweet_synthesis(effect: Effect) -> bool: ...


def sweet_synthesis(*args):
    return LibraryFunction("sweet_synthesis")(*args)


@overload
def sweet_synthesis_pair(effect: Effect, flags: int) -> dict[int, Item]: ...


@overload
def sweet_synthesis_pair(effect: Effect) -> dict[int, Item]: ...


def sweet_synthesis_pair(*args):
    return LibraryFunction("sweet_synthesis_pair")(*args)


@overload
def sweet_synthesis_pairing(
    effect: Effect, item: Item, flags: int
) -> dict[int, Item]: ...


@overload
def sweet_synthesis_pairing(effect: Effect, item: Item) -> dict[int, Item]: ...


def sweet_synthesis_pairing(*args):
    return LibraryFunction("sweet_synthesis_pairing")(*args)


def sweet_synthesis_result(item1: Item, item2: Item) -> Effect:
    return LibraryFunction("sweet_synthesis_result")(item1, item2)


@overload
def take_closet(count: int, item: Item) -> bool: ...


@overload
def take_closet(item: Item, count: int) -> bool: ...


@overload
def take_closet(item: Item) -> bool: ...


@overload
def take_closet(meat: int) -> bool: ...


def take_closet(*args):
    return LibraryFunction("take_closet")(*args)


@overload
def take_display(count: int, item: Item) -> bool: ...


@overload
def take_display(item: Item, count: int) -> bool: ...


def take_display(*args):
    return LibraryFunction("take_display")(*args)


@overload
def take_shop(count: int, item: Item) -> bool: ...


@overload
def take_shop(itemValue: Item) -> bool: ...


def take_shop(*args):
    return LibraryFunction("take_shop")(*args)


@overload
def take_stash(count: int, item: Item) -> bool: ...


@overload
def take_stash(item: Item, count: int) -> bool: ...


def take_stash(*args):
    return LibraryFunction("take_stash")(*args)


@overload
def take_storage(count: int, item: Item) -> bool: ...


@overload
def take_storage(item: Item, count: int) -> bool: ...


def take_storage(*args):
    return LibraryFunction("take_storage")(*args)


@overload
def tavern(goal: str) -> int: ...


@overload
def tavern() -> int: ...


def tavern(*args):
    return LibraryFunction("tavern")(*args)


def throw_item(item: Item) -> str:
    return LibraryFunction("throw_item")(item)


def throw_items(item1: Item, item2: Item) -> str:
    return LibraryFunction("throw_items")(item1, item2)


def thunder_cost(skill: Skill) -> int:
    return LibraryFunction("thunder_cost")(skill)


def time_to_string() -> str:
    return LibraryFunction("time_to_string")()


def timestamp_to_date(timestamp: int, outFormat: str) -> str:
    return LibraryFunction("timestamp_to_date")(timestamp, outFormat)


@overload
def to_boolean(value: int) -> bool: ...


@overload
def to_boolean(value: bool) -> bool: ...


@overload
def to_boolean(value: str) -> bool: ...


def to_boolean(*args):
    return LibraryFunction("to_boolean")(*args)


def to_bounty(value: str) -> Bounty:
    return LibraryFunction("to_bounty")(value)


@overload
def to_buffer(value: str) -> str: ...


@overload
def to_buffer(value: str) -> str: ...


def to_buffer(*args):
    return LibraryFunction("to_buffer")(*args)


@overload
def to_class(value: int) -> Class: ...


@overload
def to_class(value: str) -> Class: ...


def to_class(*args):
    return LibraryFunction("to_class")(*args)


def to_coinmaster(value: str) -> Coinmaster:
    return LibraryFunction("to_coinmaster")(value)


@overload
def to_effect(skill: Skill) -> Effect: ...


@overload
def to_effect(id: int) -> Effect: ...


@overload
def to_effect(name: str) -> Effect: ...


def to_effect(*args):
    return LibraryFunction("to_effect")(*args)


def to_element(value: str) -> Element:
    return LibraryFunction("to_element")(value)


@overload
def to_familiar(id: int) -> Familiar: ...


@overload
def to_familiar(name: str) -> Familiar: ...


def to_familiar(*args):
    return LibraryFunction("to_familiar")(*args)


@overload
def to_float(value: float) -> float: ...


@overload
def to_float(value: int) -> float: ...


@overload
def to_float(value: bool) -> float: ...


@overload
def to_float(value: str) -> float: ...


def to_float(*args):
    return LibraryFunction("to_float")(*args)


@overload
def to_int(value: Path) -> int: ...


@overload
def to_int(value: Vykea) -> int: ...


@overload
def to_int(value: Servant) -> int: ...


@overload
def to_int(value: Thrall) -> int: ...


@overload
def to_int(value: Monster) -> int: ...


@overload
def to_int(value: Class) -> int: ...


@overload
def to_int(value: Effect) -> int: ...


@overload
def to_int(value: Skill) -> int: ...


@overload
def to_int(value: Location) -> int: ...


@overload
def to_int(value: Familiar) -> int: ...


@overload
def to_int(value: Item) -> int: ...


@overload
def to_int(value: float) -> int: ...


@overload
def to_int(value: int) -> int: ...


@overload
def to_int(value: bool) -> int: ...


@overload
def to_int(value: str) -> int: ...


def to_int(*args):
    return LibraryFunction("to_int")(*args)


@overload
def to_item(name: str, count: int) -> Item: ...


@overload
def to_item(value: int) -> Item: ...


@overload
def to_item(value: str) -> Item: ...


def to_item(*args):
    return LibraryFunction("to_item")(*args)


def to_json(val: Any) -> str:
    return LibraryFunction("to_json")(val)


@overload
def to_location(value: int) -> Location: ...


@overload
def to_location(value: str) -> Location: ...


def to_location(*args):
    return LibraryFunction("to_location")(*args)


def to_lower_case(string: str) -> str:
    return LibraryFunction("to_lower_case")(string)


def to_modifier(name: str) -> Modifier:
    return LibraryFunction("to_modifier")(name)


@overload
def to_monster(id: int) -> Monster: ...


@overload
def to_monster(name: str) -> Monster: ...


def to_monster(*args):
    return LibraryFunction("to_monster")(*args)


@overload
def to_path(value: int) -> Path: ...


@overload
def to_path(value: str) -> Path: ...


def to_path(*args):
    return LibraryFunction("to_path")(*args)


def to_phylum(value: str) -> Phylum:
    return LibraryFunction("to_phylum")(value)


def to_plural(item: Item) -> str:
    return LibraryFunction("to_plural")(item)


@overload
def to_servant(value: int) -> Servant: ...


@overload
def to_servant(value: str) -> Servant: ...


def to_servant(*args):
    return LibraryFunction("to_servant")(*args)


@overload
def to_skill(effect: Effect) -> Skill: ...


@overload
def to_skill(id: int) -> Skill: ...


@overload
def to_skill(name: str, type: str) -> Skill: ...


@overload
def to_skill(name: str) -> Skill: ...


def to_skill(*args):
    return LibraryFunction("to_skill")(*args)


@overload
def to_slot(item: Item) -> Slot: ...


@overload
def to_slot(item: str) -> Slot: ...


def to_slot(*args):
    return LibraryFunction("to_slot")(*args)


def to_stat(value: str) -> Stat:
    return LibraryFunction("to_stat")(value)


@overload
def to_string(val: float, fmt: str) -> str: ...


@overload
def to_string(val: int, fmt: str) -> str: ...


@overload
def to_string(val: str) -> str: ...


def to_string(*args):
    return LibraryFunction("to_string")(*args)


@overload
def to_thrall(value: int) -> Thrall: ...


@overload
def to_thrall(value: str) -> Thrall: ...


def to_thrall(*args):
    return LibraryFunction("to_thrall")(*args)


def to_upper_case(string: str) -> str:
    return LibraryFunction("to_upper_case")(string)


def to_url(value: Location) -> str:
    return LibraryFunction("to_url")(value)


def to_vykea(value: str) -> Vykea:
    return LibraryFunction("to_vykea")(value)


@overload
def to_wiki_url(value: Monster) -> str: ...


@overload
def to_wiki_url(value: Skill) -> str: ...


@overload
def to_wiki_url(value: Effect) -> str: ...


@overload
def to_wiki_url(value: Item) -> str: ...


@overload
def to_wiki_url(value: str) -> str: ...


def to_wiki_url(*args):
    return LibraryFunction("to_wiki_url")(*args)


def today_to_string() -> str:
    return LibraryFunction("today_to_string")()


def total_free_rests() -> int:
    return LibraryFunction("total_free_rests")()


def total_turns_played() -> int:
    return LibraryFunction("total_turns_played")()


def tower_door() -> bool:
    return LibraryFunction("tower_door")()


def traceprint(string: str) -> None:
    return LibraryFunction("traceprint")(string)


def track_copy_count(monster: Monster) -> int:
    return LibraryFunction("track_copy_count")(monster)


def track_ignore_queue(monster: Monster) -> bool:
    return LibraryFunction("track_ignore_queue")(monster)


def tracked_by(monster: Monster) -> dict[int, str]:
    return LibraryFunction("tracked_by")(monster)


def truncate(val: float) -> int:
    return LibraryFunction("truncate")(val)


def turns_per_cast(skill: Skill) -> int:
    return LibraryFunction("turns_per_cast")(skill)


def turns_played() -> int:
    return LibraryFunction("turns_played")()


def twiddle() -> str:
    return LibraryFunction("twiddle")()


def unusual_construct_disc() -> Item:
    return LibraryFunction("unusual_construct_disc")()


def update_candy_prices() -> None:
    return LibraryFunction("update_candy_prices")()


def url_decode(string: str) -> str:
    return LibraryFunction("url_decode")(string)


def url_encode(string: str) -> str:
    return LibraryFunction("url_encode")(string)


@overload
def use(count: int, item: Item) -> bool: ...


@overload
def use(item: Item, count: int) -> bool: ...


@overload
def use(item: Item) -> bool: ...


def use(*args):
    return LibraryFunction("use")(*args)


def use_familiar(familiar: Familiar) -> bool:
    return LibraryFunction("use_familiar")(familiar)


def use_servant(servant: Servant) -> bool:
    return LibraryFunction("use_servant")(servant)


@overload
def use_skill(skill: Skill) -> str: ...


@overload
def use_skill(count: int, skill: Skill, target: str) -> bool: ...


@overload
def use_skill(skill: Skill, count: int, target: str) -> bool: ...


@overload
def use_skill(count: int, skill: Skill) -> bool: ...


@overload
def use_skill(skill: Skill, count: int) -> bool: ...


def use_skill(*args):
    return LibraryFunction("use_skill")(*args)


@overload
def user_confirm(message: str, timeOut: int, defaultBoolean: bool) -> bool: ...


@overload
def user_confirm(message: str) -> bool: ...


def user_confirm(*args):
    return LibraryFunction("user_confirm")(*args)


@overload
def user_notify(message: str, onlyShowWhenHidden: bool) -> None: ...


@overload
def user_notify(message: str) -> None: ...


def user_notify(*args):
    return LibraryFunction("user_notify")(*args)


@overload
def user_prompt(message: str, timeOut: int, defaultString: str) -> str: ...


@overload
def user_prompt(message: str, options: dict[Any, Any]) -> str: ...


@overload
def user_prompt(message: str) -> str: ...


def user_prompt(*args):
    return LibraryFunction("user_prompt")(*args)


def visit(master: Coinmaster) -> bool:
    return LibraryFunction("visit")(master)


@overload
def visit_url(string: str, usePostMethod: bool, encoded: bool) -> str: ...


@overload
def visit_url(string: str, usePostMethod: bool) -> str: ...


@overload
def visit_url(string: str) -> str: ...


@overload
def visit_url() -> str: ...


def visit_url(*args):
    return LibraryFunction("visit_url")(*args)


@overload
def voting_booth_initiatives(
    clss: int, path: int, daycount: int
) -> dict[str, bool]: ...


@overload
def voting_booth_initiatives(
    clss: Class, path: Path, daycount: int
) -> dict[str, bool]: ...


def voting_booth_initiatives(*args):
    return LibraryFunction("voting_booth_initiatives")(*args)


def wait(delay: int) -> None:
    return LibraryFunction("wait")(delay)


def waitq(delay: int) -> None:
    return LibraryFunction("waitq")(delay)


def weapon_hands(item: Item) -> int:
    return LibraryFunction("weapon_hands")(item)


def weapon_type(item: Item) -> Stat:
    return LibraryFunction("weapon_type")(item)


def weight_adjustment() -> int:
    return LibraryFunction("weight_adjustment")()


def well_stocked(itemName: str, quantity: int, price: int) -> bool:
    return LibraryFunction("well_stocked")(itemName, quantity, price)


def white_citadel_available() -> bool:
    return LibraryFunction("white_citadel_available")()


def who_clan() -> dict[str, bool]:
    return LibraryFunction("who_clan")()


def will_usually_dodge() -> bool:
    return LibraryFunction("will_usually_dodge")()


def will_usually_miss() -> bool:
    return LibraryFunction("will_usually_miss")()


def write(string: str) -> None:
    return LibraryFunction("write")(string)


def write_ccs(data: str, name: str) -> bool:
    return LibraryFunction("write_ccs")(data, name)


def writeln(string: str) -> None:
    return LibraryFunction("writeln")(string)


def xpath(html: str, xpath: str) -> dict[int, str]:
    return LibraryFunction("xpath")(html, xpath)


def zap(item: Item) -> Item:
    return LibraryFunction("zap")(item)
