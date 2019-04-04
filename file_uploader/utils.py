import pandas as pd
from django.core.files.storage import FileSystemStorage
import json

#recibo la ruta al archivo
def csv_to_geojson(csv):
    data_frame = pd.read_csv(csv)
    json_result_string = data_frame.to_json(
        orient='records',
        double_precision=6,
        date_format='iso'
    )
    json_result = json.loads(json_result_string)
    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }
    for record in json_result:
        geojson['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [record['latitude'], record['longitude']],
            },
            'properties': record,
        })
    return geojson