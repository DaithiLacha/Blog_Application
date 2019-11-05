from flask import Flask, render_template, url_for, flash, redirect
from forms import CreateUser, WritePost, DeleteUser
from database import create_user, get_posts, write_post, get_users_2
from database import posts_per_user, get_users, delete_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c5c30923acaa4750cc952dc26ccc009b'


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', posts=get_posts())


@app.route('/stats')
def stats():
    return render_template('stats.html', title='About', stats=posts_per_user())


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = CreateUser()
    if form.validate_on_submit():
        create_user(form.username.data, form.name.data,
                    form.email.data, form.password.data)
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('create_user.html', title='Create User', form=form)


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = WritePost()
    users = get_users_2()
    form.username.choices = []
    for key, value in users.items():
        form.username.choices += [(key, value)]
    if form.validate_on_submit():
        write_post(form.username.data, form.title.data, form.content.data)
        return redirect(url_for('home'))
    return render_template('write_post.html', title='Write Post', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteUser()
    users = get_users_2()
    form.user.choices = []
    for key, value in users.items():
        form.user.choices += [(key, value)]
    if form.validate_on_submit():
        delete_user(form.user.data)
        return redirect(url_for('home'))
    return render_template('delete_user.html', title='Delete User',
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
