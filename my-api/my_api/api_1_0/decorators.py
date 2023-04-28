"""
JWT Decorators
"""

from functools import wraps
from flask_jwt_extended.exceptions import CSRFError, NoAuthorizationError
from flask_jwt_extended import (
    verify_jwt_in_request,
)
import jwt


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
