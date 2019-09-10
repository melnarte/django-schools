from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from schools.views import SignUpView,Profile, home,load_courses
from students.views import StudentSignUpView
from teachers.views import TeacherSignUpView
urlpatterns = [
	path('', home, name='home'),
	path('admin/', admin.site.urls),
    path('schools/', include(('schools.urls','schools'),namespace='schools')),
    path('students/', include(('students.urls','students'),namespace='students')),
    path('teachers/', include(('teachers.urls','teachers'),namespace='teachers')),
    path('classroom/', include(('classroom.urls','classroom'),namespace='classroom')),
    path('quizzes/', include(('quizzes.urls','quizzes'),namespace='quizzes')),
    path('dashboard/', include(('dashboard.urls','dashboard'),namespace='dashboard')),
    path('exams/', include(('exams.urls','exams'),namespace='exams')),

    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('settings/profile/', Profile.as_view(), name='profile'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/student/ajax/load-courses/', load_courses, name='ajax_load_courses'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
