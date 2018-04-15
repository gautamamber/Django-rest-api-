from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many = True, queryset = Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username' , 'snippets')

class SnippetSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    highlight = serializers.HyperlinkedIdentityField(view_name = 'snippet-highlight' , format = 'html')
    
    class Meta:
        model = Snippet
        fields = ('url','id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    def update(self, instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.code = validated_data.get('title' , instance.code)
        instance.linenos = validated_data.get('title' , instance.linenos)
        instance.language = validated_data.get('title' , instance.language)
        instance.style= validated_data.get('title' , instance.style)
        instance.save()
        return instance