# Code generated by ChatGPT

import re

def convert_enum(enum_code):
    # Find enum name
    enum_name = re.search(r'typedef\s+enum\s+(\w+)\s*{', enum_code).group(1)

    # Find enum items
    enum_items = re.findall(r'(\w+)\s*,', enum_code)

    # Mapping for special cases
    special_cases = {
        #"Seance": "Séance",        Unfortunately, OpenCL doesn't work nicely with the accented E...
        "Top up Tag": "Top-up Tag",
        "Riff raff": "Riff-raff",
        "Mail In Rebate": "Mail-In Rebate",
        "Mr Bones": "Mr. Bones",
        "Oops All 6s": "Oops! All 6s",
        "Drivers License": "Driver's License",
        "Directors Cut": "Director's Cut"
    }

    # Helper function to format enum item names
    def format_enum_item(enum_item):
        # Remove leading underscores
        enum_item = enum_item.lstrip("_")
        # Replace underscores with spaces
        enum_item = enum_item.replace("_", " ")
        # Handle special cases
        return special_cases.get(enum_item, enum_item)

    # Generate print function
    print_function = f"void print_{enum_name.lower()}({enum_name.lower()} i) {{\n"
    print_function += "    switch(i) {\n"
    for item in enum_items:
        formatted_item = format_enum_item(item)
        print_function += f'        case {item}: printf("{formatted_item}"); break;\n'
    print_function += "    }\n}\n"

    return print_function

