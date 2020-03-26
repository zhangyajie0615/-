from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import LeaveForm

# Create your views here.
@require_POST
def leave(request):

    form = LeaveForm(request.POST)

    if form.is_valid():

        leave = form.save(commit=False)

        leave.save()

        messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
        return redirect('blog:index')

    context = {
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)


def liu(request):
    return render(request, 'leaves/inclusions/liu.html')
