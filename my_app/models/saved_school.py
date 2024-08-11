
# my_app/models/saved_school.py

from django.db import models
from .user import CustomUser
from .school import School

class SavedSchool(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'school')

    def __str__(self):
        return f"{self.user.username} saved {self.school.name}"
