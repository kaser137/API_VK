import dotenv
import os
from pathlib import Path
from servicefile import publish_wall_image


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    token = os.environ['VK_TOKEN']
    group_id = int(os.environ['VK_GROUP_ID'])
    print(publish_wall_image(token, group_id))


if __name__ == '__main__':
    main()
