from app.authentication.urls import urlpatterns as authentication_urls
from app.departments.urls import urlpatterns as departments_urls
from app.equipments.urls import urlpatterns as equipments_urls
from app.repair.urls import urlpatterns as repair_urls
from app.suppliers.urls import urlpatterns as suppliers_urls
from app.users.urls import urlpatterns as users_urls

urlpatterns = (
    authentication_urls
    + users_urls
    + departments_urls
    + equipments_urls
    + suppliers_urls
    + repair_urls
)
