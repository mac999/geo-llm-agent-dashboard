import random, pandas as pd
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import IoT_model_from_file
from .geo_llm import text_to_geo_code
from django.conf import settings

def update_column_data():
    column_data = [
        { "label": "ACC", "y": random.randint(10000, 150000), "color": 'red' },
        { "label": "TEMP", "y": random.randint(50000, 100000), "color": 'blue'  },
        { "label": "ICV", "y": random.randint(100000, 150000), "color": 'green'  },
        { "label": "RUT", "y": random.randint(150000, 200000), "color": 'yellow'  },
        { "label": "STRAIN", "y": random.randint(200000, 250000), "color": 'orange'  },
        { "label": "LOAD", "y": random.randint(100000, 200000), "color": 'purple'  }
    ]
    return column_data

def save_static_model_file():
    file_path = os.path.join(settings.BASE_DIR, 'static', 'uploads', f.name)
    with open(file_path, 'wb+') as destination:
        destination.write('test')

def text_to_code(request):
    query_text = request.GET.get('query')
    code = text_to_geo_code(query_text)
    return code

def index(request):
    fetch_type = request.GET.get('fetch_type')
    if fetch_type == 'column':
        column_data = update_column_data()
        return JsonResponse(column_data, safe=False)
    if fetch_type == 'text_to_code':
        code = text_to_code(request)
        return JsonResponse(code, safe=False)

    iot_data = IoT_model_from_file()
    for row in iot_data:
        row['x'] = pd.to_datetime(row['time']).timestamp() * 1000  # Convert to JavaScript timestamp
        row['y'] = [row['open'], row['high'], row['low'], row['close']]

    column_data = update_column_data()
    pie_data = [
        { "y": 12.21, "name": "Blue", "color": "#007bff" },
        { "y": 15.58, "name": "Red", "color": "#dc3545" },
        { "y": 11.25, "name": "Yellow", "color": "#ffea00" },
        { "y": 8.32, "name": "Green", "color": "#28a745" }
    ]
    return render(request, 'index.html', { "iot_data" : iot_data, "column_data": column_data, "pie_data": pie_data })

def scan_view(request):
    return render(request, 'scan_view.html')

def flow_view(request):
    return render(request, 'flow_view.html')