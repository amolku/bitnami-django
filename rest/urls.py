from django.conf.urls import url, include
from rest import views
from rest_framework.routers import DefaultRouter

# Create a router adn register our viewsets with it
router = DefaultRouter(schema_title='Pastebin API')
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router
# Additinoally, we incldue hte login URLs for the browsable api

#app_name = 'rest' # this may cuase many errors -- it did for me
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
