import psycopg2


def get_connection():
    
    return psycopg2.connect(
        host='localhost', port='5432', database='postgres', 
        user='admin', password='admin'
    )
