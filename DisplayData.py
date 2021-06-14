import pymysql
class Display:
    def __init__(self):
        self.con=pymysql.connect(host="localhost",user="root",passwd="",database="book")
    def display(self):
        query="select * from table1;"
        cur=self.con.cursor()
        cur.execute(query)
        data=cur.fetchall()

        for i in data:
            for j in i:
                print(j,end="  ")
            print()
        self.con.close()
