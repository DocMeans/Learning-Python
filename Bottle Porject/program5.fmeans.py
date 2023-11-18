from bottle import route, run, request, response, template
import data_methods
import uuid


@route("/", method="GET")
def index():
    return template("sign_in")


@route("/login", method="POST")
def login():
    username = request.forms.get("username")
    password = request.forms.get("password")

    if data_methods.validate(username, password):  # validate against database
        cookie_val = str(uuid.uuid4())
        response.set_cookie("COOKIE", cookie_val + "|" + username)  # set a cookie

        data = {"title": "Welcome", "user": username}
        # return template("landing_page")  # list of nav links
        return template("landing_page", data)

    else:
        m = {"msg": "login Failed"}
        return template("status", m)


@route("/add_trip", method=["GET", "POST"])
def add_trip():
    if request.method == "GET":
        return template("add_trip")
    else:
        user = request.forms.get("user")
        date = request.forms.get("date")
        dest = request.forms.get("dest")
        miles = request.forms.get("miles")
        gallons = request.forms.get("gallons")

        try:
            data = (None, user, date, dest, miles, gallons)
            data_methods.add_new_trip(data)
            m = {"msg": "Successfully added trip"}
            return template("status", m)

        except:
            m = {"msg": "Failed to add trip"}
            return template("status", m)


@route("/show_trips", method="GET")
def show_trips():
    current_user = request.get_cookie("COOKIE")  # Get the current user from the cookie
    if current_user:
        current_user = current_user.split("|")[1]  # Extract username

    if not current_user:
        m = {"msg": "Invalid username"}
        return template("status", m)

    sql = "SELECT * FROM trips WHERE username = ?"
    rows = data_methods.show_trips_data(sql, current_user)

    if rows:
        data = {"rows": rows}
        return template("show_trips", data)
    else:
        m = {"msg": f"No trips found for user {current_user}"}
        return template("status", m)


run(host="localhost", port="8080", reloader=True)
