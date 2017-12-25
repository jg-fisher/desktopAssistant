# Desktop Assistant
Siri like desktop assistant written in Python which uses google's speech-to-text library to process voice input.

* Install the dependencies in a virtual environment (using conda or virtualenv) to avoid any issues. Use either pip2 or pip3 for python2 and python3 respectively.

If you are a linux user install the [say](https://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line) command using
```
sudo apt-get install gnustep-gui-runtime
```

```bash
pip2 install -r requirements.txt
pip3 install -r requirements.txt
```

* Usage

```bash
python desktopAssistant.py
````


Supported commands :
* Open reddit subreddit : Opens the subreddit in default browser.
* Open website xyz.com : self-explanatory
* Send email/email : Follow up questions such as recipient name, content will be asked in order.
* Tell a joke/another joke : Says a random dad joke.
* Current weather in {cityname} : Tells you the current condition and temperture
* weather forecast in {cityname} : Tells you the condition, highest and lowest temperture of the next two days
* What's up
