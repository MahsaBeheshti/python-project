import sqlite3
from typing import List, Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Database1:

    def __init__(self, db_name):
        self.connection = sqlite3.connect("./mydatabase.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS laptops(
            user_id INTEGER PRIMARY KEY,
            price VARCHAR (50),
            brand VARCHAR (50),
            color VARCHAR (50),
            weight VARCHAR (50),
            gunus_and_species VARCHAR (50)
            );
        """
        self.cursor.execute(sql)
        self.connection.commit()
    #
    # def search_laptops(self, **kwargs) -> List[Tuple]:
    #     """
    #     Search laptops based on provided criteria
    #     Returns list of matching laptops
    #     """
    #     try:
    #         with self:
    #             conditions = []
    #             parameters = []
    #
    #             # Build dynamic query based on provided parameters
    #             if kwargs.get('min_price'):
    #                 conditions.append('price >= ?')
    #                 parameters.append(kwargs['min_price'])
    #             if kwargs.get('max_price'):
    #                 conditions.append('price <= ?')
    #                 parameters.append(kwargs['max_price'])
    #             if kwargs.get('brand'):
    #                 conditions.append('brand LIKE ?')
    #                 parameters.append(f"%{kwargs['brand']}%")
    #             if kwargs.get('color'):
    #                 conditions.append('color LIKE ?')
    #                 parameters.append(f"%{kwargs['color']}%")
    #             if kwargs.get('weight'):
    #                 conditions.append('weight = ?')
    #                 parameters.append(kwargs['weight'])
    #             if kwargs.get('gunus_and_species'):
    #                 conditions.append('gunus_and_species = ?')
    #                 parameters.append(kwargs['gunus_and_species'])
    #
    #             query = "SELECT * FROM laptop"
    #             if conditions:
    #                 query += " WHERE " + " AND ".join(conditions)
    #
    #             self.cursor.execute(query, parameters)
    #             return self.cursor.fetchall()
    #     except sqlite3.Error as e:
    #         logger.error(f"Error searching laptops: {e}")
    #         return []
    #
    # def add_sample_data(self):
    #     """Add sample laptop data for testing"""
    #     try:
    #         with self:
    #             laptop = [
    #                 ('36000000', 'Dell', "silver", "13.5", "plastick"),
    #                 ('20000000', 'Hp', "gold", "15", "plastick"),
    #                 ("45000000", "lenovo", "white", "14", "plastick"),
    #                 ('50000000', "apple", "red", "16", "plastick"),
    #             ]
    #             self.cursor.executemany("""
    #                 INSERT OR IGNORE INTO laptops (price, brand, color, weight, gunus_and_species)
    #                 VALUES ( ?, ?, ?, ?, ?)""", laptop)
    #             self.connection.commit()
    #     except sqlite3.Error as e:
    #         logger.error(f"Error adding sample data: {e}")
    #         raise


# import sqlite3
#
#
# class Database:
#     def __init__(self, db_name):
#         self.connection = sqlite3.connect(db_name)
#         self.cursor = self.connection.cursor()
#         self.create_table()
#
#     def create_table(self):
#         connection = sqlite3.connect('./mydatabasemain.db')
#         cursor = connection.cursor()
#         sql = """
#             CREATE TABLE IF NOT EXISTS user1(
#             user_id INTEGER PRIMARY KEY,
#             username VARCHAR (50),
#             password VARCHAR (50)
#             );
#         """
#         cursor.execute(sql)
#         connection.commit()
#         connection.close()
#
#     def insert_into_db(self,username,password):
#         try:
#             self.cursor.execute(
#                 "INSERT INTO user1 VALUES (NULL,?,?)",(username,password))
#             self.cursor.commit()
#             self.connection.close()
#         except:
#             return None
#
#     def value_table(self):
#         self.cursor.execute( """
#             INSERT INTO user1 VALUES (NULL, 'sara','5425' )
#             """)
#         self.connection.commit()
#
#
#
#
#     def close(self):
#         self.connection.close()
#
#     # def select_table():
#     #     connection = sqlite3.connect('./mydatabasemain.db')
#     #     cursor = connection.cursor()
#     #     cursor.execute('SELECT * FROM user1 ')
#     #     res = cursor.fetchone()
#     #     connection.commit()
#     #     connection.close()
#     #
#     # select_table()
#
#     def select_from_db(username):
#         connection = sqlite3.connect('./mydatabasemain.db')
#         cursor = connection.cursor()
#         cursor.execute('SELECT username FROM user1 WHERE username = ?', (username))
#         res = cursor.fetchone()
#         connection.commit()
#         connection.close()
