import requests # imports the module necessary for API
import json
# Below is the constants
method= 'POST'
url= 'https://motivational-quotes1.p.rapidapi.com/motivation'
headers = {
    'content-type': 'application/json',
    'X-RapidAPI-Key': '6615470177msh2eb9d9776c82332p163317jsn65585d1a22d9',
    'X-RapidAPI-Host': 'motivational-quotes1.p.rapidapi.com'
}
data = '{"key1":"value","key2":"value"}'
responses={}
for i in range(1):
    response = requests.request(method, url, headers=headers, data=data)
    print(response.text)
    text=response.text
    responses[text]=text
    # End Rapid API Code
responsesJson = json.dumps(responses)
print(responsesJson)