import mysql.connector

class Database():

    def __init__(self,host,user,password,database):

        self.host= host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        '''
        Intializes mydb and cursor

        Returns
        ------
        None
        '''
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.mydb.cursor()

        return

    def close(self):
        '''
        Disconencts mydb and cursor

        Returns
        ------
        None
        '''
        self.cursor.close()
        self.mydb.close()

        return

    def escapeString(self,sqlString):
        '''
        Escapes apostrophe to prevent sql injections

        Parameters
        ----------
        sqlString: str
            The injection string that may include apostrophes

        Returns
        ------
        sqlString: str
            The cleaned up version without the aopstrophes
        '''
        sqlString.replace('\'','')
        return sqlString

    def insert(self, userId, username, channel):
        '''
        Inserts a new user into the database

        Parameters
        ----------
        user: class
            The user to be inserted

        Returns
        ------
        None
        '''

        self.connect()

        sqlFormula = "INSERT INTO execList (userID, username, channel) VALUE (%s,%s,%s)"
        word = (self.escapeString(userId),self.escapeString(username),self.escapeString(channel))
        self.cursor.execute(sqlFormula,word)
        self.mydb.commit()
        self.close()

        return

    def fetch(self,table):
        '''
        Fetches users and combines them into a list

        Returns
        ------
        userArray: str[]
            A list of the users pulled from database
        '''
        self.connect()

        sqlFormula = "SELECT * FROM %s" % table
        self.cursor.execute(sqlFormula)
        myresults = self.cursor.fetchall()

        return myresults