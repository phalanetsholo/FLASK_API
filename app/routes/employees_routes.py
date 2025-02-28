from flask import Blueprint
from app.controllers.employees_contoller import add_employee, view_employees, update_employee_route, delete_employee_route

employee_bp = Blueprint('employee', __name__)

employee_bp.route('/view', methods=['GET'])(view_employees)
employee_bp.route('/add', methods=['POST'])(add_employee)
employee_bp.route('/update/<int:id>', methods=['PUT'])(update_employee_route)
employee_bp.route('/delete/<int:id>', methods=['DELETE'])(delete_employee_route)