# Example usage
enum_code = """
typedef enum Item {
    RETRY,

    //Jokers
    J_BEGIN,

    J_C_BEGIN,
    Joker,
    Greedy_Joker,
    Lusty_Joker,
    Wrathful_Joker,
    Gluttonous_Joker,
    Sly_Joker,
    Wily_Joker,
    Devious_Joker,
    Crafty_Joker,
    Gift_Card,
    Gros_Michel,
    Even_Steven,
    Odd_Todd,
    Misprint,
    Green_Joker,
    Photograph,
    Fortune_Teller,
    Drunkard,
    Popcorn,
    Swashbuckler,
    Credit_Card,
    Superposition,
    Raised_Fist,
    J_C_END,

    J_U_BEGIN,
    Four_Fingers,
    Banner,
    Fibonacci,
    Hack,
    Shortcut,
    Hologram,
    Vagabond,
    Ramen,
    Reserved_Parking,
    Bull,
    Throwback,
    Flower_Pot,
    Trading_Card,
    Diet_Cola,
    Spare_Trousers,
    J_U_END,

    J_R_BEGIN,
    Seance,
    Baseball_Card,
    Hit_the_Road,
    The_Trio,
    Invisible_Joker,
    Brainstorm,
    Obelisk,
    J_R_END,

    J_END,

    // Vouchers
    V_BEGIN,
    Overstock,
    Hone,
    Crystal_Ball,
    Grabber,
    Tarot_Merchant,
    Planet_Merchant,
    Seed_Money,
    Paint_Brush,
    V_END,

    // Tarots
    T_BEGIN,
    The_Fool,
    The_Magician,
    The_High_Priestess,
    The_Empress,
    The_Emperor,
    The_Hierophant,
    The_Lovers,
    The_Chariot,
    Justice,
    The_Hermit,
    The_Wheel_of_Fortune,
    Strength,
    The_Hanged_Man,
    Death,
    Temperance,
    The_Devil,
    The_Tower,
    The_Star,
    The_Moon,
    The_Sun,
    Judgement,
    The_World,
    T_END,

    // Planets
    P_BEGIN,
    Mercury,
    Venus,
    Earth,
    Mars,
    Jupiter,
    Saturn,
    Uranus,
    Neptune,
    Pluto,
    Planet_X,
    Ceres,
    Eris,
    P_END,

    // Hands
    H_BEGIN,
    Pair,
    Three_of_a_Kind,
    Full_House,
    Four_of_a_Kind,
    Flush,
    Straight,
    Two_Pair,
    Straight_Flush,
    High_Card,
    Five_of_a_Kind,
    Flush_House,
    Flush_Five,
    H_END,

    // Spectrals
    S_BEGIN,
    Familiar,
    Grim,
    Incantation,
    Talisman,
    Aura,
    Wraith,
    Sigil,
    Ouija,
    Ectoplasm,
    Immolate,
    Ankh,
    Deja_Vu,
    Hex,
    Trance,
    Medium,
    Cryptid,
    S_END,

    // Enhancements
    ENHANCEMENT_BEGIN,
    No_Enhancement,
    Bonus_Card,
    Mult_Card,
    Wild_Card,
    Glass_Card,
    Steel_Card,
    Stone_Card,
    Gold_Card,
    Lucky_Card,
    ENHANCEMENT_END,

    // Seals
    SEAL_BEGIN,
    No_Seal,
    Gold_Seal,
    Red_Seal,
    Blue_Seal,
    Purple_Seal,
    SEAL_END,

    // Editions
    E_BEGIN,
    No_Edition,
    Foil,
    Holographic,
    Polychrome,
    Negative,
    E_END,

    // Booster Packs
    PACK_BEGIN,
    Arcana_Pack,
    Jumbo_Arcana_Pack,
    Mega_Arcana_Pack,
    Celestial_Pack,
    Jumbo_Celestial_Pack,
    Mega_Celestial_Pack,
    Standard_Pack,
    Jumbo_Standard_Pack,
    Mega_Standard_Pack,
    Buffoon_Pack,
    Jumbo_Buffoon_Pack,
    Mega_Buffoon_Pack,
    Spectral_Pack,
    Jumbo_Spectral_Pack,
    Mega_Spectral_Pack,
    PACK_END,

    // Tags
    TAG_BEGIN,
    Uncommon_Tag,
    Rare_Tag,
    Negative_Tag,
    Foil_Tag,
    Holographic_Tag,
    Polychrome_Tag,
    Investment_Tag,
    Voucher_Tag,
    Boss_Tag,
    Standard_Tag,
    Charm_Tag,
    Meteor_Tag,
    Buffoon_Tag,
    Handy_Tag,
    Garbage_Tag,
    Ethereal_Tag,
    Coupon_Tag,
    Double_Tag,
    Juggle_Tag,
    D6_Tag,
    Top_up_Tag,
    Speed_Tag,
    Orbital_Tag,
    Economy_Tag,
    TAG_END,

    // Blinds
    B_START,
    Small_Blind,
    Big_Blind,
    The_Hook,
    The_Ox,
    The_House,
    The_Wall,
    The_Club,
    The_Fish,
    The_Manacle,
    The_Mouth,
    The_Tooth,
    The_Mark,
    Cerulean_Bell,
    B_END,

    // Suits
    SUIT_BEGIN,
    Hearts,
    Clubs,
    Diamonds,
    Spades,
    SUIT_END,

    // Ranks
    RANK_BEGIN,
    _2,
    _3,
    _4,
    _5,
    _6,
    _7,
    _8,
    _9,
    _10,
    Jack,
    Queen,
    King,
    Ace,
    RANK_END,

    // Cards
    C_BEGIN,
    C_2,
    C_3,
    C_4,
    C_5,
    C_6,
    C_7,
    C_8,
    C_9,
    C_A,
    C_J,
    C_K,
    C_Q,
    C_T,
    D_2,
    D_3,
    D_4,
    D_5,
    D_6,
    D_7,
    D_8,
    D_9,
    D_A,
    D_J,
    D_K,
    D_Q,
    D_T,
    H_2,
    H_3,
    H_4,
    H_5,
    H_6,
    H_7,
    H_8,
    H_9,
    H_A,
    H_J,
    H_K,
    H_Q,
    H_T,
    S_2,
    S_3,
    S_4,
    S_5,
    S_6,
    S_7,
    S_8,
    S_9,
    S_A,
    S_J,
    S_K,
    S_Q,
    S_T,
    C_END,

    ITEMS_END,
} item;
"""

print(convert_enum(enum_code))