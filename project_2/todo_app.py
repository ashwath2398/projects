from flask import Flask, render_template, request

app = Flask(__name__)

# Sample to-do list (replace with database or persistence mechanism for a more robust app)
todo_list = []

@app.route("/")
def home():
  return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
  new_todo = request.form.get("new_todo")
  if new_todo:
    todo_list.append(new_todo)
  return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
  app.run(debug=True)

