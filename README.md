# blogProject
This project is designed to display, edit and create blog posts

# launch

There are two ways to launch an application:
Makefile and docker.
To use the Makefile, you must have a Unix system. If you don't have required libraries, you must write 'make requirements' in the project folder. After that write 'make' in the project folder.
To use docker for launch just write 'docker-compose up' in the project folder.
The project runs in debug mode for the convenience of checking requests.

# requests and responses
The project supports Django authorization (Users are created through the admin panel).
When user go to the url localhost:8000/api/v1/posts/, a list of all/non-login-required-only posts will be returned to him. The user can add new posts from url localhost:8000/api/v1/posts/create/. When navigating to the url localhost:8000/api/v1/posts/"post slug"/ The user can edit the post, if he created this post.
When user go to the url localhost:8000/api/v1/authors/, localhost:8000/api/v1/categories/ or localhost:8000/api/v1/tags/, he gets list of authors/categories/tags.

# usage

You can to create users, posts, categories and tags from localhost:8000/admin. For that you must to create superuser with command 'python3 manage.py createsuperuser' and go to the url.
