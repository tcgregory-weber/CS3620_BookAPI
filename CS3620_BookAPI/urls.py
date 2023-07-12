"""CS3620_BookAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BookAPI.views import BookViewSet, HistoryViewSet, FantasyViewSet, HistoricalFictionViewSet, ScienceFictionViewSet, ThrillerViewSet, SelfHelpViewSet, MemoirViewSet, NonFictionViewSet, SocialScienceFictionViewSet, BiographyViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('history', HistoryViewSet)
router.register('fantasy', FantasyViewSet)
router.register('historicalfiction', HistoricalFictionViewSet)
router.register('sciencefiction', ScienceFictionViewSet)
router.register('socialsciencefiction', SocialScienceFictionViewSet)
router.register('thriller', ThrillerViewSet)
router.register('selfhelp', SelfHelpViewSet)
router.register('memoir', MemoirViewSet)
router.register('nonfiction', NonFictionViewSet)
router.register('biography', BiographyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
