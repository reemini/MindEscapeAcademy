from django.db import models

class Educator(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    picture = models.ImageField(upload_to='course_pictures/')  # For uploading course pictures
    files = models.ManyToManyField('File', related_name='courses', blank=True)   # For uploading files like PDFs, Word documents, audio, or videos
    

    def __str__(self):
        return self.title
    # Add more fields as needed
    
class File(models.Model):
    file = models.FileField(upload_to='course_files/')  # For uploading files like PDFs, Word documents, audio, or videos

    def __str__(self):
        return self.file.name