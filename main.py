import datetime
import webbrowser
CURRENT_DATE = datetime.date.today()
ISSUE_URL = "https://www.google.com"
TOTAL_MESSAGES = 0
TRACKED_ADDRESSES = []
KEYWORDS = ["work", "oppertunity", "interview", "hireing",
            "full-time", "part-time", "remote", "entry level", "jr", "web developer", "software developer", "software engineer", "requiter", "resume", "opening"]


def main():
    print("Hello welcome to E-mail bot...\n===MAIN MENU===\n1. Start Bot\n2. Report Issue\n3. About E-mail Bot\n4. Exit")
    selection = input("What would you like to do? [1-4]:")
    if(selection == "1"):
        start_bot()
    elif (selection == "2"):
        # Open to github issues page
        webbrowser.open_new_tab(ISSUE_URL)
        main()
    elif (selection == "3"):
        # print about text

        main()
    elif (selection == "4"):
        # exit program
        quit()
    else:
        print(
            f"Sorry but {selection} is not a valid option, please consult the main menu and try again.\n")
        main()


def start_bot():
    print("Starting Bot...")


# PROGRAM ENTRY POINT
main()
