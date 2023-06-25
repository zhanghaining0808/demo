from db import init_db
from ui.menu import show_menu


def main():
    try:
        connect = init_db()
        show_menu(connect)
        connect.close()
    except Exception as e:
        print(f"程序崩溃,发生异常:{e}")


if __name__ == "__main__":
    main()
