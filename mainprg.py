from CRUD_OPERATION import *
from flask import *
app=Flask(__name__)

@app.route('/')
def openhomepage():
    return render_template('home.html')
@app.route('/studentreg')
def openstudentregistration():
    return render_template('studentreg.html')
@app.route('/savetostudentTable',methods=['POST','GET'])
def savedetailes():
    if request.method=='POST':
        a=int(request.form['sid'])
        b=request.form['sname']
        c=request.form['sphone']
        d=request.form['saddress']
        e= request.form['sdate']
        f=request.form['sdateofjoin']
        print(a,b,c,d,e,f)
        try:
            insertstudent(a,b,c,d,e,f)
            msg="successfully inserted"
        except:
            msg="Not successful inserted"

    return render_template('result.html',msg=msg)
@app.route("/allstudent")
def openallstudent():
    rows=readallstudent()
    print(rows)
    return render_template('allstudentt.html',rows=rows)
@app.route("/<id>/deletestudent")
def deletesinglestudent(id):#we cannot use same as the crud operation
    print(id)
    msg=deletestudent(id)
    return render_template('result.html',msg=msg)
@app.route("/<id>/editstudent")
def updatesinglestudent(id):
    print(id)
    rows=readsinglestudent(id)
    print(rows)
    return render_template('editstudent.html',rows=rows)
@app.route('/updatetostudenttable',methods=['POST','GET'])
def updatedetailes():
    if request.method=='POST':
        a=int(request.form['sid'])
        b=request.form['sname']
        c=request.form['sphone']
        d=request.form['saddress']
        e= request.form['sdate']
        f=request.form['sdateofjoin']
        print(a,b,c,d,e,f)
        try:
            updatestudent(a,b,c,d,e,f)
            msg="successfully updated"
        except:
            msg="Not successful updated"

    return render_template('result.html',msg=msg)

if __name__=='__main__':
    app.run(port=2024)
