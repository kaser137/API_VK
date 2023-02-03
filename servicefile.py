import requests
from pathlib import Path


def get_latest_comic_num():
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    return response.json()['num']


def get_comic_url_and_comments(comic_num):
    response = requests.get(f'https://xkcd.com/{comic_num}/info.0.json')
    response.raise_for_status()
    response = response.json()
    return response['img'], response['alt']


def fetch_comic(url, payload=None):
    response = requests.get(url, payload)
    response.raise_for_status()
    name_for_comic = Path(url).parts[-1]
    with open(name_for_comic, 'wb') as file:
        file.write(response.content)
    return name_for_comic


def get_wall_upload_url(token, group_id, v=5.131):
    payload = {'v': v, 'access_token': token, 'group_id': group_id}
    response = requests.get('https://api.vk.com/method/photos.getWallUploadServer', params=payload)
    upload_url = response.json()['response']['upload_url']
    return upload_url


def upload_image_to_vk(upload_url, image):
    with open(image, 'rb') as img:
        files = {'photo': img}
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    response = response.json()
    return response['server'], response['photo'], response['hash']


def save_wall_image(token, group_id, upload_url, image, v=5.131):
    img_server, img_photo, img_hash = upload_image_to_vk(upload_url, image)
    payload = {'server': img_server, 'photo': img_photo, 'hash': img_hash, 'v': v, 'access_token': token,
               'group_id': group_id}
    response = requests.post('https://api.vk.com/method/photos.saveWallPhoto', params=payload)
    response.raise_for_status()
    response = response.json()['response'][0]
    photo_id = ''.join(('photo', str(response['owner_id']), '_', str(response['id'])))
    return photo_id


def publish_wall_image(token, group_id, photo_id, comments, v=5.131):
    payload = {'v': v, 'access_token': token, 'attachments': photo_id, 'from_group': 1, 'owner_id': -group_id,
               'message': comments}
    response = requests.post('https://api.vk.com/method/wall.post', params=payload)
    response.raise_for_status()
    return response.json()
