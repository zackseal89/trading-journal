from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('trades.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/add_trade', methods=['POST'])
def add_trade():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trades (date, time, symbol, position, entry_price, exit_price, profit_loss, trade_size, strategy, indicators, reason, stop_loss, take_profit, emotions, emotional_triggers, distractions, mistakes, comments, market_conditions, news_events)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['date'], data['time'], data['symbol'], data['position'], data['entry_price'], data['exit_price'], data['profit_loss'], data['trade_size'], data['strategy'], data['indicators'], data['reason'], data['stop_loss'], data['take_profit'], data['emotions'], data['emotional_triggers'], data['distractions'], data['mistakes'], data['comments'], data['market_conditions'], data['news_events']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Trade added successfully'})

@app.route('/analytics', methods=['GET'])
def analytics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trades')
    trades = cursor.fetchall()
    conn.close()
    return render_template('analytics.html', trades=trades)

if __name__ == '__main__':
    app.run(debug=True)
