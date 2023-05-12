from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.



@api_view(['GET']) # This decorator is used to specify which HTTP methods are allowed for this view
def index(request):
    #pass # This is a placeholder for the function body
    return Response("Hello World") # This is the function body



@api_view(['GET'])
def GetAllPosts(request): #get all the posts
   posts = Post.objects.all() # This is the query that will be executed on the database
   serializer = PostSerializer(posts, many=True) # This is the function body ,many=True means that we are serializing multiple objects
   return Response(serializer.data) # This is the function body



@api_view(['GET','POST'])   
def CreatePost(request): #create a post
     data = request.data # getting all the data from the client request
     serializer = PostSerializer(data=data) 
     if serializer.is_valid(): #if the data is valid save this into database
         serializer.save()
         return Response({"Success": "Post Created Successfully"},status=201)
     else:
         return Response(serializer.errors,status=400)
     

@api_view(['DELETE'])
def DeletePost(request): #delete a post 
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": "Post Deleted Successfully"},status=200)
    except:
        return Response({"Error": "Post Not Found"},status=404)


 



     