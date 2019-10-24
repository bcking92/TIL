from rest_framework import serializers
from .models import Music, Comment, Artist

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)

    # 물론 직접 다 적어줄 수도 있지만 상속 받는 것이 당연히 좋다.
    # property가 많아지면 코드가 길어지기 때문 + 코드 중복은 피하기 + 모듈화를 이용하기

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MusicDetailSerializer(serializers.ModelSerializer):
    # source는 모델파일에 related_name을 다르게 설정해 준것을 사용할 때
    # comments = CommentSerializer(source='comment_set', many=True)
    comment_set = CommentSerializer(many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)