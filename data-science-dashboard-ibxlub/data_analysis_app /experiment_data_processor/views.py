from django.shortcuts import render, redirect
import csv, io
from .models import Experiment
from django.db.models import Avg
from django.http import JsonResponse

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        dataset = csv_file.read().decode('utf-8')
        io_string = io.StringIO(dataset)
        next(io_string)  # Skip the header
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = Experiment.objects.update_or_create(
                name=column[0],
                date=column[1],
                observation_type=column[2],
                value=float(column[3])
            )
        return redirect('display_data')  # Redirect to the display_data URL
    return render(request, 'experiment_data_processor/upload_csv.html')

def display_data(request):
    data = calculate_average_value()
    formatted_data = []
    for experiment_name, observations in data.items():
        for observation_type, values in observations.items():
            formatted_data.append({
                'name': experiment_name,
                'date': values['date'],  # Add date if available
                'observation_type': observation_type,
                'avg_value': values['average_value']
            })
    return render(request, 'experiment_data_processor/display_data.html', {'data': formatted_data})


def calculate_average_value():
    data = {}
    experiments = Experiment.objects.all()
    for experiment in experiments:
        name = experiment.name
        observation_type = experiment.observation_type
        value = experiment.value
        date = experiment.date  # Add date if available
        if name in data:
            if observation_type in data[name]:
                data[name][observation_type]['total_value'] += value
                data[name][observation_type]['count'] += 1
            else:
                data[name][observation_type] = {'total_value': value, 'count': 1, 'date': date}
        else:
            data[name] = {observation_type: {'total_value': value, 'count': 1, 'date': date}}
    
    for name, observations in data.items():
        for observation_type, values in observations.items():
            total_value = values['total_value']
            count = values['count']
            average_value = total_value / count
            data[name][observation_type]['average_value'] = average_value
    
    return data


def get_data(request):
    # Placeholder function, you need to implement your logic to retrieve data
    data = {}  # Placeholder for data retrieval logic
    return JsonResponse(data)
