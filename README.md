# Bitly url shorterer
This program convert usual URL to bitly short URL. You can learn more about `bitly` at [bitly.com](https://bitly.com/).
Also if you already have a short URL from bitlink, you can see how many clicks have done on it.

## How to install
### Get your own token
Before using you should get your own token.
- Log in at the [bitly.com](https://bitly.com/a/sign_in).
- Follow instructions to get a token.

### Create environment variables
Create file `.env` in a root directory. Save the token there as value of `BITLY_GENERIC_ACCESS_TOKEN`.
```
BITLY_GENERIC_ACCESS_TOKEN = place_your_token_here
```

### Install requirements
Python3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## How to start
Start project by using `python` (or `python3`):
```
python main.py link
```
where *link* is URL you want to convert the short link to or the existing bitlink that you want to see the number of clicks on.

For help type
```
python main.py -h
```

## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).