from flask import Blueprint, render_template
import requests

api = Blueprint("api", __name__)

def round_to_nearest_strike(strike, strike_diff):
    return round(strike/strike_diff)*strike_diff

def get_data(sm):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={sm}"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8','accept-encoding': 'gzip, deflate, br'}
    sess = requests.Session()
    cookies = dict()
    request = sess.get(url, headers=headers, timeout=10)
    cookies = dict(request.cookies)
    response = sess.get(url, headers=headers, timeout=10, cookies=cookies)
    if(response.status_code==401):
        cookies = dict()
        response = sess.get(url, headers=headers, timeout=10, cookies=cookies)
    if(response.status_code==200):
        return response.json()
    return {}


@api.route("/api", methods=["GET"])
def home():
    # nifty_price = nse_quote_ltp("NIFTY")
    sm = "NIFTY"
    r = get_data(sm)
    strike_diff = 50
    nearest_strike = round_to_nearest_strike(r["records"]["underlyingValue"], strike_diff)
    strike_list = list(range(nearest_strike - (15*strike_diff), nearest_strike + (15*strike_diff), strike_diff))
    data = {
        "price" : r["records"]["underlyingValue"],
        "current_exp": r["records"]["expiryDates"][0],
        "oc" : [x for x in r["filtered"]["data"] if x["expiryDate"] == r["records"]["expiryDates"][0] and x["strikePrice"] in strike_list]
    }
    return data
