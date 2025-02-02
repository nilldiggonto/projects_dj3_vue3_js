from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from time_track_project.time_team.models import Team

class ProjectTask(models.Model):
    team        = models.ForeignKey(Team,related_name='projects',on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)

    created_by = models.ForeignKey(User,related_name='projects',on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

    def registered_time(self):
        # minutes = 0
        # entries = self.entries.all()
        # for entry in entries:
        #     minutes = minutes + entry.minutes
        # return minutes
        return sum(entry.minutes for entry in self.entries.all())
    def num_tasks_todo(self):
        return self.tasks.filter(status=TaskPrimary.TODO).count()


class TaskPrimary(models.Model):
    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (TODO,'Todo'),
        (DONE,'Done'),
        (ARCHIVED,'Archived')
    )
    team        = models.ForeignKey(Team,related_name='tasks',on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    project     = models.ForeignKey(ProjectTask,related_name='tasks',on_delete=models.CASCADE)
    status      = models.CharField(max_length=25,choices=CHOICES_STATUS,default=TODO)

    created_by = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())





#time track
class Entry(models.Model):
    team        = models.ForeignKey(Team,related_name='entries',on_delete=models.CASCADE)
    project     = models.ForeignKey(ProjectTask,related_name='entries', on_delete=models.CASCADE,blank=True,null=True)
    task        = models.ForeignKey(TaskPrimary,related_name='entries', on_delete=models.CASCADE,blank=True,null=True)
    minutes     = models.IntegerField(default=0)
    is_track    = models.BooleanField(default=False)
    created_by  = models.ForeignKey(User,related_name='entries',on_delete=models.CASCADE)
    created_at  = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.task:
            return '%s - %s' % (self.task.title,self.created_at)
        return '%' % self.created_at

