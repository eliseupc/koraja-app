from flask import Flask, render_template, request
import requests
import math
import json

app = Flask(__name__)

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
PAGE_SIZE = 10

FILTER_TERMS = {
    'all': 'parque pista de corrida trilha espaço verde pista atlética',
    'parque': 'parque parque público área verde',
    'pista': 'pista de corrida pista atlética pista esportiva',
    'trilha': 'trilha de corrida trilha para correr rota de trilha',
    'verde': 'parque árvore área verde jardim',
}

SORT_OPTIONS = ('relevance', 'name')

@app.route('/')
def index():
    return render_template(
        'index.html',
        query='',
        location='',
        filter_type='all',
        sort_by='relevance',
        page=1,
        results_count=None,
        total_pages=1,
        places=[],
        places_json='[]',
        search_message='',
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


def build_search_queries(query, location, filter_type='all'):
    filters = FILTER_TERMS.get(filter_type, FILTER_TERMS['all'])
    candidates = []

    if query and location:
        candidates.append(f"{query} {location} {filters}")
        candidates.append(f"{query} {location}")
        candidates.append(f"{location} {filters}")
        candidates.append(f"{query} {filters}")
        candidates.append(query)
        candidates.append(location)
    elif query:
        candidates.append(f"{query} {filters}")
        candidates.append(query)
    else:
        candidates.append(f"{location} {filters}")
        candidates.append(location)

    return [q.strip() for q in candidates if q.strip()]


def search_nominatim(q):
    params = {
        'q': q,
        'format': 'json',
        'addressdetails': 1,
        'limit': 60,
    }
    response = requests.get(NOMINATIM_URL, params=params, headers={
        'User-Agent': 'FlaskRunningMapApp/1.0',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8'
    }, timeout=15)
    response.raise_for_status()
    return response.json()


@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    location = request.args.get('location', '').strip()
    filter_type = request.args.get('filter_type', 'all')
    sort_by = request.args.get('sort_by', 'relevance')
    page = request.args.get('page', '1')

    try:
        page = max(1, int(page))
    except ValueError:
        page = 1

    places = []
    results_count = None
    total_pages = 1
    search_message = ''
    active_filter = filter_type if filter_type in FILTER_TERMS else 'all'
    active_sort = sort_by if sort_by in SORT_OPTIONS else 'relevance'

    if query or location:
        queries = build_search_queries(query, location, active_filter)
        results = []
        for q in queries:
            results = search_nominatim(q)
            if results:
                break

        if results:
            extracted = []
            for item in results:
                extracted.append({
                    'name': item.get('display_name', 'Local desconhecido'),
                    'lat': item.get('lat'),
                    'lon': item.get('lon'),
                    'type': item.get('type', ''),
                    'category': item.get('class', ''),
                    'address': item.get('address', {}),
                })
            if active_sort == 'name':
                extracted.sort(key=lambda item: item['name'])

            results_count = len(extracted)
            total_pages = max(1, math.ceil(results_count / PAGE_SIZE))
            if page > total_pages:
                page = total_pages
            start = (page - 1) * PAGE_SIZE
            places = extracted[start:start + PAGE_SIZE]
            if not places and results_count > 0:
                search_message = 'Nenhuma local nesta página. Use outra página ou ajuste o filtro.'
        else:
            results_count = 0
            total_pages = 1
            search_message = 'Nenhum local encontrado. Tente outros termos, bairro ou filtro.'

    return render_template(
        'index.html',
        query=query,
        location=location,
        filter_type=active_filter,
        sort_by=active_sort,
        page=page,
        results_count=results_count,
        total_pages=total_pages,
        places=places,
        places_json=json.dumps(places, ensure_ascii=False),
        search_message=search_message,
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
