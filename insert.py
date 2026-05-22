import psycopg2
import numpy as np
import sys
import random

def get_embedding(text):
    # Generating random 128-dim vector as placeholder
    return np.random.rand(128).tolist()

def insert_text(text):
    conn = psycopg2.connect(
        dbname="lc",
        user="lc",
        password="lc",
        host="localhost",
        port="55432"
    )
    cur = conn.cursor()
    
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id            bigserial PRIMARY KEY,
            content       text,
            embedding     vector(128),
            jurisdiction  text,
            practice_area text,
            in_force      boolean,
            doc_date      date
        );
    """)
    
    embedding = get_embedding(text)
    
    # Randomly select other values
    jurisdiction = random.choice(["NZ", "AU", "UK"])
    practice_area = random.choice([
        "tax", "litigation", "property", "employment", "family", "immigration",
        "commercial", "criminal", "ip", "construction", "banking", "insolvency",
        "environment", "maritime", "tax_disputes", "trusts", "competition",
        "privacy", "health", "energy",
    ])
    in_force = random.random() < 0.25
    doc_date = f"20{random.randint(10, 25):02d}-{random.randint(1, 12):02d}-01"
    
    cur.execute(
        "INSERT INTO chunks (content, embedding, jurisdiction, practice_area, in_force, doc_date) VALUES (%s, %s, %s, %s, %s, %s);",
        (text, embedding, jurisdiction, practice_area, in_force, doc_date)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted: {text}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        insert_text(text)
    else:
        print("Please provide text as argument.")
