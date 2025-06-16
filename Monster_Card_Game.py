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

def delete_cardm():
    """Remove a monster card from the catalogue."""
    name_m = easygui.enterbox("Enter the monster name to delete:", "Delete Monster Card.")
    if not name_m:
        return

    if name_m not in catalogue:
        easygui.msgbox("No card found with the name " + name_m + ".", "Not Found")

    if name_m in catalogue:
            if easygui.buttonbox("Are you sure you want to delete" + name_m + "?", choices = ["Yes", "No"],
                                 "Confirm deletion")):
                del catalogue[name_m]
                easygui.msgbox(name_m + " has been deleted from the catalogue.", "deleted")

    else:
        easygui.msgbox("No card was deleted", "Cancelled")
            
    
