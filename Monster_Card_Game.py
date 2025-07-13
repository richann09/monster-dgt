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

def display_card():
    """Display all the monster card in the catalogue"""

    display = "Monster catalpgue\n" + "=" * 20 + "\n\n"

    for name, stats in catalogue.items():
        display += name
        display += "Strength" + str(stats["strength"]) + "\n"
        display += "Speed" + str(stats["speed"]) + "\n"
        display += "Stealth" + str(stats["stealth"]) + "\n"
        display += "Cunning" + str(stats["cunning"]) + "\n"

    display += "Total monster card: " + str(len(catalogue))

    easygui.textbox("Monster card catalogue", "All cards", display)
    print(display)

        
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

def add_card():
    """Add a new card monster card"""
    name_m = easygui.enterbox("enter monster name:")
    if not name_m:
        return

    if name_m in catalogue:
        easygui.msgbox("monster card already exists!")


    strength = easygui.enterbox("Enter strength (1-25):")
    speed = easygui.enterbox("Enter speed (1-25):")
    stealth = easygui.enterbox("Enter stealth (1-25):")
    cunning = easygui.enterbox("Enter cunning (1-25):")

    try:
        strength = int(stength)
        speed = int(speed)
        stealth = int(stealth)
        cunning = int(cunning)

        if not (1 < strength < 25 and 1 < speed < 25 and 1 < stealth < 25 and 1 < cunning < 25):
            easygui.msgbox("all values must be between 1 to 25")
            return

        except:
            easygui.msgbox("Please enter valid numbers")
            return

        catalogue[name_m] = {
            "strength": strength,
            "speed": speed,
            "stealt": stealth,
            "cunning": cunning
            }

        easygui.msgbox(card_info, "card added")


def main():
    """main program"""
    easygui.msgbox("Welcome to Monster card catalogue")

    while True:
        choice = easygui.buttonbox("Choose an option:",
                                   "Monster card catalogue",
                                   ["Add monster", "Search/Edit Monster", "Delete monster", "Display Monster", "Exit"])

        if choice == "Add monster":
            add_card()
        elif choice == "Search/Edit Monster":
            search_card()
        elif choice == "Delete monster":
            delete_cardm
        elif choice == "Display Monster":
            display_card
        elif choice == "Exit":
            if easygui.ynbox("Are you sure u want to exit?", "Exit"):
                easygui.msgbox("Goodbye")
                break

if __name__ == "__main__":
    main()
