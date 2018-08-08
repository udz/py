import pyodbc

class Database:
    #server = '192.168.1.47' 
    server = 'localhost'
    database = 'WEEKEND'
    username = 'sa'
    password = '123456'
    
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        #print('Connection Successful!')
    
    def query_select(self,q):
        try:
            cursor = self.connection.cursor()
            #cursor = self.connection.cursor(pyodbc.cursors.DictCursor)  # DictCursor is available in MySQL but not in pyodbc
            cursor.execute(q)
            # Following lines return Dictionary object
            columns =  [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns,row)))
            return results
        except pyodbc.Error as err:
            self.connection.rollback()
            print('There was a problem with SQL\n',err.args[0],err.args[1])
            return -1

    def query(self,q):
        cursor = self.connection.cursor()
        cursor.execute(q)
        return cursor.fetchall()

    def query_insert(self,q,data):
        cursor = self.connection.cursor()
        cursor.executemany(q,data)
        cursor.commit()
        #return cursor.fetchall()

    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
    db = Database()
    
    q = "SELECT * FROM tbl_stock"
    
    q1 = """
        INSERT INTO tbl_stock
        (item,weekday,price)
        VALUES
        ('item5','Mon',999),
        ('item5','Tue',948),
        ('item5','Wed',453),
        ('item5','Thu',122),
        ('item5','Fri',199)
        """
    q2 = """
        INSERT INTO tbl_stock
        (item,weekday,price)
        VALUES
        (?,?,?)"""
    t =(
        ('item4','Mon',120),
        ('item4','Tue',125),
        ('item4','Wed',133),
        ('item4','Thu',170),
        ('item4','Fri',188)
    )
    #db.query_insert(q2,t)
    
    rows = db.query_select(q)

    if rows != -1:
        for row in rows:
            print(row['item'],row['weekday'],row['price'],row)
            #print(row['item'],row['weekday'],row['price'],row)

    '''
    fetchone
    fetchall
    commit
    rollback
    executemany -- can pass tuple object template
    executescript -- multiple SQL statements separated by ;
    '''