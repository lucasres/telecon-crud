from flask import Response, json

def bad_request(error):
    """
    Return response with bad request status
    """
    return Response(
        mimetype="application/json",
        response=json.dumps({'errors': error.messages}),
        status=400
    )