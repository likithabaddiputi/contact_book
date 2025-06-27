from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts ={}

@app.route('/')
def index():
    return render_template('index.html', contacts = contacts)

@app.route('/add-contact', methods=['GET', 'POST'] )
def add():
    if request.method == 'POST':
        name = request.form["name"].strip().title()
        phone = request.form["phone"].strip()
        
        if name and phone.isdigit() and len(phone) == 10:
            contacts[name] = phone
        
        
        return redirect('/')
    
    return render_template('add_contact.html')
    
@app.route('/update-contact/<name>', methods = ['GET', 'POST'])
def update(name):
    if request.method == 'POST':
        new_name = request.form["name"].strip().title()
        phone = request.form["phone"]
        
        if new_name and phone.isdigit() and len(phone) == 10:
            contacts.pop(name)
            contacts[new_name] = phone
            
        return redirect('/')  
    phone = contacts[name]
    return render_template('update_contact.html', name = name , phone = contacts[name])
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query'].lower()
        results = {}

        for name, phone in contacts.items():
            if query in name.lower():  # partial match, case-insensitive
                results[name] = phone

        return render_template('search.html', results=results, query=query)

    return render_template('search.html', results=None)

        
@app.route('/delete-contact/<name>')
def delete(name):
    contacts.pop(name, None)  # safely remove without error if not found
    return redirect('/')           
    
    
if __name__ == "__main__":                                                                                  
    app.run(debug = True)
 