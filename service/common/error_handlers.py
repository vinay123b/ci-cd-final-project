"""
Error Handlers
"""
from flask import jsonify
from service import app
from service.common import status


@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """Handles 404 Not Found errors"""
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND,
            error="Not Found",
            message=error.description,
        ),
        status.HTTP_404_NOT_FOUND,
    )


@app.errorhandler(status.HTTP_409_CONFLICT)
def conflict(error):
    """Handles 409 Conflict errors"""
    return (
        jsonify(
            status=status.HTTP_409_CONFLICT,
            error="Conflict",
            message=error.description,
        ),
        status.HTTP_409_CONFLICT,
    )


@app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
def method_not_supported(error):
    """Handles 405 Method Not Allowed errors"""
    return (
        jsonify(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            error="Method Not Allowed",
            message=error.description,
        ),
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@app.errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    """Handles 500 Internal Server Error"""
    return (
        jsonify(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=error.description,
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
