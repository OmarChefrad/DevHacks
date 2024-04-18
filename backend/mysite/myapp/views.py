from django.http import JsonResponse

def get_data(request):
    data = {'message': 'Data fetched from server!'}
    return JsonResponse(data)
