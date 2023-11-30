from flask import Flask

from app.views import index_bp

app = Flask(__name__)


def create_app(config):
    """
    Creates and configures the Flask application.

    Args:
        config (str): The name of the configuration class to use for the Flask
        application.

    Returns:
        The configured Flask application instance.
    """

    app.config.from_object(config)

    app.register_blueprint(index_bp)

    return app
