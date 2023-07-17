from flask import Blueprint, render_template, request, json, Response

from application.models.user_model import User
# from application import app

user_bp = Blueprint("user", __name__)

# @user_bp.route('/mongodb', methods=['GET'])
# def mongo_read():
#     data = request.json
#     if data is None or data == {}:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = User(data)
#     response = obj1.read()
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')

@user_bp.route('/read', methods=['GET'])
def mongo_read():
    obj1 = User()
    documents = obj1.read()
    # return Response(response=json.dumps(response),
    #                 status=200,
    #                 mimetype='application/json')
    return render_template('users.html', documents=documents)



# @user_bp.route('/mongodb', methods=['POST'])
# def mongo_write():
#     data = request.json
#     if data is None or data == {} or 'Document' not in data:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = User(data)
#     response = obj1.write(data)
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')


@user_bp.route('/create', methods=['GET', 'POST'])
def write_controller():
    if request.method == 'POST':
        data = request.get_json()
        if data is None or data == {}:
            return Response(response=json.dumps({"Error": "Please provide information"}),
                            status=400,
                            mimetype='application/json')
        obj = User(data)
        response = obj.write(data)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')
    elif request.method == 'GET':
        return render_template('create.html')

# @user_bp.route('/update/<document_id>', methods=['PUT'])
# def mongo_update():
#     data = request.json
#     if data is None or data == {}:
#         return Response(response=json.dumps({"Error": "Please provide information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = User(data)
#     response = obj1.update()
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')


# @user_bp.route('/update/<document_id>', methods=['POST', 'PUT'])
# def update(document_id):
#     user_model = User()
#     user = user_model.get_user_by_id(document_id)
#     if user:
#         if request.method == 'PUT' or request.form.get('_method') == 'PUT':
#             # Obtener los datos del formulario
#             first_name = request.form.get('first_name', user.get('first_name'))
#             last_name = request.form.get('last_name', user.get('last_name'))
#             age = request.form.get('age', user.get('age'))

#             # Verificar si se realizaron cambios
#             if first_name != user.get('first_name') or last_name != user.get('last_name') or age != user.get('age'):
#                 data = {
#                     'first_name': first_name,
#                     'last_name': last_name,
#                     'age': age
#                 }
#                 if user_model.update(document_id, data):
#                     return 'Usuario actualizado correctamente'
#                 else:
#                     return 'No se encontró el usuario o no se realizó ninguna actualización'
#             else:
#                 return 'No se realizaron cambios en el usuario'
#         else:
#             return render_template('update.html', user=user)
#     else:
#         return 'Usuario no encontrado'


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
                    return 'Usuario actualizado correctamente'
                else:
                    return 'No se encontró el usuario o no se realizó ninguna actualización'
            else:
                return 'No se realizaron cambios en el usuario'
        else:
            return render_template('update.html', user=user)
    else:
        return 'Usuario no encontrado'


# @user_bp.route('/delete', methods=['DELETE'])
# def mongo_delete():
#     data = request.json
#     if data is None or data == {} or 'Filter' not in data:
#         return Response(response=json.dumps({"Error": "Please provide connection information"}),
#                         status=400,
#                         mimetype='application/json')
#     obj1 = User(data)
#     response = obj1.delete(data)
#     return Response(response=json.dumps(response),
#                     status=200,
#                     mimetype='application/json')

@user_bp.route('/delete/<document_id>', methods=['POST', 'DELETE'])
def mongo_delete(document_id):
    # id = request.view_args['document_id']
    if request.method == 'DELETE' or request.form.get('_method') == 'DELETE':
        if document_id is None:
            return Response(response=json.dumps({"Error": "Please provide connection information"}),
                            status=400,
                            mimetype='application/json')
        obj1 = User()
        response = obj1.delete(document_id)
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype='application/json')
    else:
        return Response(response=json.dumps({"Error": "NANI"}),
                        status=400,
                        mimetype='application/json')
