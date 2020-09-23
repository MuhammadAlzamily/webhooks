import requests

import schedule


def trump():

    hook_url = ["webhook_token"]

    trump_api = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"

    resp = requests.get(trump_api)

    msg = resp.json()['message']

    icon_url = "https://whatdoestrumpthink.com/api-docs/images/logo.png"

    data = {
        "avatar_url": icon_url,
        "content": msg,
    }

    requests.post(hook_url, data)


def chuck():
    hook_url = ["webhook_token"]

    chuck = "https://api.chucknorris.io/jokes/random"

    resp = requests.get(chuck)

    icon = resp.json()['icon_url']

    joke = resp.json()['value']

    data = {
        "avatar_url": icon,
        "content": joke,
    }

    requests.post(hook_url, data)


# ADD IN THE TIME PERIOD YOU WANT, THIS MODULE IS QUITE EASY
schedule.every(5).seconds.do(trump)

schedule.every(10).seconds.do(chuck)

schedule.run_all()
