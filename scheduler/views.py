from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from . import forms


@csrf_exempt
def workstation_list(request: HttpRequest):
    workstations = models.Workstation.objects.all()
    workstation_data = [
        {
            'workstation_id': workstation.workstation_id,
            'workstation_name': workstation.workstation_name,
            'availability_status': workstation.availability_status
        }
        for workstation in workstations
    ]
    return JsonResponse(workstation_data, safe=False)


@csrf_exempt
def workstation_detail(request: HttpRequest, workstation_id):
    try:
        workstation = models.Workstation.objects.get(
            workstation_id=workstation_id)  # Retrieve the specific workstation
        workstation_data = {
            'workstation_id': workstation.workstation_id,
            'workstation_name': workstation.workstation_name,
            'availability_status': workstation.availability_status
        }
        return JsonResponse(workstation_data)
    except models.Workstation.DoesNotExist:
        return JsonResponse({'error': 'Workstation not found'}, status=404)


@csrf_exempt
def workstation_create(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = forms.WorkstationForm(data)
        if form.is_valid():
            workstation = form.save()
            return JsonResponse({'message': 'Workstation created successfully', 'workstation_id': workstation.workstation_id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def workstation_update(request: HttpRequest, workstation_id):
    try:
        workstation = models.Workstation.objects.get(
            workstation_id=workstation_id)
    except models.Workstation.DoesNotExist:
        return JsonResponse({'error': 'Workstation not found'}, status=404)
    if request.method == 'PUT':
        data = json.loads(request.body)
        form = forms.WorkstationForm(data, instance=workstation)
        if form.is_valid():
            workstation = form.save()
            return JsonResponse({'message': 'Workstation updated successfully', 'workstation_id': workstation.workstation_id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def workstation_delete(request: HttpRequest, workstation_id):
    try:
        workstation = models.Workstation.objects.get(
            workstation_id=workstation_id)
        workstation.delete()
        response = {
            'message': 'Workstation deleted successfully'
        }
        return JsonResponse(response)
    except models.Workstation.DoesNotExist:
        raise Http404("Workstation does not exist")


@csrf_exempt
def schedule_list(request: HttpRequest):
    schedules = models.Schedule.objects.all()
    schedule_data = [
        {
            'schedule_id': schedule.schedule_id,
            'employee_name': schedule.employee_name,
            'workstation_id': schedule.workstation_id,
            'schedule_date': schedule.schedule_date,
            'time_slot': schedule.time_slot
        } for schedule in schedules]
    return JsonResponse(schedule_data, safe=False)


@csrf_exempt
def schedule_detail(request: HttpRequest, schedule_id):
    try:
        schedule = models.Schedule.objects.get(schedule_id=schedule_id)
        schedule_data = {
            'schedule_id': schedule.schedule_id,
            'employee_name': schedule.employee_name,
            'workstation_id': schedule.workstation_id,
            'schedule_date': schedule.schedule_date,
            'time_slot': schedule.time_slot
        }
        return JsonResponse(schedule_data)
    except models.Schedule.DoesNotExist:
        raise Http404("Schedule does not exist")


@csrf_exempt
def schedule_create(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = forms.ScheduleForm(data)
        if form.is_valid():
            schedule = form.save()
            return JsonResponse({'message': 'Schedule created successfully', 'schedule_id': schedule.schedule_id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def schedule_update(request: HttpRequest, schedule_id):
    try:
        schedule = models.Schedule.objects.get(schedule_id=schedule_id)
    except models.Schedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        form = forms.ScheduleForm(data, instance=schedule)
        if form.is_valid():
            schedule = form.save()
            return JsonResponse({'message': 'Schedule updated successfully', 'schedule_id': schedule.schedule_id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def schedule_delete(request: HttpRequest, schedule_id):
    try:
        schedule = models.Schedule.objects.get(schedule_id=schedule_id)
        schedule.delete()
        response = {
            'message': 'Schedule deleted successfully'
        }
        return JsonResponse(response)
    except models.Schedule.DoesNotExist:
        raise Http404("Schedule does not exist")
