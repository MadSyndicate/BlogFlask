from flask import Flask, render_template, request, redirect, url_for
import db_operations

app = Flask(__name__)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = db_operations.get_all_blogs()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        print(request.form.get('author'))
        print(request.form.get('title'))
        print(request.form.get('content'))
        # adding to "db", id handled in post_blog-func
        new_blog_post = {
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }
        result = db_operations.post_blog(new_blog_post)
        print(f'Added new blog_post with id "{result}".')
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)