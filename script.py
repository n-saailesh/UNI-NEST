# from flask import Flask, request, render_template

# app = Flask(__name__, template_folder=r'C:\Users\MyPC\OneDrive\VS Code Projects\uninest')

# @app.route('/a')
# def preferences():
#     render_template('preferences.html')

# @app.route('/a', methods = ['GET','POST'])
           
# def submit():
#     city_retrived = request.form.get('city')
#     minimum_retrived = request.form.get('minimum')
#     maximum_retrived = request.form.get('maximum')
#     house_retrived = request.form.get('house')
#     apartment_retrived = request.form.get('apartment')


#     string = str(city_retrived) + str(maximum_retrived) + str(minimum_retrived) + str(house_retrived) + str(apartment_retrived)

#     return  render_template('preferences.html', string=string)


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__, template_folder=r'C:\Users\MyPC\OneDrive\VS Code Projects\uninest')

@app.route('/preferences.html')
def preferences():
    return render_template('preferences.html')

@app.route('/a', methods = ['GET','POST'])
def submit():

    if request.method == "POST":
        city_retrived = request.form.get('city')
        minimum_retrived = request.form.get('minimum')
        maximum_retrived = request.form.get('maximum')
        strcutures = request.form.getlist('structure[]')


        string = str(city_retrived) + str(maximum_retrived) + str(minimum_retrived) + str(strcutures)
        print(string)
        return render_template('preferences.html', string=string)

        print(string)
    return render_template('preferences.html')



if __name__ == '__main__':
    app.run(debug=True)

