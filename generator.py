import sqlite3
import numpy as np

class DataGenerator:
    """
        A DataGenerator class that reads data from a SQLite database and returns in a batch
    """
    
    batch_size = 32
    maxlen = 40
    database=''
    
    def __init__(self, database, batch_size=32, maxlen=40):
        """
            Constructor method for the DataGenerator class
            
            # Arguments
                database: String
                    Link of the database
                batch_size: Integer
                    Size of each batch, Default size is 32
                maxlen: Integer
                    Max length of each sequence, Default is 40
        """
        
        # If there is a batch size provided, then setting it, else using the default
        if batch_size > 0:
            self.batch_size = batch_size
        
        # If there is max length, then setting it, else using the default
        if maxlen > 0:
            self.maxlen = maxlen
        
        # If there is database, then setting it, else thworing an ValueError
        if database and database != '':
            self.database = database
        else:
            raise ValueError("Please provide an valid database link")

        
    def ont_hot(self, seq, nxt):
        """
            DataGenerator class method one_hot for converting sequence into ont hot ventors
            
            # Arguments
                seq: List
                    List of sequences
                nxt: List
                    List of next characters
        """
        
        # Initializng numpy arrays
        x = np.zeros((self.batch_size, self.maxlen, 128), dtype=np.bool)
        y = np.zeros((self.batch_size, 128), dtype=np.bool)
        
        # Iterating through the seq and nxt
        for i, sentence in enumerate(seq):
            for t, char in enumerate(seq):
                x[i, t, char] = 1
            y[i, nxt[i]] = 1
            
        return x, y
    
    
    def generator(self):
        """
            DataGenerator class generator method generates batches of data 
            
            # Arguments
                No arguments
        """
        while True:
            # Initializng a SQLite database connection
            # TODO: Need to find a better way to find something
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            
            # Counter for tracking the index
            counter = 0
            
            # SQL query
            sql = "SELECT * FROM reviews LIMIT {} OFFSET {};".format(self.batch_size, counter * self.batch_size)
            
            # Updateing the counter
            counter += 1
            
            # Executing the sql
            cursor.execute(sql)
            
            # Fetching the data
            rows = cursor.fetchall()
            
            seq_arr = []
            nxt_arr = []
            
            # Converting the charcacters into ASCII numbers
            for seq, nxt in rows:
                temp = []
                for char in seq:
                    temp.append(ord(char))
                
                seq_arr.append(temp)
                nxt_arr.append(ord(nxt))
            
            yield self.ont_hot(seq_arr, nxt_arr)
