from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static, settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'academicstoday_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),

    # This regex makes the default URL for the website to launch this view.
    path('', include('landpage.urls', 'landpage')),
    path('', include('registration.urls', 'registration')),
    path('', include('login.urls', 'login')),
    path('', include('account.urls', 'account')),
    path('', include('registrar.urls', 'registrar')),
    path('', include('student.urls', 'student')),
    path('', include('teacher.urls', 'teacher')),
    path('', include('publisher.urls', 'publisher')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
