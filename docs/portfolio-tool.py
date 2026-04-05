import os
import webbrowser

# -----------------------------
# Portfolio Data (EDIT THIS)
# -----------------------------
portfolio = {

    "name": "Name: Amjad Hassan",
    "role": "Python Developer | Automation | Web Scraping", 
    "projects": [
        {
            "name": "BuffaloEx Tracking Scraper",
            "description": "Scrapes tracking data from Buffalo website and displays it.",
            "tech": "Python, Selenium, Flask",
            "link": "https://github.com/ahaulakh0890/mywsportfolio/blob/main/docs/projects/tracking-scraper-flask.md"
        },
        {
            "name": "Inventory Management System",
            "description": "Manages inventory with CRUD operations.",
            "tech": "Python, SQLite",
            "link": "https://github.com/ahaulakh0890/mywsportfolio/blob/main/docs/projects/Inventory-management.md"
        },
        {
            "name": "Book Scraper",
            "description": "Scrapes books data from online sources.",
            "tech": "Python, Scrapy",
            "link": "https://github.com/ahaulakh0890/mywsportfolio/blob/main/docs/projects/book-scraper.md"
        }
    ]
}

# -----------------------------
# Functions
# -----------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print("=" * 40)
    print(f"{portfolio['name']}")
    print(f"{portfolio['role']}")
    print("=" * 40)

def show_projects():
    print("\n📂 Projects:\n")
    for i, project in enumerate(portfolio["projects"], start=1):
        print(f"{i}. {project['name']}")
    print("0. Back")

def show_project_details(index):
    project = portfolio["projects"][index]
    clear()
    show_header()
    
    print(f"\n🔹 {project['name']}")
    print(f"📖 {project['description']}")
    print(f"🛠 Tech: {project['tech']}")
    print(f"🔗 Link: {project['link']}")
    
    choice = input("\nOpen in browser? (y/n): ")
    if choice.lower() == 'y':
        webbrowser.open(project["link"])

def main_menu():
    while True:
        clear()
        show_header()
        print("\n1. View Projects")
        print("2. About Me")
        print("3. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            while True:
                clear()
                show_header()
                show_projects()

                try:
                    p_choice = int(input("\nSelect project: "))
                    if p_choice == 0:
                        break
                    elif 1 <= p_choice <= len(portfolio["projects"]):
                        show_project_details(p_choice - 1)
                        input("\nPress Enter to continue...")
                except:
                    print("Invalid input!")
                    input("Press Enter...")

        elif choice == "2":
            clear()
            show_header()
            print("\n👋 About Me:\n")
            print("I am a Python developer specializing in automation, scraping, and web tools.")
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("\nGoodbye 👋")
            print("\n")
            break

        else:
            print("Invalid choice!")
            input("Press Enter...")

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    main_menu()