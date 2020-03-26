from django import template
from ..forms import LeaveForm

register = template.Library()


@register.inclusion_tag('leaves/inclusions/leave.html', takes_context=True)
def show_leave_form(context, form=None):
    if form is None:
        form = LeaveForm()
    return {
        'form': form,
    }