# API for YaTube
## About this project
API that allows you to view or edit posts, groups, comments in YaTube,
view you subscriptions or subscribe to other authors
## Installation
- Clone the repo</br>
`git clone https://github.com/mosphox/api_final_yatube.git`
- Install packages</br>
`pip install -r requirements.txt`
- Apply migrations</br>
`python manage.py migrate`
- Start server</br>
`python manage.py runserver`
## Examples
### Posts
- Get all posts</br>
`api/v1/posts`
- You can limit the number of posts received by using pagination</br>
`api/v1/posts?limit=2&offset=4`
- Get detail info on any post by it's id</br>
`api/v1/posts/1`
- It is possible to edit posts by sending PUT, PATCH or DELETE requests</br>
`api/v1/posts/1`</br>
### Same rules are applied for group and comments section</br>
- `api/v1/groups`
- `api/v1/posts/1/comments`</br>
### Except groups are readonly</br>
### Subscriptions
- View you subscriptions</br>
`api/v1/follow`
- Is is possible to subscribe to an author by sending his username in POST request</br>
`api/v1/follow`
### Full docs are available on `/redoc` page