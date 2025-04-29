from django.http import JsonResponse
def getRoutes(request):
    routes=[
        'GET /api/'
        'GET /api/rooms',
        'Get /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)