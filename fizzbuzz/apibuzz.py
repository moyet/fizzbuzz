from requests import request


def api_buzz():
    my_url = 'http://127.0.0.1:3000/fizzbuzz/{i}'
    my_range = range(0, 101)

    for fb in my_range:
        req = request('GET', my_url.format(i=fb))
        print(req.json().get('result'))


if __name__ == "__main__":
    api_buzz()
