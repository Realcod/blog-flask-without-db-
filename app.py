from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for posts
posts = []

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if title and content:
            posts.append({"id": len(posts) + 1, "title": title, "content": content})
            return redirect(url_for("home"))
    return render_template("create.html")

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    post = next((post for post in posts if post["id"] == id), None)
    if not post:
        return "Post not found", 404
    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]
        return redirect(url_for("home"))
    return render_template("update.html", post=post)

@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    global posts
    posts = [post for post in posts if post["id"] != id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
