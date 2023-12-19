# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View  # CBV(原生Django)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from app01.serializer import TodoInfoSerializer
from app01.models import TodoInfo


# FBV(原生Django)
def auth(request):
    if request.method == "GET":
        return JsonResponse({"status": True, "message": "GET"})
    elif request.method == "POST":
        return JsonResponse({"status": True, "message": "POST"})


# CBV(原生Django)
class UserView(View):
    def get(self, request):
        return JsonResponse({"status": True, "message": "GET"})

    def post(self, request):
        return JsonResponse({"status": True, "message": "POST"})

# rest_framework
class TodoInfoView(APIView):
    def get(self, request):
        # print(request.GET)
        # print(request.query_params)
        todo_data = TodoInfo.objects.all()
        print(todo_data)
        serializer = TodoInfoSerializer(instance=todo_data, many=True)
        return Response({"status": True, "message": "GET", "info": serializer.data})

    def post(self, request):
        print(request.data)
        serializer = TodoInfoSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            # 插入紀錄
            todo = TodoInfo.objects.create(**serializer.validated_data)
            ser = TodoInfoSerializer(instance=todo, many=False)
            return Response({"status": True, "message": "POST", "info": ser.data})
        except Exception as e:
            print(e)
            return Response(serializer.errors)
# rest_framework
class TodoInfoDetailView(APIView):
    def get(self, request, id):
        todo_data = TodoInfo.objects.get(pk=id)
        serializer = TodoInfoSerializer(instance=todo_data, many=False)
        return Response({"status": True, "message": "GET", "info": serializer.data})

    def delete(self, request, id):
        TodoInfo.objects.get(pk=id).delete()
        return Response({"status": True, "message": "DELETE"})

    def put(self, request, id):
        serializer = TodoInfoSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            n = TodoInfo.objects.filter(pk=id).update(**serializer.validated_data)
            print('n',n)
            todo = TodoInfo.objects.get(id=id)
            ser = TodoInfoSerializer(instance=todo, many=False)
            return Response({"status": True, "message": "PUT", "info": ser.data})
        except Exception as e:
            print(e)
            return Response(serializer.errors)
    
    def patch(self, request, id):
        serializer = TodoInfoSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            n = TodoInfo.objects.filter(pk=id).update(**serializer.validated_data)
            print('n',n)
            todo = TodoInfo.objects.get(id=id)
            ser = TodoInfoSerializer(instance=todo, many=False)
            return Response({"status": True, "message": "PUT", "info": ser.data})
        except Exception as e:
            print(e)
            return Response(serializer.errors)
    

#
# @api_view(["GET"])
# def login(request):
#     return Response({'status':True,'message':'success'})