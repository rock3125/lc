import psycopg2
import numpy as np
import sys
import argparse

def get_embedding(text):
    # Generating random 128-dim vector as placeholder
    # In a real scenario, this would call your embedding model
    return np.random.rand(128).tolist()

def search_text(query_text, jurisdiction=None, practice_area=None):
    conn = psycopg2.connect(
        dbname="lc",
        user="lc",
        password="lc",
        host="localhost",
        port="55432"
    )
    cur = conn.cursor()

    embedding = get_embedding(query_text)

    # Base query
    query = "SELECT content, 1 - (embedding <=> %s::vector) AS score FROM chunks"
    params = [embedding]
    
    filters = []
    if jurisdiction:
        filters.append("jurisdiction = %s")
        params.append(jurisdiction)
    if practice_area:
        filters.append("practice_area = %s")
        params.append(practice_area)
        
    if filters:
        query += " WHERE " + " AND ".join(filters)
        
    query += " ORDER BY embedding <=> %s::vector LIMIT 5;"
    params.append(embedding)
    
    cur.execute(query, tuple(params))
    results = cur.fetchall()

    print(f"Top 5 matches for: {query_text} (Jurisdiction: {jurisdiction}, Area: {practice_area})")
    print("-" * 50)
    for row in results:
        content, score = row
        print(f"Score: {score:.4f} | Content: {content}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vector Search App with Filters")
    parser.add_argument("query", type=str, help="Query text")
    parser.add_argument("--jurisdiction", type=str, help="Filter by jurisdiction")
    parser.add_argument("--practice_area", type=str, help="Filter by practice area")

    args = parser.parse_args()

    search_text(args.query, args.jurisdiction, args.practice_area)
