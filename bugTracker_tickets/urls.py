from django.urls import path
from bugTracker_tickets import views

url_paths = [
    path('', views.homepage_view, name='homepage'),
    path('tickets/new', views.new_ticket_view, name='new_ticket'),
    path('tickets/<int:ticketId>', views.ticket_detail_view, name='ticket_detail')
]
