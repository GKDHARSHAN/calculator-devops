from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result=None
    if request.method=="POST":
        num1=float(request.form.get("num1",0))
        num2=float(request.form.get("num2",0))
        op=request.form.get("operation")
        if op=="add":
            result=num1+num2
        elif op=="sub":
            result=num1-num2
        elif op=="mul":
            result=num1*num2
        elif op=="div":
            result=num1/num2
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)