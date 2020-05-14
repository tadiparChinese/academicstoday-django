from django.urls import path, include
from publisher.views import catalog
from publisher.views import my_publication
from publisher.views import publication

app_name = 'publisher'

urlpatterns = [
    # Publications(s)
    path('publish/', catalog.catalog_page),
    path('publication/(\\d+)/', publication.publication_page),
    path('publication/(\\d+)/peer_review_modal/', publication.peer_review_modal),
    path('publication/(\\d+)/save_peer_review/', publication.save_peer_review),
    path('publication/(\\d+)/delete_peer_review/',
         publication.delete_peer_review),

    # My Publications
    path('my_publications/', my_publication.my_publications_page),
    path('refresh_publications_table/',
         my_publication.refresh_publications_table),
    path('my_publication_modal/', my_publication.my_publication_modal),
    path('save_publication/', my_publication.save_publication),
    path('delete_publication/', my_publication.delete_publication),
]
