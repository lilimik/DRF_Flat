from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text',)


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('comments',)


class AdditionalValidation:
    requires_context = True

    def __init__(self, post, comment):
        self.post = post
        self.comment = comment

    def __call__(self, post, comment):
        if self.post is None and self.comment is None:
            raise serializers.ValidationError('The form must contain one of the fields: post, comment')
        if self.post is not None and self.comment is not None:
            raise serializers.ValidationError('The form must contain only one of the fields: post, comment')


class CommentCreateSerializer(CommentSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id', required=False)
    comment = serializers.SlugRelatedField(queryset=Comment.objects.all(), slug_field='id', required=False)

    class Meta:
        model = Comment
        fields = (*CommentSerializer.Meta.fields, 'post', 'comment')
        validators = [AdditionalValidation]

