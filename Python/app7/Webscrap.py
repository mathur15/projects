import requests
from bs4 import BeautifulSoup
import pandas

#website is subject to changes,output will differ

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
base_url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
c = r.content
soup = BeautifulSoup(c,"html.parser")
page_nr = soup.find_all("a",{"class":"Page"})[-1].text #to extract the number of pages
#getting content of every page as each url has a base url which is common + pattern
for page in (0,int(page_nr)*10,10):
	r = requests.get(base_url+str(page)+".html")
	c = r.content
	soup = BeautifulSoup(c,"html.parser")
	all = soup.find_all("div", {"class":"propertyRow"})

	#loop to iterate over all the text elements -outer divs
	l = []
	for item in all:
		#a dictionary for every item
		d = {}
		d["Price"]= item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
		try:
			d["Address"]=item.find("span",{"class":"propAddressCollpse"}).text
		except:
			d["Address"]= None
		try:
			d["Locality"]=item.find_all("span",{"class":"propAddressCollpse"})[1].text
		except:
			d["Locality"] = None
		try:
			d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
		except:
			d["Beds"]=None

		try:
			d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
		except:
			d["Area"] = None

		try:
			d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
		except:
			d["Full Baths"] = None

		try:
			d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
		except:
			d["Half Baths"] = None
		#have another iteration to extract the lot size
		for column_group in item.find_all("div",{"class","columnGroup"}):
			#iterating over specific divs within the outer div which is items
			#print(column_group)
			#iterate over column_group
			for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class": "featureName"})):
					if "Lot Size" in feature_group.text:
						d["Lot Size"]= feature_name.text
		l.append(d)
		#print(" ")
	df = pandas.DataFrame(l)
	df.to_csv("Output.csv")