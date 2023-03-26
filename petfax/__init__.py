from flask import Flask

# factory
def create_app() :
    app = Flask(__name__)

    @app.route('/')
    def hello() :
        return 'Hello, This is PetFax!'

    # register pet bluprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    # return the app
    return app