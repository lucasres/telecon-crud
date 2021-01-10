from src.models import db
from src.utils.response import single_response
import datetime
import os
import traceback

def handle_internal_server_error(e):
    """
    Handle with 500 error
    """
    #rollback sessions
    db.session.rollback()
    #write trackeback erro in file
    filename = os.path.join('storage','error.txt')
    with open(filename, 'a+') as f:
        time = datetime.datetime.now()
        f.write('[' + str(time) + '] - ' + str(e))
        f.write(traceback.format_exc())
    return single_response({'message': 'Internal server error'}, 500)