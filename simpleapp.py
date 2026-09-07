from flask import Flask, render_template, Request, request, jsonify
#create a simple flask app
app = Flask(__name__)
@app.route("/", methods=["GET"])
def welcome():
    return "welcome here to idk"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome here to index page</h2>"
#varaiable rule
@app.route("/success/<int:score>")#by default it is GET method #int is variable rule
def success(score):
    return"the person has passed and the socre is:" + str(score)
@app.route("/fail/<int:score>")#by default it is GET method #int is variable rule
def fail(score):
    return"the person has failed and the socre is:" + str(score)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        return render_template('form.html', score=average_marks)

        
@app.route('/api', methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_value=float(dict(data)['a'])
    b_value=float(dict(data)['b'])
    return jsonify(a_value+b_value)
if __name__ == '__main__':
    app.run(debug=True)
