import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS user1(
            user_id INTEGER PRIMARY KEY,
            username VARCHAR (50),
            password INTEGER (50)
            );
        """
        self.cursor.execute(sql)
        self.connection.commit()

    def insert_to_db(self,username,password):
        self.cursor.execute('INSERT INTO user1 VALUES(NULL,?,?)',(username,password))
        self.connection.commit()
        # self.connection.close()
    def close(self):
        self.connection.close()
    def insert(self):

        user = ('3','lina','123456789')
        self.cursor.execute('INSERT INTO user1 VALUES (NULL,?,?);',user)
        self.connection.commit()
        self.connection.close()

    def select_table(self,username):
        self.cursor.execute('SELECT * FROM user1 WHERE username=?',(username,))
        res = self.cursor.fetchone()
        self.connection.commit()
        return res

    def select_from_db(self):
        self.cursor.execute('SELECT * FROM user1')
        res = self.cursor.fetchall()
        self.connection.commit()

    def value_table(self):
        # connection = sqlite3.connect('./mydatabasemain.db')
        # cursor = connection.cursor()
        sql = """
           INSERT INTO user1 VALUES (NULL, 'mahsa','5245' 
                       """
        self.cursor.execute(sql)
        self.connection.commit()

# *******************************************


    # def insert_into_db(self):
    #     try:
    #         self.cursor.execute(
    #             "INSERT INTO user1 (user_id , username , password) VALUES (NULL,?,?)")
    #         self.connection.commit()
    #         print('create a acount ')
    #
    #     except:
    #         print('please try agine')


    # select_table()1
#

# select_from_db()




# import sqlite3
#
# def create_table():
#     connection = sqlite3.connect('./mydatabasemain.db')
#     cursor = connection.cursor()
#     sql = """
#         CREATE TABLE IF NOT EXISTS user1(
#         user_id INTEGER PRIMARY KEY,
#         username VARCHAR (50),
#         password VARCHAR (50)
#         );
#     """
#     cursor.execute(sql)
#     connection.commit()
#     connection.close()
#
#
# create_table()
#
#

#
#
#
# select_table()
#
# def select_from_db(username):
#     connection = sqlite3.connect('./mydatabasemain.db')
#     cursor = connection.cursor()
#     cursor.execute('SELECT username FROM user1 WHERE username = ?',  (username))
#     res = cursor.fetchone()
#     connection.commit()
#     connection.close()
#
#
# select_table()
#
#
#
#
#
#
#
#
#
#
#
# #
# # def distnct_table():
# #     connection = sqlite3.connect('./mydatabasemain.db')
# #     cursor = connection.cursor()
# #     sql = """
# #         SELECT username , password FROM user1
# #     """
# #     cursor.execute(sql)
# #     connection.commit()
# #     connection.close()
# #
#
# # distnct_table()
#
#
#
#
# # def update_table():
# #     connection = sqlite3.connect('./mydatabasemain.db')
# #     cursor = connection.cursor()
# #     sql = """
# #         DELETE FROM user1 WHERE phone = '09157140358';
# #     """
# #     cursor.execute(sql)
# #     connection.commit()
# #     connection.close()
#
#
# create_table()
#
#
#
