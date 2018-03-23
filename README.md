# Bread Exercise 1

An implementation of a Bread button adhering to exercise parameters. The web application is built upon the Flask microframework, a simple tool for writing tight and tiny web applications.

## Installation and Setup

Optional: Setup a virtual environment using virtualenv
```
pip install virtualenv
virtualenv -p python3 .venv
. .venv/bin/activate
```

Install Flask microframework
```
pip install -r requirements.txt
```

Launch Flask application
```
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

Navigate to `127.0.0.1:5000` to view the app

## Notes

`app.py` contains the routing logic, and the tax calculation and shipping option endpoints.
`templates/app.html` configures the button itself.

Most of the solutions are idiomatic according to the Bread documentation. A hack was used, however, to color the button text red. The default button CSS was copied and pasted into the `customCSS` field for the `opts` struct, which was modified to have red text. I am interested in knowing if there is a cleaner way to modify the button style without needing to redefine the style entirely.
