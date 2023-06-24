from db import init_db
from ui.menu import show_menu

def main():
    connect = init_db()
    show_menu(connect)
    connect.close()


if __name__ == "__main__":
    main()

