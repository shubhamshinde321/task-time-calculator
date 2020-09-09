from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserForm
import logging


logger = logging.getLogger(__name__)


@login_required
def user_form(request):
    if request.method == "POST":
        try:
            user = request.user
            task_name = request.POST.get('task_name').strip()
            project = request.POST.get('project').strip()
            start_time = request.POST.get('start_time').strip()
            end_time = request.POST.get('end_time').strip()
            total_time = request.POST.get('total_time').strip()

            start_time = datetime.strptime(start_time, '%m/%d/%Y, %H:%M:%S')
            end_time = datetime.strptime(end_time, '%m/%d/%Y, %H:%M:%S')

            exists = UserForm.objects.filter(task_name=task_name).exists()
            if not exists:
                form = UserForm(user=user, task_name=task_name,
                                project=project,
                                start_time=start_time, end_time=end_time,
                                total_time=total_time)
                form.save()
                messages.success(request, 'Task Submitted Successfully')
                return redirect('user_form:task_form')
            else:
                messages.warning(request, 'Task name Already Exists')
                return redirect('user_form:task_form')
        except Exception as error:
            logger.debug(error)
            messages.warning(request, 'Task Submission Failed')
            return redirect('user_form:task_form')
    return render(request, 'user_form/forms.html')


@login_required
def task_Data(request):
    if request.method == "POST":
        date = request.POST.get('date').strip()
        start_date = datetime.strptime(date, '%Y-%m-%d')
        end_date = start_date + timedelta(1)
        data_list = UserForm.objects.filter(
                            form_submitted_at__range=(start_date, end_date))
        return render(request, 'user_form/task_table.html', {
                                'data_list': data_list})
    return render(request, 'user_form/task_list.html')


def error_404(request, exception):
    return render(request, 'user_form/error404.html', status=404)


def error_500(request):
    return render(request, 'user_form/error500.html', status=500)
