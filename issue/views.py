from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue
from .forms import IssueForm


@login_required()
def issue(request):
    if request.method == "POST":
        issue_form = IssueForm(request.POST)

        if issue_form.is_valid():
            newissue = issue_form.save(commit=False)
            newissue.save()

            messages.error(request, "New issue has been created!")
            return redirect(reverse('issue'))
        else:
            print(issue_form.errors)
            messages.error(request, "Unable to submit issue!")
    else:
        issue_form = IssueForm()

    return render(request, "issue.html", {'issue_form': issue_form})


def upvote(request, id):
    """Increase the upvote count"""

    i = Issue.objects.get(id=id)
    i.upvotes += 1
    i.save()

    # Take user back to main page, but ensure we maintain the filter state
    return redirect(reverse('filters', args=(request.session['issue_filter'],)))

