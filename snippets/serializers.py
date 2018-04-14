from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many = True, queryset = Snippet.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username' , 'snippets')

class SnippetSerializers(serializers.Serializer):
	owner = serializers.ReadOnlyField(source = 'owner.username')
	id = serializers.IntegerField(read_only = True)
	title = serializers.CharField(required = False, max_length = 100)
	code = serializers.CharField(style = {'base_template' : 'textarea.html'})
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
	
	"""
	class Meta:
		model = Snippet
		fields = ('id' , 'title' , 'code' , 'linenos' , 'language' , 'style')
		"""
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