from flask import Flask, render_template
import data
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('infoscreen.html')

@app.route('/data/dvb/85')
def line_85():
    return json.dumps(data.dvb.getDirection('Mohorner Straße', '85'))

@app.route('/data/dvb/62')
def line_62():
    return json.dumps(data.dvb.getDirection('Mohorner Straße', '62'))

@app.route('/data/dvb/63')
def line_63():
    return json.dumps(data.dvb.getDirection('Würzburger Straße', '63'))

@app.route('/data/dvb/61')
def line_61():
    return json.dumps(data.dvb.getDirection('Tharandter Straße', '61'))

@app.route('/data/dvb/tharan')
def tharan():
    return json.dumps(data.dvb.getDepartures('Tharandter Straße'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
