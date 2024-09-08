import psycopg2
from uuid import UUID, uuid4

conn = psycopg2.connect(host="localhost", dbname="SubstanceSecrets", user="postgres", password="merlayn313", port="5432")

cur = conn.cursor()
cur.connection.close()

#   //  Database CRUD Functions

def insertUser(name,emails,passwd, usage):
    """Inserts a new user into the database table users"""
    cur = conn.cursor()
    id = uuid4()    # NEED TO MAKE INCREMENTING NEW ID OR UUID
    username = name
    email = emails
    password = passwd
    history = usage

    cur.execute(f"""INSERT INTO users
    VALUES ('{id}', '{username}', '{email}', '{password}', '{history}')""")

    conn.commit()
    cur.close()
    conn.close()

def insertUsage (username, drugs, dose, roa):
    """Inserts a new usage record into database table history"""
    cur = conn.cursor()
    id = uuid4()
    user = username
    drug = drugs
    dosage = dose
    route = roa

    cur.execute(f"""INSERT INTO history
                VALUES ('{id}', '{user}', '{drug}', '{dosage}', '{route}');""")
    
    conn.commit()
    cur.close()
    conn.close()
