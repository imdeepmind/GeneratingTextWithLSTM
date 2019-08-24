import sqlite3
import numpy as np

class DataGenerator:
    connection = None
    cursor = None
    batch_size = 32
    maxlen = 40
    database=''
    counter = 0
    
    def __init__(self, database, batch_size=32, maxlen=40):
        self.batch_size = batch_size
        self.maxlen = maxlen
        self.database=database
        
    def ont_hot(self, seq, nxt):
        x = np.zeros((self.batch_size, self.maxlen, 128), dtype=np.bool)
        y = np.zeros((self.batch_size, 128), dtype=np.bool)
        
        for i, sentence in enumerate(seq):
            for t, char in enumerate(seq):
                x[i, t, char] = 1
            y[i, nxt[i]] = 1
            
        return x, y
    
    def generator(self):
        while True:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            
            sql = "SELECT * FROM reviews LIMIT {} OFFSET {};".format(self.batch_size, self.counter * self.batch_size)
            
            self.counter += 1
            
            self.cursor.execute(sql)
            
            rows = self.cursor.fetchall()
            
            seq_arr = []
            nxt_arr = []
            
            for seq, nxt in rows:
                temp = []
                for char in seq:
                    temp.append(ord(char))
                
                seq_arr.append(temp)
                nxt_arr.append(ord(nxt))
            
            yield self.ont_hot(seq_arr, nxt_arr)
