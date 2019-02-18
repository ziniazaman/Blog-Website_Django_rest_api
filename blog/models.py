from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    #tags = models.ManyToManyField(Tag, related_name='tags')
    tags = models.ManyToManyField('Tag')

    def get_tags(self):
        return ", ".join([t.name for t in self.tags.all()])

    def __str__(self):
        return "%s %s" % (self.title, self.category)





