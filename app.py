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


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = db_operations.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
    # Update the post in the JSON file
    # Redirect back to index

        upd_author = request.form.get('author')
        upd_title = request.form.get('title')
        upd_content = request.form.get('content')
        result = db_operations.update_post(post_id, upd_author, upd_title, upd_content)
        print(f'Updated blog_post with id "{result}".')
        return redirect(url_for('index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Find the blog post with the given id and remove it from the list
    # Redirect back to the home page
    db_operations.delete_post(post_id)
    print(f'Deleted post with id "{post_id}".')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)