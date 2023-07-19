from flask import Flask, render_template, request, flash
from sql_queries import*


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    posts = get_posts()
    category_list = get_categorys()
    return render_template("index.html", category_list = category_list, posts = posts)
    

@app.route("/category/<id>")
def category(id):
    posts = get_category_post(id)
    category_list = get_categorys()
    category = get_category_name(id)[1].upper()
    return render_template("category_posts.html", category_list = get_categorys(), posts = posts)

@app.route("/post/<post_id>")
def post(post_id):
    post = get_post(post_id)
    category_list = get_categorys()
    return render_template("post.html",category_list = get_categorys(), post=post)




if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""