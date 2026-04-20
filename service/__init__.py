"""
Package: service
Package for the application models and services
"""
from flask import Flask
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)

# Load Configuration
app.config.from_object("config")

# Dependencies require we import the routes after the Flask app is created
from service import routes, models  # pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: E402, E261

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info(" SERVICE RUNNING ".center(70, "*"))
app.logger.info(70 * "*")

app.logger.info("Service initialized!")
