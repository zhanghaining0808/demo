import pymysql
import questionary

try:
    connect = pymysql.connect(
        host="localhost", user="root", password="test", database="bank"
    )
    connecter = connect.cursor()
except pymysql.DatabaseError as e:
    print(f"数据库连接失败:{e}")
    exit(1)


def add_user():
    user_id_card = "2131209231"
    user_deposit = "0.0"
    user_created_at = "21223222"
    user_name = questionary.text("你的用户名字:").ask()
    user_pwd = questionary.text("你的密码(6位数字):").ask()
    user_phone_number = questionary.text("你的手机号:").ask()
    user_bank = questionary.select("你使用的银行:", ["工商银行", "农业银行", "交通银行", "建设银行"]).ask()

    create_user_sql = f"""
    INSERT INTO bankuser 
    (
        id_card,
        deposit,
        user_name,
        password,
        created_at,
        phone_number,
        bank_name
    )
    VALUES
    (
        '{user_id_card}',
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
        connect.close()
        print("添加用户成功")
        print(f"以下是的用户数据:卡号:{user_id_card},\n存款为:{user_deposit},\n你的用户名:{user_name},\n你的密码:{user_pwd},\n创建时间为:{user_created_at},\n你的手机号为:{user_phone_number},\n你使用的银行为:{user_bank}") 
    except pymysql.DatabaseError as e:
        print(f"添加用户失败:{e}")
        connect.rollback()
        exit(1)

def add_deposit():
    pass
    connect.close()
