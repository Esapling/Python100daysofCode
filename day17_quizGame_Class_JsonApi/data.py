import requests
import html  # to format json

# for more questions
# go to Trivia api(https://opentdb.com/api_config.php) and choose best options
# for you then generate and copy the url here
# pl. select True/False questions for this project

url = "https://opentdb.com/api.php?amount=25&type=boolean"
response = requests.get(url)
data = response.json()  # change the response into json format so that we can read

# print(data) uncomment this line to see the format of json data

question_data = []
# to format some special characters or strings in json format, use html.unescape
# notice these all special strings are only in questions value
for question in data["results"]:
    question["question"] = html.unescape(question["question"])

question_data = data["results"]
