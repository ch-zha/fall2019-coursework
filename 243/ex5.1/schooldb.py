import mysql.connector

cnx = mysql.connector.connect(user='root', password='sesame80',
                              host='localhost',
                              database='ap')
cnx.close()