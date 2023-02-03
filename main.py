import dotenv
import os
import random
from pathlib import Path
from servicefile import save_wall_image
from servicefile import get_wall_upload_url
from servicefile import fetch_comic
from servicefile import get_latest_comic_num
from servicefile import get_comic_url_and_comments
from servicefile import publish_wall_image


def main():
    try:
        dotenv.load_dotenv(Path('venv', '.env'))
        token = os.environ['VK_TOKEN']
        group_id = int(os.environ['VK_GROUP_ID'])
        random_comic_num = random.randint(1, get_latest_comic_num()+1)
        url, comments = get_comic_url_and_comments(random_comic_num)
        image_name = fetch_comic(url)
        upload_url = get_wall_upload_url(token, group_id)
        photo_id = save_wall_image(token, group_id, upload_url, image_name)
        print(publish_wall_image(token, group_id, photo_id, comments))
    finally:
        os.remove(image_name)


if __name__ == '__main__':
    main()
