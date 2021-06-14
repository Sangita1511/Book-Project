import pymysql
class Deletee:
    def __init__(self):
        self.con=pymysql.connect(host="localhost",user="root",passwd="",database="book")
    def delete(self):
        print("Enter book no to delete:")
        bn=int(input())
        query="delete from table1 where Book_no=%s;"
        cur=self.con.cursor()
        cur.execute(query,(bn))
        self.con.commit()
        print("Data deleted...")
        self.con.close()