
import psycopg2
import psycopg2.extras
from flask import Flask,render_template,request

#pour se connecter à la base de données 
hostname = '34.162.39.209'
database = 'postgres'
username = 'postgres'
pwd = 'bingo123'
port_id = 5432
conn = None
cur = None

#fonctions préfaites pour jouer avec la base de données
def drop_table(table):
     cur.execute('DROP TABLE IF EXISTS ' + table)
     conn.commit()

def create_table():
    create_script = ''' CREATE TABLE IF NOT EXISTS groupe(
                            id int PRIMARY KEY, 
                            no int NOT NULL,
                            nb_places_comblees int NOT NULL,
                            nb_places_max int NOT NULL,
                            prof varchar(30))'''
    print(create_script)
    cur.execute(create_script)
    conn.commit()

def insert_into():
    insert_script = 'INSERT INTO groupe (id, no, nb_places_comblees, nb_places_max, prof) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 4320, 10, 30, 'mamz'), (2,4320, 15, 30, 'Henri')]
    for record in insert_values:
        cur.execute(insert_script, record)
        conn.commit()

def update():
    update_script = 'UPDATE groupe SET nb_places_comblees = 1 WHERE id = 1'## + places <
    cur.execute(update_script)
    conn.commit()

def delete():
    delete_script = 'DELETE FROM groupe WHERE prof = %s'
    delete_record = ('henri',)
    cur.execute(delete_script, delete_record) 
    conn.commit()

def select_table(table):
    cur.execute('SELECT * FROM ' + table)
    for record in cur.fetchall():
        #print(record['no'], record['nb_places_comblees'], record['prof'])
        # resultat = return resultat
        print (record)
        conn.commit()

def sql_execute(commande):
    cur.execute(commande)
    for record in cur.fetchall():
        #print(record['no'], record['nb_places_comblees'], record['prof'])
        # resultat = return resultat
        print (record)
        conn.commit()
    

#definition pour la page html
def start_page(app):
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("index.html")
        

    @app.route("/result",methods = ['POST',"GET"])
    def result():
        output = request.form.to_dict()
        name = output["name"]
        print(name)
        sql_execute(name)
        return render_template("index.html",name = name)

    @app.route("/result2",methods = ['POST',"GET"])
    def result_table():
        output = request.form.to_dict()
        name = output["name"]
        print(name)
        #create_table()
        select_table(name)
        return render_template("index.html",name = name)
        
        
    @app.route("/result3",methods = ['POST',"GET"])
    def delete_table():
        output = request.form.to_dict()
        name = output["name"]
        print(name)
        drop_table(name)
        #create_table()
        return render_template("index.html",name = name)


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    app = Flask(__name__)
    start_page(app)

    


    #passer des valeur à la page html 

    if __name__ == "__main__":
        app.run(debug=True)
    # code de la page html qui communique avec le code
except Exception as error:
    print(error)

finally:
    if cur is not None:  
        cur.close()
    if conn is not None:
        conn.close()    