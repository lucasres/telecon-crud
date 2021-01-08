from flask import Response, json

def bad_request(error):
    """
    Return response with bad request status
    """
    return Response(
        mimetype    = "application/json",
        response    = json.dumps({'errors': error.messages}),
        status      = 400
    )

def single_response(data, status = 200):
    """
    Response data in single json
    """
    return Response(
        mimetype    = "application/json",
        response    = json.dumps(data),
        status      = status
    )

def collection_response(data, status = 200):
    """
    Response data into result field
    """
    return Response(
        mimetype    = "application/json",
        response    = json.dumps({'result': data}),
        status      = status
    )

def not_fount():
    """
    Response not found to client
    """
    return Response(
        mimetype    = "application/json",
        response    = json.dumps({'errors': 'Not found entity'}),
        status      = 404
    )