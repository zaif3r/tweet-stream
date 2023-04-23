# tweet-stream
This is a Python GitHub repository that provides a real-time tweet stream using a WebSocket. The repository is designed to help users easily collect and process live tweets from Twitter's streaming API using a WebSocket server. The tweets are also saved in a MongoDB database.

## Configuration
- Before running the script, you will need to set up a Twitter developer account and create a new app. Once you have done this, you will need to obtain your app's Bearer Token key.
- You will also need to create a `.env` file in the root directory of the project and fill in the following variables:
  - `WEBSOCKET_PORT` is the port on which the WebSocket server will run.
  - `MONGODB_HOST`, `MONGODB_DBNAME`, `MONGODB_USERNAME`, and `MONGODB_PASSWORD are the MongoDB connection details.
  - `TWITTER_BEARER_TOKEN` is the bearer token obtained from Twitter's developer dashboard.

## Contributing
If you would like to contribute to this repository, please fork the repository and submit a pull request with your changes. We welcome contributions from anyone, and we appreciate all feedback and suggestions.
