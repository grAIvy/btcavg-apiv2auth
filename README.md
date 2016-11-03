# btcavg-apiv2auth
<pre>
Sample API authentication for BitcoinAverage's APIv2 in Python

BitcoinAverage began requiring API keys for all requests but could not find example python implementation in documentation
This script gives you a working python template for making authenticated API requests from BitcoinAverage's APIv2

Replace pub_key and secret_key with the api keys generated from your bitcoinaverage.com account

Adjust currency ticker with rate_url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/<b>BTCUSD</b>'

Make specific JSON requests with requests.get(url=rate_url, headers=rate_header).json()<b>['last']</b>

To run:
virtualenv venv --no-site-packages
source venv/bin/activate
pip install requests
python btcavg-apiv2auth.py

Alternatively without virtualenv:
apt-get install python-requests
python btcavg-apiv2auth.py

Keywords: BitcoinAverage, API, APIv2, python, authentication, bitcoinaverage.com
</pre>
