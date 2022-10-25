from app.authentication.urls import urlpatterns as authentication_urls
from app.users.urls import urlpatterns as users_urls

urlpatterns = users_urls + authentication_urls
