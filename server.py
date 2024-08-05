from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


def write_to_file(data):
    with open("datafile.txt", mode="a") as database:
        emails = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{emails}\t,{subject}\t,{message}\t')


def write_to_csv(data):
    with open("datafile.csv", mode="a", newline='') as database2:
        emails = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([emails, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to data"
    else:
        return 'Something went wrong please try again'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/contact.html')
def contact():
    return render_template("contact.html")
@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/')
def work():
    return render_template("work.html")
"""
