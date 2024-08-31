from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    intent = data['queryResult']['intent']['displayName']

    if intent == "weather_predictor":
        city = data['queryResult']['parameters']['geo-city']
        country = data['queryResult']['parameters']['geo-country']
        date = data['queryResult']['parameters']['date-time'][:10]  # Extract only the date part

        weather_info = fetch_weather(city, country, date)

        if weather_info:
            response = {
                'fulfillmentText': "The weather in {}, {} on {} is: {}".format(city, country, date, weather_info)
            }
        else:
            response = {
                'fulfillmentText': "Could not retrieve weather information. Please try again."
            }

    elif intent == "currency-convertor":
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        cf = fetch_conversion_factor(source_currency, target_currency)
        if cf is not None:
            final_amount = amount * cf
            final_amount = round(final_amount, 2)
            response = {
                'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
            }
        else:
            response = {
                'fulfillmentText': "Conversion failed. Please check the currency codes and try again."
            }

    return jsonify(response)

def fetch_weather(city, country, date):
    api_key = "9699dd33b5a24603ae755731243108"
    location = f"{city},{country}"
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&dt={date}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Extract the weather information for the specified date
        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast_data = data['forecast']['forecastday'][0]['day']
            avg_temp_c = forecast_data['avgtemp_c']
            condition = forecast_data['condition']['text']
            return f"{avg_temp_c}°C with {condition}"
        else:
            print("Weather information not found in the API response.")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError:
        print("Weather information not found in the API response.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def fetch_conversion_factor(source, target):
    url = f"https://v6.exchangerate-api.com/v6/25e1a1ccebe33f1a3956bd3d/pair/{source}/{target}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Extract the conversion rate from the response
        if 'conversion_rate' in data:
            return data['conversion_rate']
        else:
            print("Conversion rate not found in the API response.")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError:
        print("Conversion rate not found in the API response.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True)
