from bottle import route, run, request, template
import sqlite3 as db


@route("/", method="GET")
def index():
    return template("welcome")


@route("/getDepartment", method=["GET", "POST"])
def department():
    if request.method == "GET":
        return template("dept_form")

    else:
        dept = request.forms.get("dept")  # store the selection in this variable

        try:
            conn = db.connect("payroll.db")
            cur = conn.cursor()

            # Get information for page
            sql = """SELECT employees.emp_id, emp_name, wage, hrs_worked 
                    FROM employees
                    JOIN pay_data ON pay_data.emp_id = employees.emp_id
                    WHERE employees.department = ?"""

            cur.execute(sql, (dept,))
            rows = cur.fetchall()
            cur.close()

            hrs = 0
            wage = 0

            if rows:
                dataList = []

                for row in rows:
                    eid, name, wage, hrs = row  # unpacking the tuple

                    if hrs <= 40:
                        payout = wage * hrs

                    else:
                        ot_pay = (hrs - 40) * 1.5 * wage
                        payout = (wage * 40) + ot_pay
                    emp = (eid, name, wage, hrs, round(payout, 2))
                    dataList.append(emp)

                data = {"dept": dept, "rows": dataList}
                return template("show_department", data)

            else:
                m = {"msg": "No data found for the selected department"}
                return template("status", m)

        except db.Error as e:
            print("Error:", e)
            m = {"msg": "Something went wrong"}
            return template("status", m)


@route("/editHours", method=["GET", "POST"])
def edit_hours():
    if request.method == "GET":
        return template("edit_hours")
    else:
        eid = request.forms.get("eid")
        hrs = request.forms.get("hrs")

        try:
            conn = db.connect("payroll.db")
            cur = conn.cursor()

            # Update the hours worked for a specific employee
            sql_update = """UPDATE pay_data
                            SET hrs_worked = ?
                            WHERE emp_id = ?"""
            data_update = (hrs, eid)
            cur.execute(sql_update, data_update)

            # Get employee name and department information for template
            sql_select = """SELECT emp_name, department
                            FROM employees
                            WHERE emp_id = ?"""
            cur.execute(sql_select, (eid,))
            result = cur.fetchone()

            if result:
                name, department = result
                conn.commit()
                conn.close()

                data = {"eid": eid, "name": name, "department": department}
                return template("get_hours", data)
            else:
                conn.rollback()
                conn.close()
                m = {"msg": "Employee not found"}
                return template("status", m)

        except db.Error as e:
            print("Error:", e)
            m = {"msg": "Failed to update table"}
            return template("status", m)


run(host="localhost", port=8080, reloader=True)
