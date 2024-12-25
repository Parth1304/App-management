from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<App {self.app_name}>"

# Create the database
with app.app_context():
    db.create_all()
    
@app.route('/add-app', methods=['POST'])
def add_apps():
    data = request.get_json()

    added_apps = []
    for app_data in data:
        
        if 'app_name' not in app_data or 'version' not in app_data or 'description' not in app_data:
            abort(400, description="Missing required fields: app_name, version, or description")

        app = App(app_name=app_data['app_name'], version=app_data['version'], description=app_data['description'])
        db.session.add(app)
        db.session.commit()

        added_apps.append({'id': app.id, 'app': {'app_name': app.app_name, 'version': app.version, 'description': app.description}})

    return jsonify(added_apps), 201
   


@app.route('/get-app/<int:app_id>', methods=['GET'])
def get_app(app_id):
    app = App.query.get(app_id)
    if not app:
        abort(404, description="App not found")
    return jsonify({'id': app.id, 'app': {'app_name': app.app_name, 'version': app.version, 'description': app.description}})


@app.route('/delete-app/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    app = App.query.get(app_id)
    if not app:
        abort(404, description="App not found")
    
    db.session.delete(app)  
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
