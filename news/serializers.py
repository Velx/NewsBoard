from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data,
            post_id=self.context['post_id']
        )

    def update(self, instance, validated_data):
        instance.author_name = validated_data.get(
            'author_name',
            instance.author_name
        )
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = ['title', 'link', 'creation_date',
                  'upvotes_amount', 'author_name']
        extra_kwargs = {
            'upvotes_amount': {'read_only': True}
        }


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = PostSerializer.Meta.fields + ['comments']
