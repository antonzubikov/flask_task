from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # Замените на ваш API-ключ от OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            temp = round(data['main']['temp'] - 273.15, 2)  # Перевод в Цельсий
            description = data['weather'][0]['description']
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            return render_template('index.html', city=city, temp=temp, description=description, icon_url=icon_url)
        else:
            return "Город не найден."
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
