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

def single_response(data, status = 200):
    return Response(
        mimetype="application/json",
        response=json.dumps(data),
        status=status
    )

def collection_response(data, status = 200):
    return Response(
        mimetype="application/json",
        response=json.dumps({'result': data}),
        status=status
    )