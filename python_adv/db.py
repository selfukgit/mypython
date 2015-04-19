#*************Istructions for running the program at /home/python/python_adv/db.py :**************
#1.open my sql monitor by #mysql -u root -p with password Sujith@85
#2.#mysql> CREATE DATABASE TESTDB
#3.#CREATE USER 'user'@'localhost' IDENTIFIED BY 'user123'; (@@@@if connect("localhost","user","user123","TESTDB") if it is connect("localhost","root","Sujit@85","TESTDB") then this is not required only 1 and 2 required)
#4.#GRANT ALL ON TESTDB.* TO 'user'@'localhost';
#5.#quit
#REFERENCE : http://zetcode.com/db/mysqlpython/
#****************************************************************************************************

import MySQLdb

db = MySQLdb.connect("localhost","user","user123","TESTDB") #TESTDB should be already created DB
#db = MySQLdb.connect("localhost","root","Sujith@85","TESTDB") 
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print " Database Version : %s"%data #first row of DB is version name

db.close()
