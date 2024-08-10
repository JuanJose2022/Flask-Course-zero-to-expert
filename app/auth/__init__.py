from flask import Blueprint
    #__name__ : It makes reference to the file name auth.  
auth = Blueprint("auth", __name__, url_prefix='/auth')# url_prefix='/auth : Redirect all routes to this blueprint.

from . import views