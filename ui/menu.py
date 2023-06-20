import questionary
from service.add import add_deposit
from service.add import add_user
from service.update import update_deposit
from service.get import get_deposit

options = {
    "注册账号":add_user,
    "存入存款":add_deposit,
    "取出存款":update_deposit,
    "查看存款":get_deposit,
}

def show_menu():
    selected = questionary.select("请选择以下功能:",options).ask()
    options.get(selected)()