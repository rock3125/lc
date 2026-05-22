import psycopg2
import numpy as np
import sys

def get_embedding(text):
    # Generating random 128-dim vector as placeholder
    # In a real scenario, this would call your embedding model
    return np.random.rand(128).tolist()

def search_text(query_text):
    conn = psycopg2.connect(
        dbname="lc",
        user="lc",
        password="lc",
        host="localhost",
        port="55432"
    )
    cur = conn.cursor()

    embedding = get_embedding(query_text)

    # Cosine similarity is 1 - cosine_distance (<=>)
    # Using the same table name 'chunks' as in vector_app.py
    query = """
        SELECT content, 1 - (embedding <=> %s::vector) AS score
        FROM chunks
        ORDER BY embedding <=> %s::vector
        LIMIT 5;
    """
    
    cur.execute(query, (embedding, embedding))
    results = cur.fetchall()

    print(f"Top 5 matches for: {query_text}")
    print("-" * 50)
    for row in results:
        content, score = row
        print(f"Score: {score:.4f} | Content: {content}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_text = " ".join(sys.argv[1:])
        search_text(query_text)
    else:
        print("Please provide query text as argument.")
