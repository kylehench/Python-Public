function acceptCookies() {
    document.querySelector("#cookie-container").remove();
}
var celsius = true;
var tempsC = [[24,18],[27,19],[21,16],[26,21]];
var tempsF = [[75,65],[80,66],[69,61],[78,70]];
var els = document.getElementsByClassName("day");

// updateWeekdays days
function updateWeekdays() {
    let days = document.getElementsByClassName("week")[0].children;
    let moment = new Date();
    for (i in days) {
        days[i].firstElementChild.innerHTML = new Intl.DateTimeFormat("en-us", { weekday: "long" }).format(moment);
        moment.setDate(moment.getDate() + 1);
    }
}
updateWeekdays();

function tempConvert(value) {
    temps = [];
    if (value.slice(-1) === "F") {
        temps = tempsF;
    }
    else {
        temps = tempsC;
    }
    for (i=0; i < els.length; i++) {
        els[i].querySelector(".high").innerHTML = temps[i][0] + "&deg;";
        els[i].querySelector(".low").innerHTML = temps[i][1] + "&deg;";
        // console.log(els[i].querySelector(".high").innerText);
    }
}

function convertTemp(tempInKelvin, outputUnit) {
    temp = tempInKelvin-273.15;
    if (outputUnit=='C') {
        return Math.round(temp*10)/10;
    }
    // output temp in F
    return Math.round(temp*1.8+32);
}

