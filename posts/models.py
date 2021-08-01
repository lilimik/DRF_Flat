from django.db import models


class CommonModel(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=False, blank=False)

    class Meta:
        abstract = True


class Post(CommonModel):
    title = models.CharField(max_length=250, verbose_name='заголовок', null=False, blank=False)
    content = models.TextField(verbose_name='контент', null=False, blank=False)

    def __str__(self):
        title = f'{self.title[:50]}...' if len(self.title) > 50 else self.title
        return f'[{self.date_of_creation.strftime("%d.%m.%y")}] - {title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(CommonModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост',
                             related_name='comments', null=True, blank=True)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='комментарий',
                                related_name='comments', null=True, blank=True)
    text = models.CharField(max_length=300, blank=False, verbose_name='текст')

    def __str__(self):
        text = f'{self.text[:50]}...' if len(self.text) > 50 else self.text
        return f'[{self.date_of_creation.strftime("%d.%m.%y %H.%i")}] | {text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
