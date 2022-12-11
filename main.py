import psycopg2
import psycopg2.extras

hostname = '34.162.39.209'
database = 'postgres'
username = 'postgres'
pwd = 'bingo123'
port_id = 5432
conn = None
cur = None

#places = input('combien de places sont combless : ')
#update_script = 'UPDATE groupe SET nb_places_comblees = ' + places + ' WHERE id = 1'## + places <
def drop_table():
     cur.execute('DROP TABLE IF EXISTS groupe')

def create_table():
    create_script = ''' CREATE TABLE IF NOT EXISTS groupe (
                            id int PRIMARY KEY, 
                            no int NOT NULL,
                            nb_places_comblees int NOT NULL,
                            nb_places_max int NOT NULL,
                            prof varchar(30))'''
    cur.execute(create_script)

def insert_into():
    insert_script = 'INSERT INTO groupe (id, no, nb_places_comblees, nb_places_max, prof) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 4320, 10, 30, 'mamz'), (2,4320, 15, 30, 'Henri')]
    for record in insert_values:
        cur.execute(insert_script, record)

def update():
    update_script = 'UPDATE groupe SET nb_places_comblees = 1 WHERE id = 1'## + places <
    cur.execute(update_script)

def delete():
    delete_script = 'DELETE FROM groupe WHERE prof = %s'
    delete_record = ('henri',)
    cur.execute(delete_script, delete_record) 

def select_table():
    cur.execute('SELECT * FROM groupe')
    for record in cur.fetchall():
        print(record['no'], record['nb_places_comblees'], record['prof'])
    

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    drop_table()
    create_table()
    insert_into()
    update()
    delete()
    select_table()
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:  
        cur.close()
    if conn is not None:
        conn.close()    