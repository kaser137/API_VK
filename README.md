# Publishing comics

## What is this?

This project gets a random comic from https://xkcd.com/, and then publishes it on the wall of group in VK.

## How it works?

For working with this project, you have to copy all files in the working directory at your choice.  Create in working 
directory subdirectory "venv" and file ".env" in this subdirectory. In this file, you have to write 2 lines like this:
```python
VK_TOKEN='vk8.j.E5dLbA_4Ttpr2NW6sUds84HSOhgnFeSdsMeBY0nqZQ3mod0uM00x8-NE0QPqTxnmG_2j0IqUKKL3DyUNWYS6_IU4kKuR9Vp8uCl-tPmyZJtsw7a9j8tVjp0ZwtnINvg5-zDtTmYkShktlwzhr5cBuDZxuwPVRBfRsboua7fjlo6FKIYXj7WmBOYEkIhRGaeS1lrmr_AGfnBpb583im4R8Q'
VK_GROUP_ID=119537563
```
(presented values are not correct, it's just for example).

Where VK_TOKEN is your token for API VK, VK_GROUP_ID is your ID of your group in VK, token you can get 
[here](https://vk.com/dev.php?method=implicit_flow_user), group_id you can get at this [address](https://regvk.com/id/).

Python3 should  already be installed. Then use pip (or pip3, if there is a conflict with Python2) to install
dependencies: `
```commandline
pip install -r requirements.txt
```
Start file `main.py`, if all good, you will see string like that: 
>{'response': {'post_id': 37}}

It means that random comic is published at the wall of your group. You can also check it, just visit your group.


Код написан в образовательных целях на курсах для веб-разработчиков [dvmn.org](https://dvmn.org/).
