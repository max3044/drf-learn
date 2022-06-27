import requests

api = "http://127.0.0.1:8000/seasons/"


def get_detail_view(lookup_val:int):

    url = api + f"{lookup_val}"

    with requests.get(url) as session:

        return session.json()


def get_view():

    url = f"{api}"

    with requests.get(url) as session:
        return session.json()



def post_view(data:dict=dict(title="Somesdf season", slogan="Hi sdfsdf I am some season", number=None)):

    url = f"{api}"

    with requests.post(url, json=data) as session:

        return session.json()

# print(get_detail_view(2))
print(post_view({"title":"hello world 3!"}))