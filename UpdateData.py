import pymysql
class Update:
    def __init__(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="", database="book")
    def update(self):
        print("Enter book no to update record:")
        bn=int(input())
        print("Enter new price:")
        p=int(input())
        query="update table1 set Price=%s where Book_no=%s;"
        cur=self.con.cursor()
        cur.execute(query,(p,bn))
        self.con.commit()
        print("Updated....")
        self.con.close()