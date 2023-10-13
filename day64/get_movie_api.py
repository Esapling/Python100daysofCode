import requests, os

url = f"https://api.themoviedb.org/3/search/movie"
token = os.environ['MOVIE_API_TOKEN']
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
}
class GetMovie:
    def __init__(self) -> None:
        self.movie_name = ""
        self.initalize()
    def initalize(self):
        token = os.environ['MOVIE_API_TOKEN']
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
    def get_movieByName(self, name):
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
        "query":name,
        }
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {}
        
    def get_movieById(self, id):
        url = f"https://api.themoviedb.org/3/movie/{id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"error {response.status_code}")
            return {}

