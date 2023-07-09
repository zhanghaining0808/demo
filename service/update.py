import pymysql
from ui.input import input_deposit


def store_deposit(connect, bank_code):
    connecter = connect.cursor()
    get_deposit_sql = f"""
    select deposit from bankuser where bank_code = {bank_code};
    """
    # 现在存款 = 原存款+新增存款

    try:
        connecter.execute(get_deposit_sql)
        user = connecter.fetchall()[0]
        old_deposit = user[0]
        new_deposit = input_deposit("请输入你要存入的存款：")
        now_deposit = old_deposit + new_deposit

        update_deposit_sql = f"""
        update bankuser set deposit={now_deposit} where bank_code = {bank_code}
        """
        connecter.execute(update_deposit_sql)

        print(f"存款{new_deposit}已存入,该账户总存款为：{now_deposit}")
        exit(0)

    except pymysql.DatabaseError as e:
        print(f"存入存款时发生错误：{e}")
        exit(1)


def take_deposit(connect, bank_code):
    pass
