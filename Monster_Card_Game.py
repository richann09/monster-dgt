
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

    display = "Monster catalogue\n" + "=" * 20 + "\n\n"

    for name, stats in catalogue.items():
        display += name + "\n"
        display += " Strength: " + str(stats["Strength"]) + "\n"
        display += " Speed: " + str(stats["Speed"]) + "\n"
        display += " Stealth: " + str(stats["Stealth"]) + "\n"
        display += " Cunning: " + str(stats["Cunning"]) + "\n\n"

    display += "\nTotal monster card: " + str(len(catalogue))

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
    name_m = easygui.enterbox("Enter monster name to search:", "Search monster card")
    if not name_m:
        return

    if name_m in catalogue:
        stats = catalogue[name_m]

        m_info = name_m + "\n"
        m_info += " Strength: " + str(stats["Strength"]) + "\n"
        m_info += " Speed: " + str(stats["Speed"]) + "\n"
        m_info += " Stealth: " + str(stats["Stealth"]) + "\n"
        m_info += " Cunning: " + str(stats["Cunning"]) + "\n"
        
        edit = easygui.buttonbox("Found card:\n" + m_info + "\n\nDo you want to edit this card?", choices = ["Yes", "No"])
        if edit == "Yes":
            for category in categories:
                value = easygui.integerbox("Edit " + category + " (1-25):", default=stats[category])
                if value is not None and 1 < value < 25:
                    stats[category] = value
                else:
                    easygui.msgbox("Please put valid numbers for " + category + ". (Between 1-25)")
                    return
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
        strength = int(strength)
        speed = int(speed)
        stealth = int(stealth)
        cunning = int(cunning)

        # checks the numbers added are between 1-25
        if not (1 <= strength <= 25 and 1 <= speed <= 25 and 1 <= stealth <= 25 and 1 <= cunning <=25):
            easygui.msgbox("all values must be between 1 to 25")
            return

    except:
        easygui.msgbox("Please enter valid numbers")
        return

    monster_temp = {
        "Strength": strength,
        "Speed": speed,
        "Stealth": stealth,
        "Cunning": cunning
        }
    while True:
        details_c = "Confirm the monster card details:\n\n"
        details_c += " " + name_m + "\n"
        details_c += "Strength" + str(monster_temp["Strength"]) + "\n"
        details_c += "Speed" + str(monster_temp["Speed"]) + "\n"
        details_c += "Stealth" + str(monster_temp["Stealth"]) + "\n"
        details_c += "Cunning" + str(monster_temp["Cunning"]) + "\n\n"
        details_c += "Are these details correct?"

        confirm_card = easygui.buttonbox(details_c, "Confirm Monster card", ["Yes, add", "No, make changes"])

        if confirm_card == "Yes, add":
            catalogue[name_m] = monster_temp
            easygui.msgbox("Card added successfully to the catalogue!", "Card Added")
            break

        elif confirm_card == "No, make changes":
            edit_c = ["Strength", "Speed", "Stealth", "Cunning"]

            edit_d = "Which one would you like to edit?\n\n"
            edit_d += "Strength: " + str(monster_temp["Strength"]) + "\n"
            edit_d += "Speed: " + str(monster_temp["Speed"]) + "\n"
            edit_d += "Stealth: " + str(monster_temp["Stealth"]) + "\n"
            edit_d += "Cunning: " + str(monster_temp["Cunning"]) + "\n"

            choice = easygui.choicebox(edit_d, "Edit monster card", edit_c)

            if choice:
                current_i = monster_temp[choice]
                new_i = easygui.integerbox("enter new " + choice + " (1-25):", default=current_i)

                if new_i is not None and 1 <= new_i <= 25:
                    monster_temp[choice] = new_i
                    easygui.msgbox(choice + " updated to " + str(new_i))
                else:
                    easygui.msgbox("Invalid numbers. " + choice + "Between 1-25")
        
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
            delete_cardm()
        elif choice == "Display Monster":
            display_card()
        elif choice == "Exit":
            if easygui.ynbox("Are you sure u want to exit?", "Exit"):
                easygui.msgbox("Goodbye")
                break

if __name__ == "__main__":
    main()
