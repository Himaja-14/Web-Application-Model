from django.contrib import admin
from django.urls import path
from HRadministrator import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout-user', views.logout_user, name='logout-user'),
    path('homepage', views.homepage, name='homepage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('organization', views.org_setup, name='organization'),
    path('Create-organization', views.create_org, name='Create-organization'),
    path('Delete-organization/<int:id>', views.delorg, name='DeleteOrg'),
    path('department', views.dept_setup, name='department'),
    path('create-department', views.create_dept, name='create-department'),
    path('Delete-department/<int:id>', views.deldept, name='DeleteDept'),
    path('position', views.Pos_setup, name='position'),
    path('create-position', views.create_pos, name='create-position'),
    path('requisition', views.requi_setup, name='requisition'),
    path('create-requisition', views.create_requi, name='create-requisition'),
    path('candidate', views.cand_setup, name='candidate'),
    path('create-candidate', views.create_cand, name='create-candidate'),
    path('SendEmail/<int:id>', views.send_email, name='SendEmail'),
    path('Delete-candidate/<int:id>', views.delcand, name='DeleteCandidate'),
    path('assign-requisition/<pk>', views.requi_cand, name='assign-requisition'),
    path('assigned-candidated/<pk>', views.assigened_candidates, name='assigned-candidated'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)