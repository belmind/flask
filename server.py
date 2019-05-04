from flask import Flask, request, url_for, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos.get(todo_id, 1)}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

@app.route('/') 
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

with app.test_request_context():
    url_for('static', filename='style.css')

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True) 