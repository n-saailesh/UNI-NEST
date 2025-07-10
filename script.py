

from flask import Flask, request, render_template

#Setting up the Flask framwork and tempalte folder for the pathway of all the HTML files
app = Flask(__name__, template_folder=r'C:\Users\MyPC\OneDrive\VS Code Projects\uninest')

#When the user goes to the preferences page, it will render the preference.html amd ask the user to fill the quick form (GET by default)
@app.route('/preferences.html')
def preferences():
    return render_template('preferences.html')

#When the user submits the form, it will retrieve the data from the form and send it to the sever (POST)
@app.route('/a', methods = ['POST'])
def submit():

    if request.method == "POST":
        city_retrived = request.form.get('city')
        minimum_retrived = request.form.get('minimum')
        maximum_retrived = request.form.get('maximum')
        strcutures = request.form.getlist('structure[]')

        print(city_retrived,maximum_retrived,strcutures)

        string = str(city_retrived) + str(maximum_retrived) + str(minimum_retrived) + str(strcutures)
        
        import chatBot
        result = chatBot.retrival_from_html(city_retrived,minimum_retrived,maximum_retrived,strcutures)

        return render_template('preferences.html', string=string)

    return render_template('preferences.html')



if __name__ == '__main__':
    app.run(debug=True)


