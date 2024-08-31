# Meta_Naman_ChatBot
Meta_Naman_ChatBot is a Telegram bot that provides real-time currency conversion and weather updates while engaging in natural conversations. The bot leverages DialogFlow for natural language processing, ngrok for local development testing, and integrates with currency converter and weather teller APIs for its functionalities.

The Telegram username for my bot is @meta_naman_bot. This will be the handle users can search for and interact with on Telegram.

Key Components

DialogFlow Integration:

DialogFlow is used to handle natural language understanding. It allows the bot to interpret user inputs and respond appropriately.

Configuration and interaction details with DialogFlow are managed in config.py and handled in handlers.py.

Ngrok:

ngrok is used to expose the local development server to the internet. It provides a secure tunnel to your local environment, allowing DialogFlow to communicate with your bot during development.

Instructions for setting up ngrok are included in the README.md.

Currency Converter API:

The bot uses a currency converter API to provide real-time currency exchange rates. Integration details are in utils.py, where API requests are made, and responses are processed.

Weather Teller API:

The weather teller API is used to fetch weather information for any location and date. This functionality is implemented in utils.py, where API requests are sent and results are formatted.

