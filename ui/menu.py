import questionary
from service.add import add_deposit, add_user
from service.update import update_deposit
from service.get import user_login, get_deposit

options = {
    "注册账号": add_user,
    "登录账号": user_login,
    "存入存款": add_deposit,
    "取出存款": update_deposit,
    "查看存款": get_deposit,
    "退出程序": exit,
}


def show_menu(connect):
    selected = questionary.select("请选择以下功能:", options).ask()
    if selected == "退出程序":
        print("欢迎下次光临 OvO bye~")
        options.get(selected)(1)
    options.get(selected)(connect)
