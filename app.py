from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def load_home_template():
    return render_template('index.html')

@app.route("/weatherapp",methods=['POST','GET'])
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q': request.form['city'],
        'units': request.form.get('units'),
        'appid': request.form.get('appid')
    }
    weather_data_response = requests.get(url, params=param)
    return f"data:{weather_data_response.json()}"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5050)