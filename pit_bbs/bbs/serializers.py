from rest_framework import serializers
from .models import Novel

class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ('id', 'title', 'author', 'pw', 'content')
    #신규 Novel instance를 생성해서 리턴해준다.
    def create(self, validated_data):
        return Novel.objects.create(**validated_data)
    # 생성되어 있는 Novel Instance 를 저장한 후 리턴해준다.
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.title)
        instance.pw = validated_data.get('pw', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.save()
        return instance