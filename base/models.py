from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    heading = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
        
    