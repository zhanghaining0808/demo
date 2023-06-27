import pymysql
import questionary
from tools.stamp import generate_stamp, convert_stamp
from ui.input import input_password, input_phone_number, input_user_name
from tools.bank_code import generate_bank_code


def add_user(connect):
    connecter = connect.cursor()
    user_bank = questionary.select("选择对应的银行:", ["工商银行", "农业银行", "交通银行", "建设银行"]).ask()
    user_bank_code = generate_bank_code(user_bank)
    user_created_at = generate_stamp()
    user_name = input_user_name("你的用户名字(3至10个字之间,全中文):")
    user_pwd = input_password("你的密码(6位数字):")
    user_phone_number = input_phone_number("你的手机号(11位):")
    user_deposit = 0.0

    create_user_sql = f"""
    INSERT INTO bankuser 
    (
        bank_code,
        deposit,
        user_name,
        password,
        created_at,
        phone_number,
        bank_name
    )
    VALUES
    (
        '{user_bank_code}',
        {user_deposit},
        '{user_name}',
        {user_pwd},
        {user_created_at},
        {user_phone_number},
        '{user_bank}'
    );
    """

    try:
        connecter.execute(create_user_sql)
        connect.commit()
        print("添加用户成功")
        print(
            f"以下是的用户数据:卡号:{user_bank_code},\n存款为:{user_deposit},\n你的用户名:{user_name},\n你的密码:{user_pwd},\n创建时间为:{convert_stamp(user_created_at)},\n你的手机号为:{user_phone_number},\n你使用的银行为:{user_bank}"
        )
    except pymysql.DatabaseError as e:
        print(f"添加用户失败:{e}")
        connect.rollback()
        exit(1)


def add_deposit():
    pass
