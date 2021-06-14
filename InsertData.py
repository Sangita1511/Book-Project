import pymysql
class Insert:
    def __init__(self):
        self.con=pymysql.connect(host="localhost",user="root",passwd="",database="book")
    def insert(self):
        print("Enter book no:")
        bn=int(input())
        print("Enter book name:")
        name=input()
        print("Enter book price:")
        p=int(input())

        query="insert into table1(Book_no,Book_name,Price) values(%s,%s,%s);"
        cur=self.con.cursor()
        cur.execute(query,(bn,name,p))
        self.con.commit()
        print("Data saved...")
        self.con.close()

