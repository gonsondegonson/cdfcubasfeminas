from django.utils.datastructures import MultiValueDictKeyError

def GetParameter(request, name):

    try:
        param = request.GET[name]
    except MultiValueDictKeyError:
        param = None;

    return param

def GetRequestId(request):

    try:
        id = int(request.GET["Id"])
    except MultiValueDictKeyError:
        id = 0;

    return id

def GetObjectId(id, collection):

    if id == 0:
        current = collection[0]
    else:
        for current in collection:
            if (current.id == id):
                break

    return current
