import requests


def get_student_token(user: str, password: str):
    return "Authorized"
    url = 'https://sumvirtual.unmsm.edu.pe/sumapi/loguearse'
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip',
        'authorization': 'AUTH TOKEN',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json',
        'Host': 'sumvirtual.unmsm.edu.pe',
        'User-Agent': 'okhttp/4.9.2'
    }
    data = {
        'usuario': user,
        'clave': password
    }
    request = requests.post(url, headers=headers, json=data)
    status = request.status_code
    if status != 200:
        return None
    data = request.json()
    token = data['data'][-1]['token']
    cookies = request.cookies
    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie.name] = cookie.value

    return (token, cookie_dict)
