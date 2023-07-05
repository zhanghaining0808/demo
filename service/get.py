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

        result = None
        is_can_login = False

        for user in users:
            if user[0] == user_bank_code:
                if user[1] == user_password:
                    is_can_login = True
                    result = user[0]
                    break

        return is_can_login, result

    except pymysql.DatabaseError as e:
        print(f"登录时发生错误:{e}")
        exit(1)


def get_deposit(connect, bank_code):
    connecter = connect.cursor()
    # select 你要取的哪些数据 from 数据表 ？where 表字段 = 实际数据
    get_deposit_sql = f"""
    select deposit from bankuser where bank_code = {bank_code};
    """

    try:
        connecter.execute(get_deposit_sql)
        user = connecter.fetchall()[0]  # 符合要求的第一个用户

        print(f"卡号{bank_code}存款还有:{user[0]}")  # 该用户的第一个字段
        exit(0)

    except pymysql.DatabaseError as e:
        print(f"查看存款时发生错误:{e}")
        exit(1)
