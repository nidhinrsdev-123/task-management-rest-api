from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
 operations=[migrations.CreateModel(name="Task",fields=[
 ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
 ("title",models.CharField(max_length=200)),("description",models.TextField(blank=True)),
 ("status",models.CharField(choices=[("todo","To do"),("in_progress","In progress"),("done","Done")],default="todo",max_length=20)),
 ("priority",models.CharField(choices=[("low","Low"),("medium","Medium"),("high","High")],default="medium",max_length=10)),
 ("due_date",models.DateField(blank=True,null=True)),("created_at",models.DateTimeField(auto_now_add=True)),
 ("updated_at",models.DateTimeField(auto_now=True)),
 ("owner",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="tasks",to=settings.AUTH_USER_MODEL))],
 options={"ordering":["-created_at"],"indexes":[models.Index(fields=["owner","status"],name="tasks_owner__a4b6d2_idx"),models.Index(fields=["due_date"],name="tasks_due_dat_8f7b1a_idx")]})]
