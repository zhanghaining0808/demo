import pymysql
import questionary


def log_off_user(connect, bank_code):
    is_can_log_off = questionary.confirm(f"您确定要注销{bank_code}用户吗").ask()

    if not is_can_log_off:
        print("您以取消该操作")
        exit(0)

    connecter = connect.cursor()
    log_off_sql = f"""
    delete from bankuser where bank_code = {bank_code}
    """
    try:
        connecter.execute(log_off_sql)

    except pymysql.DatabaseError as e:
        print(f"注销账户发生错误: {e}")
        exit(1)
