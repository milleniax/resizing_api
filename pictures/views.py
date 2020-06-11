from django.shortcuts import get_object_or_404, render
from .models import Content
from .serializers import ContentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from celery import current_app
from celery.task.control import inspect
from django.http import JsonResponse
from django.views import View
import logging

logger = logging.getLogger(__name__)



def pictures(request):
    pictures = Content.objects.all()
    return render(request, 'pictures/pictures.html', {'pictures': pictures})


class ContentView(APIView):
    def get(self, request):
        content = Content.objects.all()
        serializer = ContentSerializer(content, many=True)
        return Response({"content": serializer.data})

    def post(self, request):
        content = request.data.get('content')
        # Create an article from the above data
        serializer = ContentSerializer(data=content)
        if serializer.is_valid(raise_exception=True):
            content_saved = serializer.save()
        return Response({"success": "Content created successfully"})

    def put(self, request, pk):
        saved_content = get_object_or_404(Content.objects.all(), pk=pk)
        data = request.data.get('content')
        serializer = ContentSerializer(
            instance=saved_content, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            content_saved = serializer.save()
        else:
            logger.error("Сериализатор инвалид")
        return Response({
            "success": "Picture '{}' updated successfully".format(content_saved.id)
        })


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return JsonResponse(response_data)

    
