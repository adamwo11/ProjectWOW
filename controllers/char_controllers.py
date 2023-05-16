from flask import render_template, request, redirect, session
import requests
from models.char import all_chars, get_char, create_char, update_char, delete_char, like_char
from services.session_info import current_user

def get_char_from_api(realm, name):
  # api_url = f'https://us.api.blizzard.com/profile/wow/character/{realm}/{name}?namespace=profile-us&locale=en_US&access_token=USWAvjnlORaReA2bL8QPt1HIfnrcDGRuCA'
  print('meow')
  print(realm)
  print(name)
  
  
  # response = requests.get(api_url).json()
  response = {
"_links": {
"self": {
"href": "https://us.api.blizzard.com/profile/wow/character/frostmourne/plumbob/appearance?namespace=profile-us"
}
},
"character": {
"key": {
"href": "https://us.api.blizzard.com/profile/wow/character/frostmourne/plumbob?namespace=profile-us"
},
"name": "Plumbob",
"id": 183636408,
"realm": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/realm/3725?namespace=dynamic-us"
},
"name": "Frostmourne",
"id": 3725,
"slug": "frostmourne"
}
},
"playable_race": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/playable-race/4?namespace=static-10.0.7_48520-us"
},
"name": "Night Elf",
"id": 4
},
"playable_class": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/playable-class/3?namespace=static-10.0.7_48520-us"
},
"name": "Hunter",
"id": 3
},
"active_spec": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/playable-specialization/254?namespace=static-10.0.7_48520-us"
},
"name": "Marksmanship",
"id": 254
},
"gender": {
"type": "MALE",
"name": "Male"
},
"faction": {
"type": "ALLIANCE",
"name": "Alliance"
},
"guild_crest": {
"emblem": {
"id": 92,
"media": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/media/guild-crest/emblem/92?namespace=static-10.0.7_48520-us"
},
"id": 92
},
"color": {
"id": 1,
"rgba": {
"r": 103,
"g": 35,
"b": 0,
"a": 1
}
}
},
"border": {
"id": 3,
"media": {
"key": {
"href": "https://us.api.blizzard.com/data/wow/media/guild-crest/border/3?namespace=static-10.0.7_48520-us"
},
"id": 3
},
"color": {
"id": 15,
"rgba": {
"r": 15,
"g": 20,
"b": 21,
"a": 1
}
}
},
"background": {
"color": {
"id": 45,
"rgba": {
"r": 35,
"g": 35,
"b": 35,
"a": 1
}
}
}
},
"items": [
{
"id": 129838,
"slot": {
"type": "HEAD",
"name": "Head"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 0,
"subclass": 3
},
{
"id": 173339,
"slot": {
"type": "SHOULDER",
"name": "Shoulders"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 2,
"subclass": 3
},
{
"id": 142503,
"slot": {
"type": "SHIRT",
"name": "Shirt"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 3,
"subclass": 5
},
{
"id": 173319,
"slot": {
"type": "CHEST",
"name": "Chest"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 4,
"subclass": 3
},
{
"id": 173342,
"slot": {
"type": "WAIST",
"name": "Waist"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 5,
"subclass": 3
},
{
"id": 175625,
"slot": {
"type": "LEGS",
"name": "Legs"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 6,
"subclass": 3
},
{
"id": 178745,
"slot": {
"type": "FEET",
"name": "Feet"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 7,
"subclass": 3
},
{
"id": 199448,
"slot": {
"type": "WRIST",
"name": "Wrist"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 8,
"subclass": 3
},
{
"id": 173328,
"slot": {
"type": "HANDS",
"name": "Hands"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 9,
"subclass": 3
},
{
"id": 173316,
"slot": {
"type": "BACK",
"name": "Back"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 14,
"subclass": 1
},
{
"id": 199307,
"slot": {
"type": "MAIN_HAND",
"name": "Main Hand"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 15,
"subclass": 3
},
{
"id": 142504,
"slot": {
"type": "TABARD",
"name": "Tabard"
},
"enchant": 0,
"item_appearance_modifier_id": 0,
"internal_slot_id": 18,
"subclass": 5
}
],
"customizations": [
{
"option": {
"name": "Skin Color",
"id": 40
},
"choice": {
"id": 700,
"display_order": 5
}
},
{
"option": {
"name": "Face",
"id": 41
},
"choice": {
"id": 719,
"display_order": 0
}
},
{
"option": {
"name": "Hair Style",
"id": 42
},
"choice": {
"name": "Mohawk",
"id": 747,
"display_order": 10
}
},
{
"option": {
"name": "Hair Color",
"id": 43
},
"choice": {
"id": 754,
"display_order": 5
}
},
{
"option": {
"name": "Beard",
"id": 44
},
"choice": {
"name": "Full",
"id": 765,
"display_order": 4
}
},
{
"option": {
"name": "Tattoo Color",
"id": 46
},
"choice": {
"name": "None",
"id": 8166,
"display_order": 0
}
},
{
"option": {
"name": "Horns",
"id": 47
},
"choice": {
"name": "None",
"id": 782,
"display_order": 0
}
},
{
"option": {
"name": "Blindfold",
"id": 48
},
"choice": {
"name": "None",
"id": 789,
"display_order": 0
}
},
{
"option": {
"name": "Tattoo",
"id": 376
},
"choice": {
"name": "Owl",
"id": 8152,
"display_order": 11
}
},
{
"option": {
"name": "Bear Form",
"id": 565
},
"choice": {
"id": 6513,
"display_order": 0
}
},
{
"option": {
"name": "Cat Form",
"id": 625
},
"choice": {
"id": 7150,
"display_order": 0
}
},
{
"option": {
"name": "Aquatic Form",
"id": 635
},
"choice": {
"id": 7218,
"display_order": 0
}
},
{
"option": {
"name": "Travel Form",
"id": 639
},
"choice": {
"id": 7234,
"display_order": 0
}
},
{
"option": {
"name": "Flight Form",
"id": 643
},
"choice": {
"id": 7253,
"display_order": 0
}
},
{
"option": {
"name": "Eye Color",
"id": 682
},
"choice": {
"id": 7607,
"display_order": 4
}
},
{
"option": {
"name": "Vines",
"id": 728
},
"choice": {
"name": "None",
"id": 8018,
"display_order": 0
}
},
{
"option": {
"name": "Vine Color",
"id": 730
},
"choice": {
"id": 8041,
"display_order": 1
}
},
{
"option": {
"name": "Ears",
"id": 734
},
"choice": {
"name": "Thin",
"id": 8062,
"display_order": 0
}
},
{
"option": {
"name": "Eyebrows",
"id": 738
},
"choice": {
"name": "Flat",
"id": 8084,
"display_order": 2
}
},
{
"option": {
"name": "Sideburns",
"id": 739
},
"choice": {
"name": "Groomed",
"id": 8108,
"display_order": 1
}
},
{
"option": {
"name": "Mustache",
"id": 740
},
"choice": {
"name": "Full",
"id": 8100,
"display_order": 2
}
},
{
"option": {
"name": "Scars",
"id": 742
},
"choice": {
"name": "Scratch",
"id": 8115,
"display_order": 2
}
},
{
"option": {
"name": "Moonkin Form",
"id": 924
},
"choice": {
"id": 15392,
"display_order": 0
}
},
{
"option": {
"name": "Skin Color",
"id": 1609
},
"choice": {
"name": "Blue Scales",
"id": 19598,
"display_order": 1
}
},
{
"option": {
"name": "Skin Scale Type",
"id": 1610
},
"choice": {
"name": "Heavy",
"id": 19596,
"display_order": 1
}
},
{
"option": {
"name": "Skin Color",
"id": 1611
},
"choice": {
"name": "Red Scales",
"id": 19612,
"display_order": 4
}
},
{
"option": {
"name": "Skin Scale Type",
"id": 1612
},
"choice": {
"name": "Heavy",
"id": 19603,
"display_order": 1
}
},
{
"option": {
"name": "Skin Color",
"id": 1615
},
"choice": {
"name": "Bronze Scales",
"id": 19625,
"display_order": 4
}
},
{
"option": {
"name": "Skin Scale Type",
"id": 1616
},
"choice": {
"name": "Standard",
"id": 19606,
"display_order": 0
}
},
{
"option": {
"name": "Horns",
"id": 1625
},
"choice": {
"name": "Grand Thorn",
"id": 19694,
"display_order": 5
}
},
{
"option": {
"name": "Crest",
"id": 1627
},
"choice": {
"name": "Hair",
"id": 19716,
"display_order": 6
}
},
{
"option": {
"name": "Brow",
"id": 1628
},
"choice": {
"name": "Bare",
"id": 19721,
"display_order": 0
}
},
{
"option": {
"name": "Ears",
"id": 1629
},
"choice": {
"name": "Horn",
"id": 19727,
"display_order": 2
}
},
{
"option": {
"name": "Jaw",
"id": 1630
},
"choice": {
"name": "Bare",
"id": 19729,
"display_order": 0
}
},
{
"option": {
"name": "Chin",
"id": 1631
},
"choice": {
"name": "Bare",
"id": 19733,
"display_order": 0
}
},
{
"option": {
"name": "Nose",
"id": 1632
},
"choice": {
"name": "Bare",
"id": 19739,
"display_order": 0
}
},
{
"option": {
"name": "Throat",
"id": 1633
},
"choice": {
"name": "Bare",
"id": 19743,
"display_order": 0
}
},
{
"option": {
"name": "Legs",
"id": 1634
},
"choice": {
"name": "Bare",
"id": 19745,
"display_order": 0
}
},
{
"option": {
"name": "Tail",
"id": 1635
},
"choice": {
"name": "Spikes",
"id": 19753,
"display_order": 6
}
},
{
"option": {
"name": "Back",
"id": 1636
},
"choice": {
"name": "Bare",
"id": 19756,
"display_order": 0
}
},
{
"option": {
"name": "Wings",
"id": 1637
},
"choice": {
"name": "Wings",
"id": 19759,
"display_order": 0
}
},
{
"option": {
"name": "Eyes",
"id": 1638
},
"choice": {
"name": "New 00",
"id": 19760,
"display_order": 0
}
},
{
"option": {
"name": "Body Armor",
"id": 1639
},
"choice": {
"name": "Saddle",
"id": 19762,
"display_order": 1
}
},
{
"option": {
"name": "Head Armor",
"id": 1640
},
"choice": {
"name": "None",
"id": 19764,
"display_order": 0
}
},
{
"option": {
"name": "Hair Color",
"id": 1648
},
"choice": {
"name": "White",
"id": 19781,
"display_order": 2
}
},
{
"option": {
"name": "Horn Color",
"id": 1649
},
"choice": {
"name": "Black",
"id": 19782,
"display_order": 0
}
},
{
"option": {
"name": "Pattern",
"id": 1651
},
"choice": {
"name": "Stripes",
"id": 19792,
"display_order": 1
}
},
{
"option": {
"name": "Armor Color",
"id": 1652
},
"choice": {
"name": "Gold and Green",
"id": 19799,
"display_order": 3
}
},
{
"option": {
"name": "Eyesight",
"id": 1656
},
"choice": {
"name": "Both",
"id": 19857,
"display_order": 0
}
},
{
"option": {
"name": "Eye Color",
"id": 1657
},
"choice": {
"id": 19861,
"display_order": 0
}
},
{
"option": {
"name": "Eye Style",
"id": 1658
},
"choice": {
"name": "Slit",
"id": 19904,
"display_order": 0
}
},
{
"option": {
"name": "Snout",
"id": 1659
},
"choice": {
"name": "Beaked",
"id": 19911,
"display_order": 4
}
},
{
"option": {
"name": "Horns",
"id": 1660
},
"choice": {
"name": "Ears",
"id": 19916,
"display_order": 3
}
},
{
"option": {
"name": "Crest",
"id": 1662
},
"choice": {
"name": "None",
"id": 19939,
"display_order": 0
}
},
{
"option": {
"name": "Jaw",
"id": 1664
},
"choice": {
"name": "Bare",
"id": 19954,
"display_order": 0
}
},
{
"option": {
"name": "Brow",
"id": 1666
},
"choice": {
"name": "Bare",
"id": 19965,
"display_order": 0
}
},
{
"option": {
"name": "Back",
"id": 1667
},
"choice": {
"name": "Bare",
"id": 19966,
"display_order": 0
}
},
{
"option": {
"name": "Tail",
"id": 1668
},
"choice": {
"name": "Maned",
"id": 19976,
"display_order": 5
}
},
{
"option": {
"name": "Throat",
"id": 1669
},
"choice": {
"name": "Finned",
"id": 19980,
"display_order": 2
}
},
{
"option": {
"name": "Eyes",
"id": 1670
},
"choice": {
"id": 19981,
"display_order": 0
}
},
{
"option": {
"name": "Body Armor",
"id": 1671
},
"choice": {
"name": "Saddle",
"id": 19983,
"display_order": 1
}
},
{
"option": {
"name": "Head Armor",
"id": 1672
},
"choice": {
"name": "Bare",
"id": 19985,
"display_order": 0
}
},
{
"option": {
"name": "Hair Color",
"id": 1673
},
"choice": {
"name": "Black",
"id": 19987,
"display_order": 0
}
},
{
"option": {
"name": "Horn Color",
"id": 1674
},
"choice": {
"name": "Tan",
"id": 19994,
"display_order": 0
}
},
{
"option": {
"name": "Pattern",
"id": 1675
},
"choice": {
"name": "None",
"id": 20014,
"display_order": 0
}
},
{
"option": {
"name": "Armor Color",
"id": 1676
},
"choice": {
"name": "Bronze and Green",
"id": 20009,
"display_order": 4
}
},
{
"option": {
"name": "Eyesight",
"id": 1680
},
"choice": {
"name": "Both",
"id": 20066,
"display_order": 0
}
},
{
"option": {
"name": "Eye Color",
"id": 1681
},
"choice": {
"id": 20070,
"display_order": 0
}
},
{
"option": {
"name": "Eye Style",
"id": 1682
},
"choice": {
"name": "Slit",
"id": 20113,
"display_order": 0
}
},
{
"option": {
"name": "Horns",
"id": 1683
},
"choice": {
"name": "Curled",
"id": 20119,
"display_order": 3
}
},
{
"option": {
"name": "Crest",
"id": 1684
},
"choice": {
"name": "Hair",
"id": 20128,
"display_order": 2
}
},
{
"option": {
"name": "Brow",
"id": 1685
},
"choice": {
"name": "Hair",
"id": 20137,
"display_order": 1
}
},
{
"option": {
"name": "Ears",
"id": 1686
},
"choice": {
"name": "Ears",
"id": 20141,
"display_order": 1
}
},
{
"option": {
"name": "Jaw",
"id": 1687
},
"choice": {
"name": "Hair",
"id": 20147,
"display_order": 2
}
},
{
"option": {
"name": "Chin",
"id": 1688
},
"choice": {
"name": "Hair",
"id": 20151,
"display_order": 1
}
},
{
"option": {
"name": "Nose",
"id": 1689
},
"choice": {
"name": "Horn",
"id": 20155,
"display_order": 1
}
},
{
"option": {
"name": "Throat",
"id": 1690
},
"choice": {
"name": "Hair",
"id": 20160,
"display_order": 2
}
},
{
"option": {
"name": "Legs",
"id": 1691
},
"choice": {
"name": "Bare",
"id": 20161,
"display_order": 0
}
},
{
"option": {
"name": "Tail",
"id": 1692
},
"choice": {
"name": "Spikes",
"id": 20164,
"display_order": 1
}
},
{
"option": {
"name": "Back",
"id": 1693
},
"choice": {
"name": "Hair",
"id": 20173,
"display_order": 1
}
},
{
"option": {
"name": "Wings",
"id": 1694
},
"choice": {
"name": "New 00",
"id": 20176,
"display_order": 0
}
},
{
"option": {
"name": "Armor",
"id": 1695
},
"choice": {
"name": "Saddle",
"id": 20178,
"display_order": 1
}
},
{
"option": {
"name": "Hair Color",
"id": 1697
},
"choice": {
"name": "Brown",
"id": 20187,
"display_order": 2
}
},
{
"option": {
"name": "Horn Color",
"id": 1698
},
"choice": {
"name": "Light",
"id": 20191,
"display_order": 1
}
},
{
"option": {
"name": "Pattern",
"id": 1699
},
"choice": {
"name": "Wide Stripes",
"id": 20194,
"display_order": 0
}
},
{
"option": {
"name": "Armor Color",
"id": 1700
},
"choice": {
"name": "Copper and Gray",
"id": 20197,
"display_order": 0
}
},
{
"option": {
"name": "Eyesight",
"id": 1704
},
"choice": {
"name": "Both",
"id": 20256,
"display_order": 0
}
},
{
"option": {
"name": "Eye Color",
"id": 1705
},
"choice": {
"id": 20260,
"display_order": 0
}
},
{
"option": {
"name": "Eye Style",
"id": 1706
},
"choice": {
"name": "Slit",
"id": 20303,
"display_order": 0
}
},
{
"option": {
"name": "Skin Scale Type",
"id": 1732
},
"choice": {
"name": "Light",
"id": 26486,
"display_order": 0
}
},
{
"option": {
"name": "Skin Color",
"id": 1733
},
"choice": {
"name": "Green Scales",
"id": 26491,
"display_order": 3
}
},
{
"option": {
"name": "Snout",
"id": 1734
},
"choice": {
"name": "Horn",
"id": 26502,
"display_order": 0
}
},
{
"option": {
"name": "Horns",
"id": 1735
},
"choice": {
"name": "Curved",
"id": 26510,
"display_order": 3
}
},
{
"option": {
"name": "Crest",
"id": 1737
},
"choice": {
"name": "Plates",
"id": 26526,
"display_order": 4
}
},
{
"option": {
"name": "Throat",
"id": 1738
},
"choice": {
"name": "Hair",
"id": 26532,
"display_order": 3
}
},
{
"option": {
"name": "Jaw",
"id": 1739
},
"choice": {
"name": "Long Ears",
"id": 26539,
"display_order": 3
}
},
{
"option": {
"name": "Back",
"id": 1741
},
"choice": {
"name": "Plate",
"id": 26553,
"display_order": 4
}
},
{
"option": {
"name": "Tail",
"id": 1742
},
"choice": {
"name": "Feathers",
"id": 26562,
"display_order": 6
}
},
{
"option": {
"name": "Eyes",
"id": 1743
},
"choice": {
"id": 26563,
"display_order": 0
}
},
{
"option": {
"name": "Body Armor",
"id": 1744
},
"choice": {
"name": "Bare",
"id": 26564,
"display_order": 0
}
},
{
"option": {
"name": "Head Armor",
"id": 1745
},
"choice": {
"name": "Bare",
"id": 26567,
"display_order": 0
}
},
{
"option": {
"name": "Fur Color",
"id": 1746
},
"choice": {
"name": "Gray",
"id": 26571,
"display_order": 2
}
},
{
"option": {
"name": "Horn Color",
"id": 1747
},
"choice": {
"name": "Black",
"id": 26574,
"display_order": 0
}
},
{
"option": {
"name": "Armor Color",
"id": 1748
},
"choice": {
"name": "Gold and Brown",
"id": 26579,
"display_order": 0
}
},
{
"option": {
"name": "Eyesight",
"id": 1761
},
"choice": {
"name": "Both",
"id": 26789,
"display_order": 0
}
},
{
"option": {
"name": "Eye Color",
"id": 1762
},
"choice": {
"id": 26793,
"display_order": 0
}
},
{
"option": {
"name": "Eye Style",
"id": 1763
},
"choice": {
"name": "Slit",
"id": 26836,
"display_order": 0
}
},
{
"option": {
"name": "Mouth",
"id": 1834
},
"choice": {
"name": "Toothy",
"id": 28246,
"display_order": 1
}
},
{
"option": {
"name": "Horn Style",
"id": 1847
},
"choice": {
"name": "Light",
"id": 28283,
"display_order": 0
}
},
{
"option": {
"name": "Horn Style",
"id": 1848
},
"choice": {
"name": "Light",
"id": 28285,
"display_order": 0
}
},
{
"option": {
"name": "Horn Style",
"id": 1850
},
"choice": {
"name": "Light",
"id": 28289,
"display_order": 0
}
},
{
"option": {
"name": "Head Armor",
"id": 1981
},
"choice": {
"name": "None",
"id": 29878,
"display_order": 0
}
},
{
"option": {
"name": "Pattern",
"id": 1992
},
"choice": {
"name": "None",
"id": 29995,
"display_order": 0
}
},
{
"option": {
"name": "Full Transformation",
"id": 2044
},
"choice": {
"name": "None",
"id": 30695,
"display_order": 0
}
},
{
"option": {
"name": "Full Transformation",
"id": 2962
},
"choice": {
"name": "None",
"id": 30703,
"display_order": 0
}
}
]
}

  return response 

def character():
  
  realm = request.args.get('realm')
  name = request.args.get('name')
  print(realm)
  print(name)
  char_info = get_char_from_api(realm, name)
  return render_template('chars/new_char.html', char_info=char_info)
# https://us.api.blizzard.com/profile/wow/character/frostmourne/plumbob?namespace=profile-us&locale=en_US&access_token=USWAvjnlORaReA2bL8QPt1HIfnrcDGRuCA


def index():
  chars = all_chars()
  return render_template('chars/index.html', chars=chars, current_user=current_user())

def new():
  return render_template('chars/generate.html')

def create():
  name = request.form.get('name')
  realm = request.form.get('realm')
  create_char(name, realm)
  return redirect('/')

def edit(id):
  char = get_char(id)
  return render_template('chars/edit.html', char=char)

def update(id):
  name = request.form.get('name')
  realm= request.form.get('realm')
  level= request.form.get('level')
  img_url = request.form.get('img_url')
  gender= request.form.get('gender')
  classes= request.form.get('class')
  race= request.form.get('race')
  faction= request.form.get('faction')
  update_char(id, name, realm, level, img_url, gender, classes, race, faction)
  return redirect('/')

def delete(id):
  delete_char(id)
  return redirect('/')

def like(id):
  like_char(id, session['user_id'])
  return redirect('/')

# def character():
#   name = request.args.get('name')
#   realm = request.args.get('realm')
#   print(realm)
#   print('bark')
#   char_info = get_char_from_api(realm, name)
#   return render_template('new_char', char_info=char_info)