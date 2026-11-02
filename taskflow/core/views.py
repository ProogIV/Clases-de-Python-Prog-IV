from django.http import JsonResponse

def healt_check(request):
    return JsonResponse({"status": "ok", "service": "TaskFlow API"})
