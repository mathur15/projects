from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success-table', methods=['POST'])
#when the user clicks on the submit button-success_table is executed
#read as a dataframe
#use geopy to read the address column and update df
#rename the updated file according to datetime
def success_table():
    global filename #download function will also use after updating one
    if request.method=="POST":
        file=request.files['file']
        try:
            df=pandas.read_csv(file)
            gc=Nominatim(scheme='http')
            df["coordinates"]=df["Address"].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            #finding the latitude using lambda
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df=df.drop("coordinates",1)
            filename=datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f"+".csv")#to avoid name clash
            df.to_csv(filename,index=None)#generate file with updated date
            return render_template("index.html", text=df.to_html(), btn='download.html')
            #text is variable in the output class of the div of the index and a 
            #download button is rendered as well as soon as button showed
        except Exception as e:
            return render_template("index.html", text=str(e))

@app.route("/download-file/")
def download():#this route is used for when we click on download button to get the new file with the coordinates as
                #attachment
    return send_file(filename, attachment_filename='yourfile.csv', as_attachment=True)
    #use send_file to send the download to the user
if __name__=="__main__":
    app.run(debug=True)
