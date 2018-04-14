from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

	url(r'^snippets/$', views.SnippetList.as_view()),
<<<<<<< HEAD
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetails.as_view()),
=======
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
>>>>>>> 119d5089c749b5d9ed8d3650fd2e9f93751fdb1b

]
urlpatterns = format_suffix_patterns(urlpatterns)