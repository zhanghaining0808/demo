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
        phone_number=int(questionary.text(message).ask())
        if phone_number < 1000000000 or phone_number > 999999999999:
            raise ValueError("Invalid phone_number")
       
        return phone_number
    
    except ValueError:
        print("输入的手机号格式错误!请重新输入")
        exit(1)