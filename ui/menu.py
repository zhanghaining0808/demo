import questionary
from service.add import add_user
from service.update import store_deposit, take_deposit
from service.get import user_login, get_deposit

primary_options = {
    "注册账号": add_user,
    "登录账号": user_login,
    "退出程序": exit,
}

user_options = {
    "存入存款": store_deposit,
    "取出存款": take_deposit,
    "查看存款": get_deposit,
    "退出程序": exit,
}


def show_primary_menu(connect):
    selected = questionary.select("请选择以下功能:", primary_options).ask()

    if selected == "退出程序":
        print("欢迎下次光临 OvO bye~")
        primary_options.get(selected)(1)

    if selected == "登录账号":
        is_can_show_user_menu, login_bank_code = primary_options.get(selected)(connect)
        if is_can_show_user_menu:
            print("登录成功")
            print(f"卡号:{login_bank_code}已登录")
            show_user_menu(connect, login_bank_code)
            exit(1)
        else:
            print("登录失败,银行卡或密码错误")
            exit(1)

    primary_options.get(selected)(connect)


def show_user_menu(connect, bank_code):
    selected = questionary.select("请选择以下功能:", user_options).ask()
    if selected == "退出程序":
        print("欢迎下次光临 OvO bye~")
        user_options.get(selected)(1)
    user_options.get(selected)(connect, bank_code)
