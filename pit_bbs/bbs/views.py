from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Novel
from .serializers import NovelSerializer

# 요청 url인 bbs/ 에 대해서 urls.py에 정의된 view.bbs_list 가 호출된다.
@api_view(['GET', 'POST'])
def bbs_list(request, format=None):
    if request.method == 'GET':
        novel = Novel.objects.all()
        serializer = NovelSerializer(novel, many=True) #many 값이 True이면 다수의 데이터 instance를 직렬화 할 수 있다.
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 요청 url 인 bbs/번호 에 대해서 urls.py에 정의된 view.bbs_detail 이 호출된다.
@api_view(['GET','PUT','DELETE'])
def bbs_detail(request, pk, format=None):
    try:
        novel = Novel.objects.get(pk=pk)
    except Novel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NovelSerializer(novel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NovelSerializer(novel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        novel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
