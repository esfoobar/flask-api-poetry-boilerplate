"""
JWT Decorators
"""

from functools import wraps
from flask_jwt_extended.exceptions import CSRFError, NoAuthorizationError
from flask_jwt_extended import get_jwt, verify_jwt_in_request
import jwt
from werkzeug.exceptions import BadRequest

from my_api.api_1_0.user.models import RoleEnum


def token_required(fn):
    """JWT token required decorator"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except jwt.exceptions.ExpiredSignatureError:
            return {"message": "SIGNATURE_EXPIRED"}, 403
        except jwt.exceptions.InvalidSignatureError:
            return {"message": "SIGNATURE_VERIFICATION_FAILED"}, 403
        except CSRFError:
            return {"message": "CSRF_FAILED"}, 403
        except NoAuthorizationError:
            return {"message": "NO_AUTHORIZATION_HEADER"}, 403
        except Exception:  # pylint: disable=broad-except
            return {"message": "INVALID_TOKEN"}, 403
        return fn(*args, **kwargs)

    return wrapper


def refresh_token_required(fn):
    """JWT refresh token required decorator"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request(refresh=True)
        except jwt.exceptions.ExpiredSignatureError:
            return {"message": "SIGNATURE_EXPIRED"}, 403
        except jwt.exceptions.InvalidSignatureError:
            return {"message": "SIGNATURE_VERIFICATION_FAILED"}, 403
        except Exception:  # pylint: disable=broad-except
            return {"message": "INVALID_TOKEN"}, 403
        return fn(*args, **kwargs)

    return wrapper


def admin_required(fn):
    """Admin required decorator"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_user = get_jwt()
        if jwt_user["role_name"] != RoleEnum.ADMIN.name.lower():
            e = BadRequest()
            e.data = {"message": "UNAUThORIZED_USER"}
            raise e
        return fn(*args, **kwargs)

    return wrapper
