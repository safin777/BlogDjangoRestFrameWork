from rest_framework.serializers import ModelSerializer
from .models import Post 


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
         # This will serialize all the fields of the Post model;
        fields = '__all__' # This will serialize all the fields of the Post model;
