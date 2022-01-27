import requests


def test_get(url):
    r = requests.get(url)
    r.raise_for_status()
    assert r.text.startswith("received GET request")


def test_post(url):
    r = requests.post(url, data='a=1')
    r.raise_for_status()
    assert r.text == "received POST request: a=1\n" \
                     "db.txt content: [a=1]\n"
