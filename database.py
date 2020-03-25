from cloudant.client import CouchDB, Cloudant
from cloudant.view import View
from cloudant.design_document import DesignDocument
from requests.exceptions import ConnectionError
from datetime import date
import base64


def establish_connection():
    try:
        #client = CouchDB(base64.b64decode(b'YWRtaW4='),
        #                 base64.b64decode(b'NDc3VGgzNW00NzdUaDFuZzU='),
        #                 url='http://127.0.0.1:5984',
        #                 connect=True)
        client = Cloudant('d07e4fa4-6cda-4497-ad7b-d88d85e87d09-bluemix',
                          'ac3c68b7c1048ced936c802d6d6741a1625bac6ce4ef' +
                          'f8993cd22397129eaeee',
                          url='https://d07e4fa4-6cda-4497-ad7b-d88d85e87d09' +
                          '-bluemix:ac3c68b7c1048ced936c802d6d6741a1625' +
                          'bac6ce4eff8993cd22397129eaeee@d07e4fa4-6cda-4497' +
                          '-ad7b-d88d85e87d09-bluemix.cloudantnosqldb.' +
                          'appdomain.cloud', connect=True)

    except ConnectionError:
        print('Error Connecting to localhost. ' +
              'Will attempt connection to cloud.')
        
    return client


def create_user(username, name, email, password):
    client = establish_connection()
    my_database = client['blog_users']

    data = {
        '_id': username,
        'name': name,
        'email': email,
        'password': password,
        'posts': []
    }

    my_database.create_document(data)
    client.disconnect()


def delete_user(user):
    client = establish_connection()
    my_database = client['blog_users']
    my_document = my_database[user]
    my_document.delete()
    client.disconnect()


def posts_per_user():
    client = establish_connection()
    my_database = client['blog_users']
    ddoc = DesignDocument(my_database, 'Bloggers')
    ddoc.fetch()
    view_list = View(ddoc, 'postsPerUser?group=true',
                     map_func='function(doc) {' +
                     '\n (doc.posts || []).forEach(function(posts) {\n' +
                     'emit(posts.author, 1); \n});\n}',
                     reduce_func='function (keys, values, rereduce) {\n' +
                     'return sum(values); \n}')
    posts = {}
    for view in view_list.result:
        posts[view.get('key')] = view.get('value')
    client.disconnect()
    return posts


def write_post(author, title, content):
    client = establish_connection()
    my_database = client['blog_users']
    my_document = my_database[author]
    posts = []
    if len(my_document['posts']) > 0:
        for post in my_document['posts']:
            posts.append(post)

    post = {
        'title': title,
        'author': author,
        'content': content,
        'date_posted': str(date.today())
    }

    posts.append(post)
    my_document['posts'] = posts
    my_document.save()
    client.disconnect()


def get_posts():
    client = establish_connection()
    my_database = client['blog_users']
    ddoc = DesignDocument(my_database, 'allDocs')
    ddoc.fetch()
    view_list = View(ddoc, 'getAllDocs')

    posts = []
    for view in view_list.result:
        all_posts = view.get('value', 'No Posts')
        for post in all_posts:
            posts.append(post)

    client.disconnect()
    return posts


def get_users():
    client = establish_connection()
    my_database = client['blog_users']
    ddoc = DesignDocument(my_database, 'Bloggers')
    ddoc.fetch()
    view_list = View(ddoc, 'allBloggers')
    users = {}

    for view in view_list.result:
        users[view.get('id')] = view.get('value')

    print(users)
    client.disconnect()
    return users


def get_users_2():
    client = establish_connection()
    my_database = client['blog_users']
    ddoc = DesignDocument(my_database, 'Bloggers')
    ddoc.fetch()
    view_list = View(ddoc, 'allBloggers2')
    users = {}

    for view in view_list.result:
        users[view.get('id')] = view.get('value')

    print(users)
    client.disconnect()
    return users
