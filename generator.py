import sqlite3

from constants import DATABASE

class DataGenerator:
    connection = None
    cursor = None
    batch_size = 32
    counter = 0
    
    def __init__(self, database, batch_size=32):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.batch_size = batch_size
    
    def generator(self):
        while True:
            sql = "SELECT * FROM reviews LIMIT {} OFFSET {};".format(self.batch_size, self.counter * self.batch_size)
            
            self.counter += 1
            
            self.cursor.execute(sql)
            
            rows = self.cursor.fetchall()
            
            data = []
            
            for seq, nxt in rows:
                data.append([seq, nxt])
            
            yield data

generator = DataGenerator(DATABASE, 10)

counter = 0
for data in generator.generator():
    if counter>2:
        break
    
    print(data)
    print('')
    counter += 1
