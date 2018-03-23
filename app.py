import flask
app = flask.Flask(__name__)


# Calculates tax based on shipping address
@app.route('/tax', methods=['POST'])
def tax():
    print('In tax')
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


# Returns an array of shipping options
@app.route('/shipping', methods=['POST'])
def shipping():
    print('In shipping')

    resp = []

    twoDayShipping = {
      'typeId': 'two day',
      'cost': 5000,
      'type': 'Two-Day Shipping'
    }
    overnightShipping = {
      'typeId': 'overnight',
      'cost': 10000,
      'type': 'Overnight Shipping'
    }

    resp.append(twoDayShipping)
    resp.append(overnightShipping)

    return flask.jsonify(resp)


@app.route('/')
def main():
    return flask.render_template('app.html')
