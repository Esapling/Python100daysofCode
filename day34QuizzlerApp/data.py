import requests
import html 

#
# Gets the question data using an api
# overwrites some special characters and writes them on a list called question_data
#


parameters = {
    'amount': 20,
    'type': 'boolean',
}

response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()  # change the response into json format so that we can read

question_data = []

#print(data['results'])

question = data['results'][0]
#print(question)
# some special characters in the question values should be handled  
for question in data["results"]:
    question["question"] = html.unescape(question["question"])

question_data = data["results"]