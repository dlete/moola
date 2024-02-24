
def mlreader():
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

    #print(r.headers)
    #print(r.status_code)
    #print(r.text)

    # assert
    # https://stackoverflow.com/questions/14365027/python-post-binary-data
    return r

#r = mlreader()
#print(r.headers)
#print(r.status_code)
#print(r.text)
#print(type(r))
#print(type(r.text))
"""
>>> r.text
'{"extract": {"AMOUNT": 60.0, "INVOICEDATE": "Thu, 20 Dec 2018 00:00:00 GMT", "NAME": "Charlesland Medical Centre"}, "id": "1779e904f023e4eb_2390720", "status": "OK"}'
>>> type(r.text)
<class 'str'>
>>> json.loads(r.text)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  NameError: name 'json' is not defined
  >>> import json
  >>> json.loads(r.text)
  {'status': 'OK', 'id': '1779e904f023e4eb_2390720', 'extract': {'NAME': 'Charlesland Medical Centre', 'INVOICEDATE': 'Thu, 20 Dec 2018 00:00:00 GMT', 'AMOUNT': 60.0}}
  >>> type(json.loads(r.text))
  <class 'dict'>
  >>>


# this is print(r.headers)
{'Content-Length': '165', 'Server': 'gunicorn/19.7.1', 'Content-Type': 'text/html; charset=utf-8', 'Connection': 'close', 'Date': 'Wed, 20 Feb 2019 18:00:04 GMT'}
# this is print(r.status_code)
200

"""






def my_time():
    import datetime
    t = datetime.datetime.now()
    dt = {
        'year': t.year,
        'month': t.month,
        'day': t.day,
        'hour': t.hour,
        'minute': t.minute,
        'second': t.second,
    }
    return dt
