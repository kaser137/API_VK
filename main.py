import dotenv
import os
import random
from pathlib import Path
from servicefile import save_wall_image, get_wall_upload_url, fetch_comic, get_latest_comic_num, get_comic_url_comments, publish_wall_image


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    token = os.environ['VK_TOKEN']
    group_id = int(os.environ['VK_GROUP_ID'])
    random_comic_num = random.randint(1, get_latest_comic_num()+1)
    url, comments = get_comic_url_comments(random_comic_num)
    image = fetch_comic(url)
    upload_url = get_wall_upload_url(token, group_id)
    photo_id = save_wall_image(token, group_id, upload_url, image)
    os.remove(image)
    print(publish_wall_image(token, group_id, photo_id, comments))


if __name__ == '__main__':
    main()
