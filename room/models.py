from django.db import models
from users.models import User
from uuid import uuid4
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete



class Ip (models.Model) : 
    ip = models.CharField(max_length=20,db_index=True)

    def __str__(self) : 
        return self.ip

class Room (models.Model) : 
    id  = models.UUIDField(default=uuid4,editable=False,primary_key=True,db_index=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    visitors = models.ManyToManyField(Ip,related_name='visitors_ips',blank=True)

    def __str__(self) : 
        return self.title
    
class Message (models.Model) : 
    text = models.TextField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


@receiver(post_save, sender=Room)
def Update_Room_Create (created, instance, **kwargs) : 
    if created :
        cache.set('rooms', Room.objects.all() )



@receiver(post_delete,sender=Room)
def Update_room_Delete (instance, **kwargs) :
    rooms = cache.get('rooms')
    rooms = rooms.exclude(id=instance.id)
    cache.set('rooms', rooms)
