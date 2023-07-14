from flask import Flask, jsonify, make_response
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


conn = psycopg2.connect(database="G7", user="test", password="root", host="localhost", port="5432")
cur = conn.cursor()

@app.route('/show_data')
def show_data():
	cur.execute("SELECT * FROM DB_G7")
	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append({'ID': row[0], 'Node ID' :  row[1], 'Device Type' : row[2], 'Temperature': row[3], 'Humidity': row[4], 'Date': str(row[5]), 'Time': str(row[6])})
	return jsonify(data)

@app.route('/particular_time')
def particular_time():
	cur.execute("SELECT * FROM DB_G7 WHERE tm='01:07:27'")
	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append({'ID': row[0], 'Node ID' :  row[1], 'Device Type' : row[2], 'Temperature': row[3], 'Humidity': row[4], 'Date': str(row[5]), 'Time': str(row[6])})
	return jsonify(data)
	
@app.route('/display_tmp')
def display_tmp():
	cur.execute("SELECT tmp FROM DB_G7")
	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append({'Temperature': row[0]})
	return jsonify(data)
	
@app.route('/average_tmp')
def average_tmp():
	cur.execute("SELECT AVG(tmp) FROM DB_G7")
	avg = cur.fetchone()[0]
	avg = format(avg, ".2f")
	print(avg)
	return jsonify({'average': avg})

@app.route('/average_hmd')
def average_hmd():
	cur.execute("SELECT AVG(hmd) FROM DB_G7")
	avg = cur.fetchone()[0]
	avg_rounded = round(avg, 2)
	return jsonify({'average': avg_rounded})


@app.route('/current_tmp')
def fetch_tmp():
	cur.execute(f"SELECT tmp FROM DB_G7 ORDER BY id DESC LIMIT 1")
	curr_tmp = cur.fetchone()[0]
	return jsonify({'current temp': curr_tmp})
	
	
@app.route('/current_hmd')
def fetch_hmd():
	cur.execute(f"SELECT hmd FROM DB_G7 ORDER BY id DESC LIMIT 1")
	curr_hmd = cur.fetchone()[0]
	return jsonify({'current hmd': curr_hmd})

@app.route('/show_tmp')
def show_temperature(start_date='2023-04-14',end_date='2023-04-15',start_time='14:00:00',end_time='12:30:00'):
    #start_date = request.args.get('start-date')
    #end_date = request.args.get('end-date')
    #start_time = request.args.get('start-time')
    #end_time = request.args.get('end-time')
    query="SELECT id,tmp,hmd,dt,tm FROM DB_G7 WHERE (dt >= '" +start_date+"'::date AND dt <= '"+end_date+"'::date) AND ( tm >= '" +start_time+"' AND tm <= '"+end_time+"')"
    cur.execute(query)
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append({'ID':row[0],'Temperature': row[1],'Humidity': row[2],'Date': row[3], 'Time': str(row[4])})
    return jsonify(data)

	
@app.route('/show_hmd')
def show_humidity(start_date='2023-04-14',end_date='2023-04-14',start_time='01:05:57',end_time='02:16:55'):
	query="SELECT id,hmd,dt,tm FROM DB_G7 WHERE (dt >= '" +start_date+"'::date AND dt <= '"+end_date+"'::date) AND ( tm >= '" +start_time+"' AND tm <= '"+end_time+"')"
	cur.execute(query)
	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append({'ID':row[0],'Humidity': row[1],'Date': row[2], 'Time': str(row[3])})
	return jsonify(data)
	
@app.route('/show_both')
def show_tmperature_humidity(start_date,end_date,start_time,end_time):
	query="SELECT tmp,hmd,dt,tm FROM DB_G7 WHERE (dt >= '" +start_date+"'::date AND dt <= '"+end_date+"'::date) AND ( tm >= '" +start_time+"' AND tm <= '"+end_time+"')"
	cur.execute(query)
	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append({'Temperature': row[0],'Humidity': row[1],'Date': row[2], 'Time': str(row[3])})
	return jsonify(data)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,port=9007)
