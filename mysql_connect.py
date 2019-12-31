import mysql.connector
from mysql.connector import Error


def connect():
    global conn
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(auth_plugin='mysql_native_password',
                                       host='localhost',
                                       user='root',
                                       password='secure'
                                       )
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)
#    finally:
#        if conn is not None and conn.is_connected():
#            conn.close()


if __name__ == '__main__':
    connect()

cursor = conn.cursor()
cursor.execute('SHOW DATABASES')
DBs = cursor.fetchall()
for i in DBs:
    print(i)
    t = i[0].upper()
    print(t)
    cursor.execute(f'USE {t}')
    cursor.execute(f'SHOW TABLES')
    print(cursor.fetchall())
