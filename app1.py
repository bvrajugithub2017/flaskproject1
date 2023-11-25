from flask import Flask, render_template, request, redirect

from models.todoModel import db
from models.todoModel import Todo

app = Flask(__name__)

#mention the database software
# configure the SQLite database, relative to the app instance
#That is a connection string that tells SQLAlchemy what database to connect to.
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://rajnikanth1:reno@localhost/oppoDb2"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:datapro2019@localhost:5432/oppoDb3"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://bvraju2023:lG6TJhuwglA6s4H9PSPFaWFMATH2Opay@dpg-clg96cv14gps73b10uvg-a.singapore-postgres.render.com/oppodb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #just to avoid warnings

db.init_app(app)

with app.app_context():
    db.create_all() #creates all the tables

@app.route("/" , methods=['GET', 'POST'])
def myGetData():
    #if data is submitted
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(title=title, desc=desc)   
        #recall that tid is autoincrement and created_on_date is current time by default
        
        db.session.add(todo)
        db.session.commit()

    #irrespective of data is submitted
    allTodo = Todo.query.all() 
    return render_template('home.html', allTodo=allTodo)

@app.route('/update/<int:tid>', methods=['GET', 'POST'])
def update(tid):
    if request.method=='POST': #if submit button is clicked on the Update form
        title = request.form['title']
        desc = request.form['desc']

        #retrive the existing record
        todo = Todo.query.filter_by(tid=tid).first()
        # This line queries the database using SQLAlchemy. 
        # The first() method retrieves the first result found or None if there's no match.

        #assign with the new values
        todo.title = title
        todo.desc = desc
        
        db.session.add(todo)  #update the database
        db.session.commit()
        return redirect("/") #after updating display the home page
        
    # if Update button hyperlink is clicked on the home page
    # then getting that records existing details and passing them to the update form
    todo = Todo.query.filter_by(tid=tid).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:tid>')
def delete(tid):
    todo = Todo.query.filter_by(tid=tid).first()
    
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

# if __name__ == '__main__':
#     app.run(debug=True)