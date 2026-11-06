import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from tasks.models import Task
@pytest.mark.django_db
def test_register_and_create_task():
 c=APIClient(); r=c.post("/api/auth/register/",{"username":"sam","email":"sam@example.com","password":"StrongPass123!"},format="json")
 assert r.status_code==201
 u=get_user_model().objects.get(username="sam"); c.force_authenticate(user=u)
 r=c.post("/api/tasks/",{"title":"Learn DRF","priority":"high"},format="json")
 assert r.status_code==201 and r.data["owner"]=="sam"
@pytest.mark.django_db
def test_users_only_see_own_tasks():
 U=get_user_model(); a=U.objects.create_user(username="alice",password="password123"); b=U.objects.create_user(username="bob",password="password123")
 Task.objects.create(owner=a,title="Secret")
 c=APIClient(); c.force_authenticate(user=b)
 assert c.get("/api/tasks/").data["count"]==0
@pytest.mark.django_db
def test_invalid_status_is_rejected():
 u=get_user_model().objects.create_user(username="tester",password="password123")
 c=APIClient(); c.force_authenticate(user=u)
 assert c.post("/api/tasks/",{"title":"bad","status":"unknown"},format="json").status_code==400