async function getWeather() {
    // console.log('hi there')
    // // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    // var response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=37.338207&lon=-121.886330&appid=c861f74312a06bc4c6eeb33bf2815159");


    // // We then need to convert the data into JSON format.
    // var weatherData = await response.json();
    weatherData = getWeatherData();

    for (let i = 0; i <= 4; i++) {
        console.log(weatherData.daily[i].temp.max);
        document.getElementById(`day-${i}-high`).innerHTML = `${convertTemp(weatherData.daily[i].temp.max, 'C')}&deg;`
        document.getElementById(`day-${i}-low`).innerHTML = `${convertTemp(weatherData.daily[i].temp.min, 'F')}&deg;`
        condition = weatherData.daily[i].weather[0].id
        if (condition < 700) {
            img_src = "assets/some_rain.png"
        } else if (condition < 800 || condition > 801) {
            img_src = "assets/some_clouds.png"
        } else {
            img_src = "assets/some_sun.png"
        }
        document.getElementById(`day-${i}-img`).src = img_src
        // https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    }
    // document.getElementById("text").innerHTML = `${weatherData.name} has ${weatherData.followers} followers.`
    return;
}


// c861f74312a06bc4c6eeb33bf2815159

// http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID={c861f74312a06bc4c6eeb33bf2815159}
// // Make sure to put your unique API key in the URL (taking out the brackets).
// // &APPID={INSERTAPIKEY} will need to be at the end of each URL you access below and in the assignment.


function getWeatherData() {
    weatherData = {
        "lat": 37.3382,
        "lon": -121.8863,
        "timezone": "America/Los_Angeles",
        "timezone_offset": -28800,
        "current": {
            "dt": 1645753615,
            "sunrise": 1645713931,
            "sunset": 1645754178,
            "temp": 283.87,
            "feels_like": 282.64,
            "pressure": 1025,
            "humidity": 63,
            "dew_point": 277.12,
            "uvi": 0,
            "clouds": 75,
            "visibility": 10000,
            "wind_speed": 6.69,
            "wind_deg": 330,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ]
        },
        "minutely": [
            {
                "dt": 1645753620,
                "precipitation": 0
            },
            {
                "dt": 1645753680,
                "precipitation": 0
            },
            {
                "dt": 1645753740,
                "precipitation": 0
            },
            {
                "dt": 1645753800,
                "precipitation": 0
            },
            {
                "dt": 1645753860,
                "precipitation": 0
            },
            {
                "dt": 1645753920,
                "precipitation": 0
            },
            {
                "dt": 1645753980,
                "precipitation": 0
            },
            {
                "dt": 1645754040,
                "precipitation": 0
            },
            {
                "dt": 1645754100,
                "precipitation": 0
            },
            {
                "dt": 1645754160,
                "precipitation": 0
            },
            {
                "dt": 1645754220,
                "precipitation": 0
            },
            {
                "dt": 1645754280,
                "precipitation": 0
            },
            {
                "dt": 1645754340,
                "precipitation": 0
            },
            {
                "dt": 1645754400,
                "precipitation": 0
            },
            {
                "dt": 1645754460,
                "precipitation": 0
            },
            {
                "dt": 1645754520,
                "precipitation": 0
            },
            {
                "dt": 1645754580,
                "precipitation": 0
            },
            {
                "dt": 1645754640,
                "precipitation": 0
            },
            {
                "dt": 1645754700,
                "precipitation": 0
            },
            {
                "dt": 1645754760,
                "precipitation": 0
            },
            {
                "dt": 1645754820,
                "precipitation": 0
            },
            {
                "dt": 1645754880,
                "precipitation": 0
            },
            {
                "dt": 1645754940,
                "precipitation": 0
            },
            {
                "dt": 1645755000,
                "precipitation": 0
            },
            {
                "dt": 1645755060,
                "precipitation": 0
            },
            {
                "dt": 1645755120,
                "precipitation": 0
            },
            {
                "dt": 1645755180,
                "precipitation": 0
            },
            {
                "dt": 1645755240,
                "precipitation": 0
            },
            {
                "dt": 1645755300,
                "precipitation": 0
            },
            {
                "dt": 1645755360,
                "precipitation": 0
            },
            {
                "dt": 1645755420,
                "precipitation": 0
            },
            {
                "dt": 1645755480,
                "precipitation": 0
            },
            {
                "dt": 1645755540,
                "precipitation": 0
            },
            {
                "dt": 1645755600,
                "precipitation": 0
            },
            {
                "dt": 1645755660,
                "precipitation": 0
            },
            {
                "dt": 1645755720,
                "precipitation": 0
            },
            {
                "dt": 1645755780,
                "precipitation": 0
            },
            {
                "dt": 1645755840,
                "precipitation": 0
            },
            {
                "dt": 1645755900,
                "precipitation": 0
            },
            {
                "dt": 1645755960,
                "precipitation": 0
            },
            {
                "dt": 1645756020,
                "precipitation": 0
            },
            {
                "dt": 1645756080,
                "precipitation": 0
            },
            {
                "dt": 1645756140,
                "precipitation": 0
            },
            {
                "dt": 1645756200,
                "precipitation": 0
            },
            {
                "dt": 1645756260,
                "precipitation": 0
            },
            {
                "dt": 1645756320,
                "precipitation": 0
            },
            {
                "dt": 1645756380,
                "precipitation": 0
            },
            {
                "dt": 1645756440,
                "precipitation": 0
            },
            {
                "dt": 1645756500,
                "precipitation": 0
            },
            {
                "dt": 1645756560,
                "precipitation": 0
            },
            {
                "dt": 1645756620,
                "precipitation": 0
            },
            {
                "dt": 1645756680,
                "precipitation": 0
            },
            {
                "dt": 1645756740,
                "precipitation": 0
            },
            {
                "dt": 1645756800,
                "precipitation": 0
            },
            {
                "dt": 1645756860,
                "precipitation": 0
            },
            {
                "dt": 1645756920,
                "precipitation": 0
            },
            {
                "dt": 1645756980,
                "precipitation": 0
            },
            {
                "dt": 1645757040,
                "precipitation": 0
            },
            {
                "dt": 1645757100,
                "precipitation": 0
            },
            {
                "dt": 1645757160,
                "precipitation": 0
            },
            {
                "dt": 1645757220,
                "precipitation": 0
            }
        ],
        "hourly": [
            {
                "dt": 1645750800,
                "temp": 284.11,
                "feels_like": 282.8,
                "pressure": 1025,
                "humidity": 59,
                "dew_point": 276.42,
                "uvi": 0.16,
                "clouds": 61,
                "visibility": 10000,
                "wind_speed": 3.04,
                "wind_deg": 321,
                "wind_gust": 3.97,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645754400,
                "temp": 283.87,
                "feels_like": 282.64,
                "pressure": 1025,
                "humidity": 63,
                "dew_point": 277.12,
                "uvi": 0,
                "clouds": 75,
                "visibility": 10000,
                "wind_speed": 2.27,
                "wind_deg": 326,
                "wind_gust": 3.56,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645758000,
                "temp": 283.16,
                "feels_like": 281.89,
                "pressure": 1025,
                "humidity": 64,
                "dew_point": 276.67,
                "uvi": 0,
                "clouds": 63,
                "visibility": 10000,
                "wind_speed": 1.42,
                "wind_deg": 337,
                "wind_gust": 2.57,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645761600,
                "temp": 282.17,
                "feels_like": 282.17,
                "pressure": 1025,
                "humidity": 65,
                "dew_point": 275.95,
                "uvi": 0,
                "clouds": 55,
                "visibility": 10000,
                "wind_speed": 0.61,
                "wind_deg": 342,
                "wind_gust": 1.66,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645765200,
                "temp": 281.32,
                "feels_like": 281.32,
                "pressure": 1025,
                "humidity": 66,
                "dew_point": 275.36,
                "uvi": 0,
                "clouds": 53,
                "visibility": 10000,
                "wind_speed": 0.2,
                "wind_deg": 25,
                "wind_gust": 0.99,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645768800,
                "temp": 280.27,
                "feels_like": 280.27,
                "pressure": 1026,
                "humidity": 68,
                "dew_point": 274.77,
                "uvi": 0,
                "clouds": 54,
                "visibility": 10000,
                "wind_speed": 0.48,
                "wind_deg": 331,
                "wind_gust": 1.13,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645772400,
                "temp": 278.78,
                "feels_like": 278.78,
                "pressure": 1026,
                "humidity": 73,
                "dew_point": 273.03,
                "uvi": 0,
                "clouds": 99,
                "visibility": 10000,
                "wind_speed": 0.73,
                "wind_deg": 351,
                "wind_gust": 1.03,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645776000,
                "temp": 278.12,
                "feels_like": 278.12,
                "pressure": 1026,
                "humidity": 77,
                "dew_point": 273.25,
                "uvi": 0,
                "clouds": 55,
                "visibility": 10000,
                "wind_speed": 0.87,
                "wind_deg": 353,
                "wind_gust": 1.05,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645779600,
                "temp": 277.8,
                "feels_like": 277.8,
                "pressure": 1026,
                "humidity": 80,
                "dew_point": 273.33,
                "uvi": 0,
                "clouds": 38,
                "visibility": 10000,
                "wind_speed": 0.62,
                "wind_deg": 35,
                "wind_gust": 0.82,
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645783200,
                "temp": 277.57,
                "feels_like": 277.57,
                "pressure": 1026,
                "humidity": 80,
                "dew_point": 273.06,
                "uvi": 0,
                "clouds": 28,
                "visibility": 10000,
                "wind_speed": 0.38,
                "wind_deg": 15,
                "wind_gust": 0.82,
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645786800,
                "temp": 277.36,
                "feels_like": 277.36,
                "pressure": 1026,
                "humidity": 78,
                "dew_point": 272.61,
                "uvi": 0,
                "clouds": 23,
                "visibility": 10000,
                "wind_speed": 0.49,
                "wind_deg": 50,
                "wind_gust": 0.73,
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645790400,
                "temp": 277.2,
                "feels_like": 277.2,
                "pressure": 1025,
                "humidity": 77,
                "dew_point": 272.13,
                "uvi": 0,
                "clouds": 19,
                "visibility": 10000,
                "wind_speed": 0.75,
                "wind_deg": 68,
                "wind_gust": 0.86,
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645794000,
                "temp": 277.09,
                "feels_like": 277.09,
                "pressure": 1025,
                "humidity": 74,
                "dew_point": 271.54,
                "uvi": 0,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 1.06,
                "wind_deg": 90,
                "wind_gust": 1.1,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645797600,
                "temp": 276.95,
                "feels_like": 276.95,
                "pressure": 1025,
                "humidity": 71,
                "dew_point": 270.81,
                "uvi": 0,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 0.97,
                "wind_deg": 93,
                "wind_gust": 1.01,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645801200,
                "temp": 277,
                "feels_like": 277,
                "pressure": 1026,
                "humidity": 68,
                "dew_point": 270.31,
                "uvi": 0,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 0.6,
                "wind_deg": 66,
                "wind_gust": 0.81,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645804800,
                "temp": 279.88,
                "feels_like": 279.88,
                "pressure": 1026,
                "humidity": 58,
                "dew_point": 270.74,
                "uvi": 0.51,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 0.63,
                "wind_deg": 59,
                "wind_gust": 0.88,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645808400,
                "temp": 282.92,
                "feels_like": 282.92,
                "pressure": 1026,
                "humidity": 47,
                "dew_point": 270.73,
                "uvi": 1.4,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 0.65,
                "wind_deg": 355,
                "wind_gust": 0.82,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645812000,
                "temp": 285.09,
                "feels_like": 283.36,
                "pressure": 1026,
                "humidity": 39,
                "dew_point": 270.58,
                "uvi": 2.57,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 0.92,
                "wind_deg": 352,
                "wind_gust": 1,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645815600,
                "temp": 286.74,
                "feels_like": 285.07,
                "pressure": 1026,
                "humidity": 35,
                "dew_point": 270.35,
                "uvi": 3.63,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 1.46,
                "wind_deg": 322,
                "wind_gust": 1.34,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645819200,
                "temp": 287.82,
                "feels_like": 286.18,
                "pressure": 1025,
                "humidity": 32,
                "dew_point": 270.44,
                "uvi": 4.13,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 1.68,
                "wind_deg": 334,
                "wind_gust": 1.67,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645822800,
                "temp": 288.54,
                "feels_like": 286.94,
                "pressure": 1024,
                "humidity": 31,
                "dew_point": 270.52,
                "uvi": 3.84,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 1.85,
                "wind_deg": 341,
                "wind_gust": 1.85,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645826400,
                "temp": 288.97,
                "feels_like": 287.39,
                "pressure": 1024,
                "humidity": 30,
                "dew_point": 270.57,
                "uvi": 2.88,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 2.08,
                "wind_deg": 338,
                "wind_gust": 2.02,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645830000,
                "temp": 288.97,
                "feels_like": 287.42,
                "pressure": 1023,
                "humidity": 31,
                "dew_point": 270.67,
                "uvi": 1.7,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 2.05,
                "wind_deg": 346,
                "wind_gust": 2.08,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645833600,
                "temp": 288.6,
                "feels_like": 287.04,
                "pressure": 1023,
                "humidity": 32,
                "dew_point": 270.89,
                "uvi": 0.73,
                "clouds": 1,
                "visibility": 10000,
                "wind_speed": 2.16,
                "wind_deg": 347,
                "wind_gust": 2.37,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645837200,
                "temp": 287.27,
                "feels_like": 285.76,
                "pressure": 1023,
                "humidity": 39,
                "dew_point": 272.5,
                "uvi": 0.17,
                "clouds": 12,
                "visibility": 10000,
                "wind_speed": 2.06,
                "wind_deg": 343,
                "wind_gust": 3.38,
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645840800,
                "temp": 283.37,
                "feels_like": 281.75,
                "pressure": 1024,
                "humidity": 50,
                "dew_point": 272.16,
                "uvi": 0,
                "clouds": 6,
                "visibility": 10000,
                "wind_speed": 1.57,
                "wind_deg": 341,
                "wind_gust": 2.44,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645844400,
                "temp": 281.91,
                "feels_like": 281.91,
                "pressure": 1025,
                "humidity": 55,
                "dew_point": 272.16,
                "uvi": 0,
                "clouds": 4,
                "visibility": 10000,
                "wind_speed": 1.13,
                "wind_deg": 347,
                "wind_gust": 2.25,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645848000,
                "temp": 281.08,
                "feels_like": 281.08,
                "pressure": 1025,
                "humidity": 58,
                "dew_point": 272.07,
                "uvi": 0,
                "clouds": 3,
                "visibility": 10000,
                "wind_speed": 0.53,
                "wind_deg": 32,
                "wind_gust": 1.19,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645851600,
                "temp": 280.61,
                "feels_like": 280.61,
                "pressure": 1026,
                "humidity": 59,
                "dew_point": 271.87,
                "uvi": 0,
                "clouds": 2,
                "visibility": 10000,
                "wind_speed": 0.72,
                "wind_deg": 63,
                "wind_gust": 1.05,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645855200,
                "temp": 280.19,
                "feels_like": 280.19,
                "pressure": 1026,
                "humidity": 60,
                "dew_point": 271.7,
                "uvi": 0,
                "clouds": 3,
                "visibility": 10000,
                "wind_speed": 0.89,
                "wind_deg": 79,
                "wind_gust": 0.96,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645858800,
                "temp": 279.82,
                "feels_like": 279.82,
                "pressure": 1026,
                "humidity": 60,
                "dew_point": 271.46,
                "uvi": 0,
                "clouds": 4,
                "visibility": 10000,
                "wind_speed": 0.9,
                "wind_deg": 96,
                "wind_gust": 1.03,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645862400,
                "temp": 279.73,
                "feels_like": 279.73,
                "pressure": 1026,
                "humidity": 60,
                "dew_point": 271.2,
                "uvi": 0,
                "clouds": 51,
                "visibility": 10000,
                "wind_speed": 0.9,
                "wind_deg": 88,
                "wind_gust": 1.01,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645866000,
                "temp": 279.67,
                "feels_like": 279.67,
                "pressure": 1026,
                "humidity": 58,
                "dew_point": 270.81,
                "uvi": 0,
                "clouds": 67,
                "visibility": 10000,
                "wind_speed": 1.02,
                "wind_deg": 90,
                "wind_gust": 1.04,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645869600,
                "temp": 279.37,
                "feels_like": 279.37,
                "pressure": 1026,
                "humidity": 58,
                "dew_point": 270.37,
                "uvi": 0,
                "clouds": 68,
                "visibility": 10000,
                "wind_speed": 0.88,
                "wind_deg": 104,
                "wind_gust": 1.05,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645873200,
                "temp": 279.47,
                "feels_like": 279.47,
                "pressure": 1026,
                "humidity": 55,
                "dew_point": 269.91,
                "uvi": 0,
                "clouds": 74,
                "visibility": 10000,
                "wind_speed": 1.04,
                "wind_deg": 94,
                "wind_gust": 1.01,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645876800,
                "temp": 279.38,
                "feels_like": 279.38,
                "pressure": 1026,
                "humidity": 54,
                "dew_point": 269.46,
                "uvi": 0,
                "clouds": 78,
                "visibility": 10000,
                "wind_speed": 0.88,
                "wind_deg": 85,
                "wind_gust": 0.99,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645880400,
                "temp": 279.31,
                "feels_like": 278.52,
                "pressure": 1026,
                "humidity": 52,
                "dew_point": 268.97,
                "uvi": 0,
                "clouds": 100,
                "visibility": 10000,
                "wind_speed": 1.42,
                "wind_deg": 96,
                "wind_gust": 1.36,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645884000,
                "temp": 278.84,
                "feels_like": 278.84,
                "pressure": 1026,
                "humidity": 53,
                "dew_point": 268.61,
                "uvi": 0,
                "clouds": 93,
                "visibility": 10000,
                "wind_speed": 0.87,
                "wind_deg": 101,
                "wind_gust": 1.09,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645887600,
                "temp": 278.83,
                "feels_like": 278.83,
                "pressure": 1027,
                "humidity": 52,
                "dew_point": 268.51,
                "uvi": 0,
                "clouds": 64,
                "visibility": 10000,
                "wind_speed": 1.27,
                "wind_deg": 92,
                "wind_gust": 1.17,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645891200,
                "temp": 281.77,
                "feels_like": 281.77,
                "pressure": 1027,
                "humidity": 46,
                "dew_point": 269.8,
                "uvi": 0.52,
                "clouds": 66,
                "visibility": 10000,
                "wind_speed": 0.72,
                "wind_deg": 78,
                "wind_gust": 1.04,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645894800,
                "temp": 285.22,
                "feels_like": 283.47,
                "pressure": 1027,
                "humidity": 38,
                "dew_point": 270.06,
                "uvi": 1.41,
                "clouds": 59,
                "visibility": 10000,
                "wind_speed": 0.51,
                "wind_deg": 71,
                "wind_gust": 1.04,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645898400,
                "temp": 287.52,
                "feels_like": 285.87,
                "pressure": 1027,
                "humidity": 33,
                "dew_point": 270.36,
                "uvi": 2.58,
                "clouds": 66,
                "visibility": 10000,
                "wind_speed": 0.4,
                "wind_deg": 75,
                "wind_gust": 1.42,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645902000,
                "temp": 289.1,
                "feels_like": 287.53,
                "pressure": 1027,
                "humidity": 30,
                "dew_point": 270.29,
                "uvi": 3.6,
                "clouds": 100,
                "visibility": 10000,
                "wind_speed": 0.45,
                "wind_deg": 0,
                "wind_gust": 1.59,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645905600,
                "temp": 290.47,
                "feels_like": 288.96,
                "pressure": 1026,
                "humidity": 27,
                "dew_point": 270.46,
                "uvi": 4.08,
                "clouds": 98,
                "visibility": 10000,
                "wind_speed": 0.38,
                "wind_deg": 317,
                "wind_gust": 1.53,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645909200,
                "temp": 291.19,
                "feels_like": 289.75,
                "pressure": 1026,
                "humidity": 27,
                "dew_point": 270.75,
                "uvi": 3.8,
                "clouds": 98,
                "visibility": 10000,
                "wind_speed": 0.83,
                "wind_deg": 313,
                "wind_gust": 1.47,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645912800,
                "temp": 291.23,
                "feels_like": 289.82,
                "pressure": 1025,
                "humidity": 28,
                "dew_point": 271.25,
                "uvi": 2.83,
                "clouds": 99,
                "visibility": 10000,
                "wind_speed": 1.02,
                "wind_deg": 334,
                "wind_gust": 1.3,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645916400,
                "temp": 291.29,
                "feels_like": 289.92,
                "pressure": 1025,
                "humidity": 29,
                "dew_point": 271.8,
                "uvi": 1.67,
                "clouds": 95,
                "visibility": 10000,
                "wind_speed": 1.66,
                "wind_deg": 324,
                "wind_gust": 1.45,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            },
            {
                "dt": 1645920000,
                "temp": 290.5,
                "feels_like": 289.13,
                "pressure": 1025,
                "humidity": 32,
                "dew_point": 272.5,
                "uvi": 0.72,
                "clouds": 92,
                "visibility": 10000,
                "wind_speed": 2.39,
                "wind_deg": 320,
                "wind_gust": 1.77,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0
            }
        ],
        "daily": [
            {
                "dt": 1645732800,
                "sunrise": 1645713931,
                "sunset": 1645754178,
                "moonrise": 1645696200,
                "moonset": 1645731060,
                "moon_phase": 0.78,
                "temp": {
                    "day": 287.09,
                    "min": 276.24,
                    "max": 287.56,
                    "night": 278.78,
                    "eve": 283.87,
                    "morn": 276.24
                },
                "feels_like": {
                    "day": 285.24,
                    "night": 278.78,
                    "eve": 282.64,
                    "morn": 276.24
                },
                "pressure": 1026,
                "humidity": 27,
                "dew_point": 267.51,
                "wind_speed": 3.59,
                "wind_deg": 320,
                "wind_gust": 3.97,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": 0,
                "pop": 0,
                "uvi": 4.06
            },
            {
                "dt": 1645819200,
                "sunrise": 1645800252,
                "sunset": 1645840638,
                "moonrise": 1645786800,
                "moonset": 1645820700,
                "moon_phase": 0.82,
                "temp": {
                    "day": 287.82,
                    "min": 276.95,
                    "max": 288.97,
                    "night": 279.82,
                    "eve": 283.37,
                    "morn": 276.95
                },
                "feels_like": {
                    "day": 286.18,
                    "night": 279.82,
                    "eve": 281.75,
                    "morn": 276.95
                },
                "pressure": 1025,
                "humidity": 32,
                "dew_point": 270.44,
                "wind_speed": 2.16,
                "wind_deg": 347,
                "wind_gust": 3.38,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": 0,
                "pop": 0,
                "uvi": 4.13
            },
            {
                "dt": 1645905600,
                "sunrise": 1645886572,
                "sunset": 1645927099,
                "moonrise": 1645877100,
                "moonset": 1645910940,
                "moon_phase": 0.86,
                "temp": {
                    "day": 290.47,
                    "min": 278.83,
                    "max": 291.29,
                    "night": 282.89,
                    "eve": 284.95,
                    "morn": 278.84
                },
                "feels_like": {
                    "day": 288.96,
                    "night": 282.89,
                    "eve": 283.54,
                    "morn": 278.84
                },
                "pressure": 1026,
                "humidity": 27,
                "dew_point": 270.46,
                "wind_speed": 2.42,
                "wind_deg": 327,
                "wind_gust": 3.69,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": 98,
                "pop": 0,
                "uvi": 4.08
            },
            {
                "dt": 1645992000,
                "sunrise": 1645972891,
                "sunset": 1646013558,
                "moonrise": 1645966860,
                "moonset": 1646001540,
                "moon_phase": 0.89,
                "temp": {
                    "day": 290.79,
                    "min": 282.41,
                    "max": 291.75,
                    "night": 284.15,
                    "eve": 285.57,
                    "morn": 282.79
                },
                "feels_like": {
                    "day": 289.5,
                    "night": 282.77,
                    "eve": 284.23,
                    "morn": 282.79
                },
                "pressure": 1027,
                "humidity": 34,
                "dew_point": 273.92,
                "wind_speed": 2.44,
                "wind_deg": 332,
                "wind_gust": 3.5,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": 100,
                "pop": 0,
                "uvi": 3.03
            },
            {
                "dt": 1646078400,
                "sunrise": 1646059209,
                "sunset": 1646100018,
                "moonrise": 1646056080,
                "moonset": 1646092320,
                "moon_phase": 0.93,
                "temp": {
                    "day": 294.2,
                    "min": 282.3,
                    "max": 294.2,
                    "night": 285.01,
                    "eve": 286.2,
                    "morn": 282.3
                },
                "feels_like": {
                    "day": 293.4,
                    "night": 284.52,
                    "eve": 285.65,
                    "morn": 282.3
                },
                "pressure": 1022,
                "humidity": 40,
                "dew_point": 279.1,
                "wind_speed": 4.01,
                "wind_deg": 313,
                "wind_gust": 5.02,
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03d"
                    }
                ],
                "clouds": 25,
                "pop": 0,
                "uvi": 4.82
            },
            {
                "dt": 1646164800,
                "sunrise": 1646145527,
                "sunset": 1646186477,
                "moonrise": 1646144820,
                "moonset": 1646183100,
                "moon_phase": 0.97,
                "temp": {
                    "day": 293.31,
                    "min": 284.18,
                    "max": 293.55,
                    "night": 285.71,
                    "eve": 287.04,
                    "morn": 284.28
                },
                "feels_like": {
                    "day": 292.61,
                    "night": 284.82,
                    "eve": 286.29,
                    "morn": 283.59
                },
                "pressure": 1021,
                "humidity": 47,
                "dew_point": 280.53,
                "wind_speed": 3.24,
                "wind_deg": 320,
                "wind_gust": 4.43,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": 100,
                "pop": 0,
                "uvi": 5
            },
            {
                "dt": 1646251200,
                "sunrise": 1646231843,
                "sunset": 1646272935,
                "moonrise": 1646233200,
                "moonset": 1646273640,
                "moon_phase": 0,
                "temp": {
                    "day": 293.14,
                    "min": 283.51,
                    "max": 293.14,
                    "night": 284.81,
                    "eve": 286.03,
                    "morn": 283.51
                },
                "feels_like": {
                    "day": 292.45,
                    "night": 284.33,
                    "eve": 285.46,
                    "morn": 282.4
                },
                "pressure": 1019,
                "humidity": 48,
                "dew_point": 280.83,
                "wind_speed": 3.23,
                "wind_deg": 322,
                "wind_gust": 4.49,
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": 100,
                "pop": 0,
                "uvi": 5
            },
            {
                "dt": 1646337600,
                "sunrise": 1646318159,
                "sunset": 1646359394,
                "moonrise": 1646321340,
                "moonset": 1646364060,
                "moon_phase": 0.04,
                "temp": {
                    "day": 294.58,
                    "min": 283.56,
                    "max": 294.58,
                    "night": 285.46,
                    "eve": 287.37,
                    "morn": 283.56
                },
                "feels_like": {
                    "day": 293.93,
                    "night": 284.44,
                    "eve": 286.65,
                    "morn": 283.16
                },
                "pressure": 1018,
                "humidity": 44,
                "dew_point": 280.86,
                "wind_speed": 3.11,
                "wind_deg": 331,
                "wind_gust": 3.41,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": 0,
                "pop": 0,
                "uvi": 5
            }
        ],
        "alerts": [
            {
                "sender_name": "NWS Monterey (The San Francisco area)",
                "event": "Freeze Warning",
                "start": 1645738680,
                "end": 1645808400,
                "description": "...FREEZE WARNING REMAINS IN EFFECT UNTIL 9 AM PST FRIDAY...\n* WHAT...Widespread sub-freezing temperatures are expected.\n* WHERE...North Bay Interior Valleys, North Bay Mountains,\nSouthern Salinas Valley/Arroyo Seco and Lake San Antonio,\nMountains of San Benito County and Interior Monterey County\nIncluding Pinnacles National Park, Northern Salinas\nValley/Hollister Valley and Carmel Valley, and Santa Clara\nValley.\n* WHEN...Overnight and early morning hours through 9 AM PST\nFriday.\n* IMPACTS...Frost and freeze conditions will kill crops, other\nsensitive vegetation and possibly damage unprotected outdoor\nplumbing.",
                "tags": [
                    "Extreme temperature value"
                ]
            }
        ]
    }
    return weatherData;
}