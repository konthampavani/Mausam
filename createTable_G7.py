import psycopg2

conn = psycopg2.connect(database="G7", user="test", password="root", host="localhost", port="5432")

cursor = conn.cursor()

query = '''
CREATE TABLE DB_G7 (
	id SERIAL PRIMARY KEY,
	node_id VARCHAR(50),
	device_type VARCHAR(20),
	tmp INTEGER,
	hmd INTEGER,
	dt DATE NOT NULL,
	tm TIME NOT NULL
);
'''

cursor.execute(query)

conn.commit()

cursor.close()
conn.close()

