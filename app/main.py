from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method=='POST':
        name=request.form.get('name')
    return render_template('result.html',name=name)

#if __name__ == '__main__':
#    app.run()

if __name__ == '__main__':
    app.run(debug=True, host='0.0', port=80)
    # app.run(debug=True, host='0.0.0.0', port=8000)