## LiveSentimentAnalyser
A live sentiment analyser about some keywords using live tweets from [twitter](https://twitter.com).

## Installation
1. Ensure that pip is installed and upgrade it. Pip should already be available if you are using Python 3 >= 3.4 downloaded from python.org. For further installation instructions check [this](https://pip.pypa.io/en/stable/installing/).
2. If you plan on using a virtual environment, ensure virtualenv (Python 2) or venv (Python 3) is installed. Create a virtual environment and activate it. Detailed instructions [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
3. After cloning the repo, install the required packages using pip in the terminal:
```
python3 -m pip install -r requirements.txt
```
4. Create a [developer account at twitter](https://developer.twitter.com) and create an app.
5. Then create an app and generate the access token
6. Copy consumer key, consumer secret key, access token , access secret token to
```
ckey=""
csecret=""
atoken=""
asecret=""
```
6. in [twitter_stream.py](https://github.com/naman-32/LiveSentimentAnalyser/blob/master/twitter_stream.py)
7. This will take time about an hour depending on the processor. 
```
python3 run_once_script.py
```
8. Done! Great for testing run test.py file and see the output.

## Using SentimentAnalyser
1. Clean the [output_from_twitter](https://github.com/naman-32/LiveSentimentAnalyser/blob/master/output_from_twitter) file each time sentiment analyser is run.
2. Change keyword to track  by replacing desired keyword with "awesome" in last line of in [twitter_stream.py](https://github.com/naman-32/LiveSentimentAnalyser/blob/master/twitter_stream.py) shown below.
```
twitterStream.filter(track=["awesome"])
```
3. Open two terminals with virtual environment activated.Run these two commands in separate terminals.
```
python3 twitter_stream.py
python3 plotting_live_data.py
```
