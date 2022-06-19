import requests, json

Req_URL = "http://localhost:8098/buckets/s25876/keys/"

def get_result_from_request(request):
    body = None
    try:
        body = request.json()
    except:
        body = request.text

    return json.dumps({ "status": request.status_code, "body": body })

def get(key):
    request = requests.get(Req_URL + key, stream=True)
    return get_result_from_request(request)

def put(key, body):
    request = requests.put(Req_URL + key, json = body)
    return get_result_from_request(request)

def delete(key):
    request = requests.delete(Req_URL + key)
    return get_result_from_request(request)

def start():
    example_key = "ChelseaLondyn"
    example_body = { "footballteam": "ChelseaLondyn", "year": 1954, "players": ["Drogba", "Cech", "Terry"], "winChampionsleage": "true"}

    # tworzenie dokumentu
    request_put = put(example_key, example_body)
    print("TWORZENIE DOKUMENTU\nKlucz: " + example_key + "\nDokument: " + json.dumps(example_body) + "\nWynik:\n" + request_put, end = "\n\n")


    # pobieranie dokumentu
    request_get = get(example_key)
    print("POBIERANIE DOKUMENTU\nKlucz: " + example_key + "\nWynik:\n" + request_get, end = "\n\n")

    # aktualizacja dokumentu
    example_body["year"] = 2002
    request_put_new = put(example_key, example_body)
    print("AKTUALIZACJA DOKUMENTU\nKlucz: " + example_key + "\nDokument: " + json.dumps(example_body) + "\nWynik:\n" + request_put_new, end = "\n\n")

    # pobieranie zaktualizowanego dokumentu
    request_get_new = get(example_key)
    print("POBIERANIE ZAKTUALIZOWANEGO DOKUMENTU\nKlucz: " + example_key + "\nWynik:\n" + request_get_new, end = "\n\n")

    # usuwanie dokumentu
    request_delete = delete(example_key)
    print("USUWANIE DOKUMENTU\nKlucz: " + example_key + "\nWynik:\n" + request_delete, end = "\n\n")

    # pobieranie usunietego dokumentu
    request_get_deleted = get(example_key)
    print("POBIERANIE USUNIETEGO DOKUMNETU\nKlucz: " + example_key + "\nWynik:\n" + request_get_deleted, end = "\n\n")


start()