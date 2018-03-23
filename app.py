import flask
app = flask.Flask(__name__)


@app.route('/tax', methods=['POST'])
def tax():
    print("In tax")
    # Assume incoming data is JSON
    data = flask.request.get_json(force=True)
    print(data)

    # Find city
    state = data['shippingAddress']['state']

    # Find total value
    total = data['total']
    tax = 0

    # If city is NY, apply 5% tax
    if state == 'NY':
        tax = int(total * 0.05)

    resp = {'tax': tax}
    return flask.jsonify(resp)


@app.route('/')
def main():
    print("In main")
    return flask.render_template('app.html', words='YO')
