import pymysql
from ui.input import input_bank_code, input_password


def user_login(connect):
    connecter = connect.cursor()
    user_bank_code = input_bank_code("卡号(17至19位):")
    user_password = input_password("登录密码(6位数字):")

    get_all_bank_user_sql = """
    select bank_code,password from bankuser;
    """

    try:
        connecter.execute(get_all_bank_user_sql)
        users = connecter.fetchall()

        is_can_login = False

        for user in users:
            if user[0] == user_bank_code:
                if user[1] == user_password:
                    is_can_login = True
                    break

        if is_can_login:
            print("登录成功!")
        else:
            print("卡号或密码不正确,登录失败!")
            exit(1)

    except pymysql.DatabaseError as e:
        print(f"登录时发生错误:{e}")
        exit(1)


def get_deposit(connect):
    pass
