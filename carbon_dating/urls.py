"""carbon_dating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# from author.views import home_view, explore_view
from author import views as author_views
# from authentication.views import SignUpView
from authentication import views as authentication_views
from direct_messages.urls import url_patterns as messages_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', author_views.home_view, name='homepage'),
    # path('', include('django.contrib.auth.urls')),
    path('login/', authentication_views.LoginFormView.as_view(), name="login"),
    path('logout/', authentication_views.LogoutView.as_view(), name="logout"),
    path('explore/', author_views.explore_view, name="explore"),
    path('signup/', authentication_views.SignUpView.as_view(), name='signup'),
    path('posts/', include('post.urls')),
    path('posts/', include('comment.urls')),
    path(
        'author_profile/<int:user_id>/',
        author_views.author_profile,
        name="author_profile"
        ),
    path('admire/<int:user_id>/', author_views.admire_view),
    path('profile_admire/<int:user_id>/', author_views.profile_admire_view),
    path('change_profile/', author_views.change_profile, name="change_profile"),
    path('password/', author_views.PasswordsChangeView.as_view(template_name="change_password.html")),
    *messages_urls,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
