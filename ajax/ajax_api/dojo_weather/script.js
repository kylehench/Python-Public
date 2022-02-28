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
    for (let i = 0; i < days.length; i++) {
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

function displayWeather(weatherData, unit) {
    for (let i = 0; i <= 3; i++) {
        console.log(weatherData.daily[i].temp.max);
        document.getElementById(`day-${i}-high`).innerHTML = `${convertTemp(weatherData.daily[i].temp.max, unit)}&deg;`
        document.getElementById(`day-${i}-low`).innerHTML = `${convertTemp(weatherData.daily[i].temp.min, unit)}&deg;`
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
}

async function getWeather() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=37.338207&lon=-121.886330&appid=c861f74312a06bc4c6eeb33bf2815159");


    // We then need to convert the data into JSON format.
    var weatherData = await response.json();
    // var weatherData = getWeatherData();
    displayWeather(weatherData, 'F')
    // document.getElementById("text").innerHTML = `${weatherData.name} has ${weatherData.followers} followers.`
    return;
}


// c861f74312a06bc4c6eeb33bf2815159

// http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID={c861f74312a06bc4c6eeb33bf2815159}
// // Make sure to put your unique API key in the URL (taking out the brackets).
// // &APPID={INSERTAPIKEY} will need to be at the end of each URL you access below and in the assignment.

