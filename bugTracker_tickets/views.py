from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from bugTracker_tickets.forms import NewTicketForm, TicketDetailForm
from bugTracker_tickets.models import BugTicket
from bugTracker_users.models import TrackerUser

# Create your views here.


@login_required
def homepage_view(request):
    if request.user.display_name:
        user = request.user.display_name
    else:
        user = request.user.username

    open_tickets = BugTicket.objects.filter(status='open')
    in_prog_tickets = BugTicket.objects.filter(status='in progress')
    completed_tickets = BugTicket.objects.filter(status='complete')
    invalid_tickets = BugTicket.objects.filter(status='invalid')

    return render(
        request,
        'index.html',
        {
            'user': user,
            'open': open_tickets,
            'in_progress': in_prog_tickets,
            'complete': completed_tickets,
            'invalid': invalid_tickets
        }
    )


@login_required
def new_ticket_view(request):
    # POST request handling
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return HttpResponseRedirect(
                reverse('homepage')
            )
        # GET request handling

    form = NewTicketForm()
    creator_field = form.fields['creator']
    creator_field.initial = request.user
    creator_field.queryset = TrackerUser.objects.filter(
        username=request.user.username)

    return render(
        request,
        'form.html',
        {
            'page_title': 'New Ticket',
            'button_value': 'Submit Ticket',
            'form': form,
            'auth': request.user.is_authenticated

        }
    )


@login_required
def ticket_detail_view(request, ticketId):
    ticket = BugTicket.objects.get(id=ticketId)
    # POST request handling
    if request.method == 'POST':
        form = TicketDetailForm(request.POST)
        # validate form
        if form.is_valid():
            data = form.cleaned_data
            new_title = data['title']
            new_desc = data['description']
            assigned = data['assign']
            completed = data['completed']
            marked_as_invalid = data['invalid']

            # check for changes
            if new_title != ticket.title:
                ticket.title = new_title
            if new_desc != ticket.description:
                ticket.description = new_desc
            if assigned:
                ticket.assigned_to = request.user
                ticket.status = 'in progress'
            if completed:
                ticket.assigned_to = None
                ticket.completed_by = request.user
                ticket.status = 'complete'
            if marked_as_invalid:
                ticket.assigned_to = None
                ticket.completed_by = None
                ticket.status = 'invalid'
            if not assigned and not completed and not marked_as_invalid:
                ticket.status = 'open'

            ticket.save()
            return HttpResponseRedirect(
                reverse('homepage')
            )

    # GET request handling
    form = TicketDetailForm(instance=ticket)
    form.fields['creator'].queryset = TrackerUser.objects.filter(
        id=ticket.creator.id)

    return render(
        request,
        'form.html',
        {
            'page_title': ticket.title,
            'button_value': 'Save Changes',
            'form': form,
            'auth': request.user.is_authenticated
        }
    )
