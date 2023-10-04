from flask import Flask, render_template
from flask_compress import Compress
import requests


app = Flask(__name__)

response = requests.get('https://api.npoint.io/ec6d722c374ad5cec3fa')
post_data = response.json()



@app.route('/')
def home():
    print(post_data)
    return render_template('index.html', posts= post_data)
# 
# 
@app.route('/about')
def about():
    return render_template('about.html')
# 
# 
@app.route('/contact')
def contact():
    return render_template('contact.html')
# 
@app.route("/post/<id>")
def get_post(id):
    post_send = post_data[0]
    for post in post_data:
        if post['id'] == int(id):
            post_send = post
    return render_template('post.html', post = post_send)





if __name__ == '__main__':
    app.run(debug=True)
    Compress(app)
