import requests
import json
import hmac
import hashlib
import time

pub_key = 'your_pubkey_here'
secret_key = 'your_secretkey_here'

def sign(self):
    if type(self) is str:
	self = self.encode()
    signature = hmac.new(secret_key, msg=self, digestmod=hashlib.sha256).hexdigest()
    return signature

timestamp = int(time.time())
pub_key_str = str(pub_key)
payload = "{}.{}".format(timestamp, pub_key_str)
digest_value = sign(payload)
signature_header = "{}.{}".format(payload, digest_value)
rate_url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
rate_header = {"X-Signature": signature_header}
rate = requests.get(url=rate_url, headers=rate_header).json()
print rate
