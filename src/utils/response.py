from flask import Response, json, request
from src.models import db

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

def collection_response(data, status = 200, extra = {}):
    """
    Response data into result field
    """
    payload = {
        'result': data,
        **extra
    }
    return Response(
        mimetype    = "application/json",
        response    = json.dumps(payload),
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

def no_content():
    """
    Response no content to client
    """
    return Response(
        mimetype    = "application/json",
        status      = 204
    )

def paginate(query, serializer, size = 5):
    """
    Serializer response paginated
    """
    #get query
    if(isinstance(query, type(db.Model))):
        query = query.query
    #current page
    page = int(request.args.get('page')) if request.args.get('page') else 1
    page = page if page > 0 else 1
    #query of pagination
    paginate_query = query.limit(size).offset((page - 1) * size)
    #serialize response data
    serialized = serializer.dump(paginate_query.all(), many=True)
    #next and prev pages
    next_page = page + 1
    prev_page = page -1 if page > 1 else 1
    #return response
    return collection_response(serialized, 200, {
        'per_page':     size,
        'total':        query.count(),
        'next':         request.base_url + '?page=' + str(next_page),
        'prev':         request.base_url + '?page=' + str(prev_page),
    })