# Weather App

The Weather App is a simple and intuitive application that allows users to check the current weather conditions of a specific location. With a clean and user-friendly interface, users can quickly access essential weather information such as temperature, humidity, wind speed, and more. and a 5-day forecast. The app is built using [OpenWeatherMap API](https://openweathermap.org/) to fetch real-time weather data.

## Features

- Display current weather conditions, including temperature, humidity, wind speed, and more.
- 5-day weather forecast with hourly details.
- Gives location of the searched city
- User-friendly interface with responsive design.
- Easy-to-use and intuitive user experience.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Abhik-Develops/weather-app.git
```

2. Create virtualenv:

```bash
virtualenv env
```

3. Navigate to the project directory:

```bash
cd weather-app
```

5. Install dependencies:

```bash
pip install -r requirements.txt 
```

5. Configuration:

Get your API key from OpenWeatherMap by creating an account.
Create a .env file in the project root and add your API key:

API_KEY=your_api_key_here

## Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Open your browser and go to http://localhost:8000/

3. Enter the city name to get the weather information.

## Screenshots

![image](https://github.com/Abhik-Develops/weather-app/assets/134844120/3ac2b74b-778f-4af2-b1dc-cce862079bd3)

![image](https://github.com/Abhik-Develops/weather-app/assets/134844120/53f7708c-c297-423b-88f4-8f4373c5d3a8)


## Technologies Used

- Django
- OpenWeatherMap API

## Contributing
If you'd like to contribute, please fork the repository and create a pull request. Feel free to open an issue for any bugs or feature requests.
