# Movies database class
import re
import sqlite3

class Movies:

    def __init__(self, dbname='anon_list'):
        'creates moves database and stores it in dbname.db'
        self.db = dbname
        self.conn = sqlite3.connect(self.db + '.db')
        cur = self.conn.cursor( )
        cur.execute( \
        '''create table if not exists movies(
           id integer primary key,
           title varchar(100),
           year integer,
           genres varchar(20),
           seen boolean
           );''')

    def load(self):
        'erases database and loads movie records from movies.txt'
        fd = open('movies.txt', 'r', encoding='utf-8')
        content = fd.read()
        fd.close()
        cur = self.conn.cursor()
        cur.execute("delete from movies;") # remove records first
        movie_list = re.findall(r'\d+\. (\S.*) \((\d\d\d\d)\)\s+Movies *(.*)\n', \
                           content)
        id = 1
        for item in movie_list:
            db_item = (id, item[0], int(item[1]), item[2], False)
            cur.execute("insert into movies values(?, ?, ?, ?, ?);", \
                db_item )
            id = id + 1
        self.conn.commit()

    def show(self):
        'print out all records in the movies table'
        cur = self.conn.cursor()
        cur.execute("select * from movies;")

        # Print results from query
        for m in cur.fetchall( ):
            print(m)

    def title_search(self, word):
        'return list of all movie records that match word string in title'
        cur = self.conn.cursor()
        pattern = '%' + word + '%'   # appending wildcard characters for match
        cur.execute("select * from movies where title like ? ;", [pattern] )
        return cur.fetchall()
    
    def genre_search(self,word):
        'return list of all movie records that match word string in title'
        cur = self.conn.cursor()
        pattern = '%' + word + '%'   # appending wildcard characters for match
        cur.execute("select * from movies where title like ? ;", [pattern] )
        return cur.fetchall()


    def delete(self, movie_id):
        'delete the movie whose id is movie_id'
        cur = self.conn.cursor()
        cur.execute("delete from movies where id = ?;", [movie_id])
        self.conn.commit()

    def mark_as_seen(self, movie_id):
        'mark the movie with movie_id as seen (set to true)'
        cur = self.conn.cursor()
        cur.execute("update movies set seen = ? where id = ?;", \
                    [True, movie_id])
        self.conn.commit()

    def show_seen(self):
        'print out all records that have been seen'
        cur = self.conn.cursor()
        cur.execute("select * from movies where seen = ?;", [True])

        # Print results from query
        for m in cur.fetchall( ):
            print(m)

    def show_notseen(self):
        'print out all records that have been seen'
        cur = self.conn.cursor()
        cur.execute("select * from movies where seen = ?;", [False])

        # Print results from query
        for m in cur.fetchall( ):
            print(m)
            
    def close(self):
        'close the database connection'
        self.conn.close()
