# Create your views here.

from django.shortcuts import render_to_response
from photobookengine.models import Post

def getRecentPosts(request):
    # recuperation des posts
    posts = Post.objects.all()
    
    # triage dans l'ordre alphabetique
    sorted_posts = posts.order_by('-pub_date')
    
    # Affichage de tout les postes
    return render_to_response('templatePost.html', { 'posts':sorted_posts})