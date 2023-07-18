from flask import Blueprint, render_template, request, json, Response, redirect, url_for, flash

from application.models.user_model import User

user_bp = Blueprint("user", __name__)

@user_bp.route('/read', methods=['GET'])
def read():
    obj1 = User()
    documents = obj1.read()
    return render_template('users.html', documents=documents)

@user_bp.route('/create', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        data = request.get_json()
        if data is None or data == {}:
            return Response(response=json.dumps({"Error": "Please provide information"}),
                            status=400,
                            mimetype='application/json')
        obj = User(data)
        obj.write(data)
        # flash(response)
        # return redirect(url_for("user.read"))
        return Response(response=json.dumps({"Ok": "User Added"}),
                            status=200,
                            mimetype='application/json')

    elif request.method == 'GET':
        return render_template('create.html')

@user_bp.route('/update/<document_id>', methods=['GET', 'POST', 'PUT'])
def update(document_id):
    user_model = User()
    user = user_model.get_user_by_id(document_id)
    if user:
        if request.method == 'POST' or request.form.get('_method') == 'PUT':
            # data = request.get_json()
            first_name = request.form.get('first_name', user.get('first_name'))
            last_name = request.form.get('last_name', user.get('last_name'))
            age = request.form.get('age', user.get('age'))

            if first_name != user.get('first_name') or last_name != user.get('last_name') or age != user.get('age'):
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'age': age
                }
                if user_model.update(document_id, data):
                    # flash("Usuario Actualizado")
                    return redirect(url_for("user.read"))
                else:
                    return redirect(url_for("user.read"))
            else:
                return redirect(url_for("user.read"))

        else:
            return render_template('update.html', user=user)
    else:
        return Response(response=json.dumps({"Error": "User not found"}),
                            status=400,
                            mimetype='application/json')

@user_bp.route('/delete/<document_id>', methods=['POST', 'DELETE'])
def delete(document_id):
    if request.method == 'DELETE' or request.form.get('_method') == 'DELETE':
        if document_id is None:
            return Response(response=json.dumps({"Error": "Please provide connection information"}),
                            status=400,
                            mimetype='application/json')
        obj1 = User()
        obj1.delete(document_id)
        # flash(response)
        return redirect(url_for("user.read"))
    else:
        return Response(response=json.dumps({"Error": "Error when deleating"}),
                        status=400,
                        mimetype='application/json')
