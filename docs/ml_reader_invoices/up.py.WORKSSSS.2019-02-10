#https://stackoverflow.com/questions/31594769/posting-image-using-requests-on-python
import requests

url = 'http://35.232.51.61:5000/extract'
headers= {'Content-Type': 'application/json'}

from base64 import b64encode
encoding = 'utf-8'
with open('./DSC_0051.JPG', 'rb') as open_file:
    byte_content = open_file.read()

base64_bytes = b64encode(byte_content)
base64_string = base64_bytes.decode(encoding)



# https://stackoverflow.com/questions/37225035/serialize-in-json-a-base64-encoded-data
# https://github.com/openlabs/docker-wkhtmltopdf-aas/issues/9
payload = {
    'image': base64_string,
    'features': [{ "donate": "1"}]
}
#r = requests.post(url, headers=headers, data=payload)

# does not work
import json
r = requests.post(url, data=json.dumps(payload), headers=headers)



print(r.headers)
print(r.status_code)
print(r.text)

# assert
# https://stackoverflow.com/questions/14365027/python-post-binary-data
