from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        return render_template('generator/index.html')

    @app.route('/render')
    def render():
        return 'Rendering CSV file to download'

    return app
