import bottle

@bottle.route('/hello/<name>')
def index(name):
    return bottle.template('<b>Hello {{name}}</b>!', name=name)

bottle.run(host='localhost', port=8080)
