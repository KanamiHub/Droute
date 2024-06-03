from flask import Flask
from blueprints.code.app import app
from blueprints.droute import droute

main = Flask(__name__)

main.register_blueprint(app, url_prefix='/')
main.register_blueprint(droute, url_prefix='/droute')

if __name__ == '__main__':
    main.run()