from flask import Flask, Response, json
import requests

app = Flask(__name__)

base_url = "https://jsonplaceholder.typicode.com/users"

home_message = """<h1>Demo app</h1>
This app consumes the <a href="https://jsonplaceholder.typicode.com">{JSON} Placeholder</a> service.<br/><br/>
<h3>Endpoints available:</h3>
<ul>
<li>/users/{id}/albums</li>
<li>/users/{id}/posts</li>
</ul>"""


def validate_data(data, id):
    if len(data.json()) == 0:
        content_type = data.headers["content-type"]
        status_code = 404
        data = json.dumps({"message": f"User {id} not found"})
    else:
        content_type = data.headers["content-type"]
        status_code = data.status_code
        data = data.text
    return data, status_code, content_type


@app.route("/")
def home():
    return home_message


@app.route("/users/<id>/albums")
def users(id):
    data = requests.get(f"{base_url}/{id}/albums")
    data, status_code, content_type = validate_data(data, id)
    return Response(
        data,
        status=status_code,
        content_type=content_type,
    )


@app.route("/users/<id>/posts")
def user(id):
    data = requests.get(f"{base_url}/{id}/posts")
    data, status_code, content_type = validate_data(data, id)
    return Response(
        data,
        status=status_code,
        content_type=content_type,
    )
