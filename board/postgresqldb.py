'''
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

print('1111')

conn = psycopg2.connect(database="postgres", 
                        user="postgres", 
                        password="postgresql", 
                        host="database-1.c9cmi4aaygql.us-east-1.rds.amazonaws.com", 
                        port="5432") 


from flask import current_app, g
conn = psycopg2.connect(
            database=current_app.config['DB_DATABASE'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            host=current_app.config['DB_HOST'],
            port=current_app.config['DB_PORT']
)


from flask import current_app, g
conn = psycopg2.connect(
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
)


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )


conn.commit()

cur.close()
conn.close()



def conexionBD_0():
    conn = psycopg2.connect(
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()
    return cursor




def create_table():
    connection = conexionBD()
    cur=connection.cursor()
    cur.execute('DROP TABLE IF EXISTS losbooks;')
    cur.execute('CREATE TABLE losbooks (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
    connection.commit()
    cur.close()
    connection.close()

#create_table()
'''

import click
from flask import current_app, g
import os
import psycopg2
#from dotenv import load_dotenv

#load_dotenv()

def init_app(app):
    app.teardown_appcontext(close_db)   
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command():
    connection = conexionBD()
    cur=connection.cursor()   
    cur.execute('DROP TABLE IF EXISTS posts')
    connection.commit()
    cur.execute('''CREATE TABLE post (
                id SERIAL PRIMARY KEY,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                author VARCHAR(255) NOT NULL,
                message VARCHAR(255) NOT NULL
                )'''
                )
    connection.commit()
    cur.close()
    connection.close()
    click.echo("You successfully initialized the database!")


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def conexionBD():
    conn = psycopg2.connect(
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
    )
    return conn








