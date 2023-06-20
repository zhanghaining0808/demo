import pymysql


def init_db():
    try:
        connect = pymysql.connect(
            host="localhost", user="root", password="test", database="bank"
        )
        connecter = connect.cursor()
        print("数据库连接成功")
<<<<<<< HEAD
    except:
        print("数据库连接失败")

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS bankuser
    (
        id INT PRIMARY KEY AUTO_INCREMENT,
        id_card TEXT NOT NULL,      
        deposit FLOAT NOT NULL,
        user_name TEXT NOT NULL,
        password INT NOT NULL, 
        create_at BIGINT NOT NULL,
        phone_number BIGINT NOT NULL,
        bank_name enum('工商银行','农业银行','交通银行','建设银行')
    ) engine=InnoDB charset=utf8;
    """

    connecter.execute(create_table_sql)

    # add_user_sql = """
    # INSERT INTO 
    # bankuser(
    #     id_card,      
    #     deposit,
    #     user_name,
    #     password, 
    #     create_at,
    #     phone_number,
    #     bank_name
    # ) 
    # values(
    #     '2535708702',
    #     50000.0,
    #     'zhanghaining',
    #     253570,
    #     202306170042,
    #     15216138606,
    #     '农业银行'
    # );
    # """
    # try:
    #     connecter.execute(add_user_sql)
    #     # 提交到数据库执行
    #     connect.commit()
    #     print("用户添加成功")
    # except:
    #     connect.rollback()
    #     print("用户添加失败")

    connect.close()
=======
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS bankuser
        (
            id INT PRIMARY KEY AUTO_INCREMENT,
            id_card TEXT NOT NULL,    
            deposit FLOAT NOT NULL,
            user_name TEXT NOT NULL,
            password INT NOT NULL, 
            create_at BIGINT NOT NULL,
            phone_number BIGINT NOT NULL,
            bank_name enum('工商银行','农业银行','交通银行','建设银行')
        ) engine=InnoDB charset=utf8;
        """
        connecter.execute(create_table_sql)
        print("数据表已生成")
        connect.close()
    except pymysql.DatabaseError as e:
        print(f"数据库连接失败:{e}")
        exit(1)
>>>>>>> 26346ed1fd8305f029519f8b442ad18c4adf6e33
