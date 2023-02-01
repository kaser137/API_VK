import random
import time
import requests
import os
from pathlib import Path


def request_api(url, payload=None, attempt_timeout=10):
    flag = True
    while flag:
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            flag = False
            return response
        except requests.exceptions.ConnectionError or requests.exceptions.Timeout:
            print(f'connection failed, next attempt in {attempt_timeout} seconds')
            time.sleep(attempt_timeout)


def grab_img(url, name_for_img, payload=None):
    response = request_api(url, payload)
    with open(name_for_img, 'wb') as file:
        file.write(response.content)


def get_latest_comic():
    return request_api('https://xkcd.com/info.0.json').json()['num']


def get_random_comic():
    random_comic = random.randint(1, get_latest_comic() + 1)
    response = request_api(f'https://xkcd.com/{random_comic}/info.0.json').json()
    grab_img(response['img'], Path(response['img']).parts[-1])
    return Path(response['img']).parts[-1], response['alt']


def get_wall_upload_url(token, group_id, v=5.131):
    payload = {'v': v, 'access_token': token, 'group_id': group_id}
    response = request_api('https://api.vk.com/method/photos.getWallUploadServer', payload)
    upload_url = response.json()['response']['upload_url']
    return upload_url


def transfer_image(token, group_id, image):
    upload_url = get_wall_upload_url(token, group_id)
    with open(image, 'rb') as img:
        files = {'photo': img}
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        answer = response.json()
    return answer['server'], answer['photo'], answer['hash']


def save_wall_image(token, group_id, image, v=5.131):
    img_server, img_photo, img_hash = transfer_image(token, group_id, image)
    payload = {'server': img_server, 'photo': img_photo, 'hash': img_hash, 'v': v, 'access_token': token,
               'group_id': group_id}
    response = requests.post('https://api.vk.com/method/photos.saveWallPhoto', params=payload)
    response.raise_for_status()
    answer = response.json()['response'][0]
    photo = ''.join(('photo', str(answer['owner_id']), '_', str(answer['id'])))
    return photo


def publish_wall_image(token, group_id, v=5.131):
    image, comments = get_random_comic()
    photo = save_wall_image(token, group_id, image)
    payload = {'v': v, 'access_token': token, 'attachments': photo, 'from_group': 1, 'owner_id': -group_id,
               'message': comments}
    response = requests.post('https://api.vk.com/method/wall.post', params=payload)
    response.raise_for_status()
    os.remove(image)
    return response.json()
