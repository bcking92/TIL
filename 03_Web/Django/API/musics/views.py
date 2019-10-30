from django.shortcuts import render
from .models import Music, Comment, Artist
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here

@api_view(['GET'])
def music_list(reqeust):
    musics = Music.objects.all()
    # context = {
    #     'musics': musics,
    # }
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_id):
    musics = get_object_or_404(Music, pk=music_id)
    serializer = MusicDetailSerializer(musics)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_id):
    # form = CommentForm(request.POST)
    serializer = CommentSerializer(data=request.data)
    # raise_exception=True 400 bad request를 띄워줌
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_id)
    return Response(serializer.data)
