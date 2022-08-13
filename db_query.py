import os
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

#cur.execute("SELECT * FROM Variants")

cur.execute("SELECT Samples.CD_num, Samples.Panel, Variants.Coding, Variants.AA_change FROM Samples INNER JOIN Variants ON Samples.CD_num=Variants.CD_num;")

#cur.execute("SELECT * FROM Samples WHERE Fusion_status LIKE 'Fusion%'")
result = cur.fetchall()

for x in result:
    print(x)
