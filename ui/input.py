import questionary


def input_password(message):
    try:
        password = int(questionary.password(message).ask())
        if password < 100000 or password > 999999:
            raise ValueError("Invalid password")

        return password

    except ValueError:
        print("密码格式不正确请重新输入")
        exit(1)


def input_phone_number(message):
    try:
        phone_number = int(questionary.text(message).ask())
        if phone_number < 1000000000 or phone_number > 999999999999:
            raise ValueError("Invalid phone_number")

        return phone_number

    except ValueError:
        print("输入的手机号格式错误!请重新输入")
        exit(1)


def input_user_name(message):
    try:
        name = questionary.text(message).ask()

        # 判断是否符合长度
        if len(name) < 3 or len(name) > 10:
            raise ValueError("Invalid name")

        # 判断是否为全中文
        for word in name:
            if not "\u4e00" <= word <= "\u9fa5":
                raise ValueError("Invalid name")

        return name
    except ValueError:
        print("用户名格式错误!请重新输入")
        exit(1)


def input_bank_code(message):
    try:
        bank_code = int(questionary.text(message).ask())
        bank_code = str(bank_code)
        if len(bank_code) < 17 or len(bank_code) > 19:
            raise ValueError("Invalid bank_code")

        return bank_code
    except ValueError:
        print("银行卡格式错误!请重新输入")
        exit(1)


def input_deposit(message):
    try:
        deposit = float(questionary.text(message).ask())
        MAX_INSERT = 50000

        if deposit > MAX_INSERT:
            raise ValueError("Invalid deposit")
        return deposit
    except ValueError:
        print("存款格式错误!请重新输入")
        exit(1)
