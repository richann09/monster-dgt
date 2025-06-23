import easygui

catalogue = {"Stoneling":
             {"Strength": 7,  "Speed": 1,  "Stealth": 25, "Cunning": 15},
             "Vexscream":
             {"Strength": 1,  "Speed": 6,  "Stealth": 21, "Cunning": 19},
             "Dawnmirage":
             {"Strength": 5,  "Speed": 15, "Stealth": 18, "Cunning": 22},
             "Blazegolem":
             {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
             "Websnake":
             {"Strength": 7,  "Speed": 15, "Stealth": 10, "Cunning": 5},
             "Moldvine":
             {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
             "Vortexwing":
             {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
             "Rotthing":
             {"Strength": 16, "Speed": 7,  "Stealth": 4,  "Cunning": 12},
             "Froststep":
             {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
             "Wispghoul":
             {"Strength": 17, "Speed": 19, "Stealth": 3,  "Cunning": 2}
}

categories = ["Strength", "Speed", "Stealth", "Cunning"]
MIN = 1
MAX = 25

def display_card(name_m, stats):
    result = name + ":\n"
    for stat_name, value in stats.items():
        result += " " + stat_name + ": " + str(value) + "\n"
    return result

def delete_cardm():
    """Remove a monster card from the catalogue."""
    name_m = easygui.enterbox("Enter the monster name to delete:", "Delete Monster Card.")

    if name_m in catalogue:
        confirm = easygui.buttonbox("Are you sure you want to delete " + name_m + "?", choices = ["Yes", "No"])
        if confirm == "Yes":
            del catalogue[name_m]
            easygui.msgbox("Card Deleted.")
    else:
        easygui.msgbox("No card was deleted", "Cancelled")

def search_card():
    """Look up a monster card by name and optionally update its stats."""
    name_m = easygui.enterbox("Enter monster name to serach:", "Search monster card")
    if not name_m:
        return

    if name_m in catalogue:
        stats = catalogue[name_m]
        monster_info = display_card(name_m, stats)
        edit = easygui.buttonbox("Found card:\n" + monster_info + "\n\nDo you want to edit this card?", choices = ["Yes", "No"])
        if edit == "Yes":
            for category in categories:
                value = easygui.integerbox("Edit " + category + " (any number):", default=stats[category])
                stats[category] = value
                catalogue[name_m] = stats
                easygui.msgbox("Card updated.")

    else:
        easygui.msgbox("Card not found")


    
    
