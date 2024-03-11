from myapp import app

from waitress import serve


# To run from command line
def create_app():
    return app


if __name__ == "__main__":
    # flask server
    # app.run()
    # waitress server
    serve(app, listen='*:8080')
