from flask import Flask, Response, json
import requests

app = Flask(__name__)

base_url = "https://jsonplaceholder.typicode.com/users"

home_message = """<h1>Demo app</h1>
This app consumes the <a href="https://jsonplaceholder.typicode.com">{JSON} Placeholder</a> service.<br/><br/>
<h3>Endpoints available:</h3>
<ul>
<li>/users</li>
<li>/users/{id}</li>
</ul>"""


@app.route("/")
def home():
    return home_message


@app.route("/users")
def users():
    data = requests.get(base_url)

    return Response(
        data.text,
        status=data.status_code,
        content_type=data.headers["content-type"],
    )


@app.route("/users/<id>")
def user(id):
    data = requests.get(f"{base_url}/{id}")

    return Response(
        json.dumps({"message": f"User {id} not found"})
        if data.status_code == 404
        else data.text,
        status=data.status_code,
        content_type=data.headers["content-type"],
    )
