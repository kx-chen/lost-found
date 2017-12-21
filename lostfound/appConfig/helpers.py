from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

def logged_out_required(error_redirect=None):
    def decorator(view_func):
        @wraps(view_func)
        def check_logged_out(*args, **kwargs):
            if not current_user.is_authenticated:
                return view_func
            else: 
                return redirect(url_for(error_redirect))
        return check_logged_out
    return decorator
