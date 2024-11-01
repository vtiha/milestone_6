from flask import Flask, request
import csv
import json
from datetime import datetime

app = Flask(__name__)

def load_employees(filename):
    employees = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                'id': len(employees) + 1,
                'full_name': row['Full_Name'],
                'hiring_date': row['Hiring_Date'],
                'department': row['Department'],
                'birthday': row['Birthday'],
                'phone_number': row['Phone_Number']
            })
    return employees

employees = load_employees('database.csv')

@app.get('/birthdays')
def get_birthdays():
    month = request.args.get('month', '').lower()
    department = request.args.get('department', '').lower()
    report = {
        "employees": [],
        "total": 0
    }

    for emp in employees:
        emp_department = emp['department'].lower()
        request_department = department.lower()
        

        emp_birthday_month = datetime.strptime(emp['birthday'], '%Y-%m-%d').strftime('%B').lower()

        if emp_department == request_department and emp_birthday_month == month:
            report['employees'].append({
                "id": emp['id'],
                "name": emp['full_name'],
                "birthday": datetime.strptime(emp['birthday'], '%Y-%m-%d').strftime('%b %d')
            })
    
    report['total'] = len(report['employees'])
    response = json.dumps(report, indent=4)
    return response, 200

@app.get('/anniversaries')
def get_anniversaries():
    month = request.args.get('month', '').lower()
    department = request.args.get('department', '').lower()
    report = {
        "employees": [],
        "total": 0
    }

    for emp in employees:
        if emp['department'].lower() == department and datetime.strptime(emp['hiring_date'], '%Y-%m-%d').strftime('%B').lower() == month:
            report['employees'].append({
                "id": emp['id'],
                "name": emp['full_name'],
                "hiring_date": datetime.strptime(emp['hiring_date'], '%Y-%m-%d').strftime('%b %d')  # Форматування дати
            })

    report['total'] = len(report['employees'])

    response = json.dumps(report, indent=4)
    return response, 200

if __name__ == '__main__':
    app.run(port=5000)