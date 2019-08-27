from flask import Blueprint, jsonify


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/ping', methods=('GET', ))
def ping():
    """
    This is for health check

    Returns: {
        'status': 'ok',
        'message': 'pong!'
    }
    """
    return jsonify({
        'status': 'ok',
        'message': 'pong!'
    })
