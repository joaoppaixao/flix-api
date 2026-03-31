from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # prefixo de URL de authentication
    path('api/v1/', include('authentication.urls')),

    # prefixo de URL de generos
    path('api/v1/', include('genres.urls')),

    # prefixo de URL de atores
    path('api/v1/', include('actors.urls')),

    # prefixo de URL de filmes
    path('api/v1/', include('movies.urls')),

    # prefixo de URL de reviews
    path('api/v1/', include('reviews.urls')),

]
