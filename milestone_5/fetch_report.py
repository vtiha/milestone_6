import requests, sys

def fetch_report(month, department):

    response = requests.get(f'http://127.0.0.1:5000/birthdays?month={month}&department={department}')

    if response.status_code == 200:
        report = response.json()
        total = report.get('total', 0)
        employees = report.get('employees', [])

        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {total}")
        if total > 0:
            print("Employees:")
            for emp in employees:
                print(f"- {emp['birthday']}, {emp['name']}")
    else:
        print("Failed to fetch report:", response.status_code)

if __name__ == "__main__":
   
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)

    month = sys.argv[1]
    department = sys.argv[2]
    fetch_report(month, department)