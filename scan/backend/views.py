from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from backend.models import *

# Create your views here.
def post(request):
    upc = request.POST["upc"]
    poster = request.POST["poster"]
    contents = request.POST["contents"]
    prod = Product.objects.get(upc=upc)
    Comment.objects.create(
        product=prod,
        poster=poster,
        contents=contents
    )
    return JsonResponse({
        "success": True,
        "poster": str(poster),
        "contents": str(contents),
        "score": 0
    })

def getPosts(request):
    upc = request.GET["upc"]
    posts = {
        "success": True,
        "posts": []
    }
    for comment in Comment.objects.filter(product__upc=upc).order_by('-score'):
        posts["posts"].append({
            "id": comment.id,
            "score": int(comment.score),
            "poster": str(comment.poster),
            "contents": str(comment.contents)
        })
    return JsonResponse(posts)

def auth(request):
    username = request.GET["username"]
    password = request.GET["password"]
    try:
        user = InsecureUser.objects.get(username=username, password=password)
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})

def register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    success = True
    try:
        user = InsecureUser.objects.create(username=username, password=password)
    except:
        success = false
    return JsonResponse({"success": success})

def vote(request):
    try:
        up = request.POST["up"]
        cid = request.POST["id"]
        cmt = Comment.objects.get(id=cid)
        cmt.score += 1 if up == "true" else -1
        cmt.save()
        return JsonResponse({"success": True, "score": cmt.score})
    except:
        return JsonResponse({"success": True, "score": 0})
