from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.employees import create_employee, get_all_employees, update_employee, delete_employee


def add_employee():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    department = data.get('department')

    if not first_name or not last_name or not email or not phone or not department:
        return jsonify({'message': 'Missing required fields'}), 400

    create_employee(first_name, last_name, email, phone, department)
    return jsonify({'message': 'Employee added successfully'}), 201

def view_employees():
    employees = get_all_employees()
    return jsonify({'employees': employees}), 200

def update_employee_route(id):
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    department = data.get('department')

    update_employee(id, first_name, last_name, email, phone, department)
    return jsonify({'message': 'Employee updated successfully'}), 200

def delete_employee_route(id):
    delete_employee(id)
    return jsonify({'message': 'Employee deleted successfully'}), 200