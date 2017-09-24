#runs after the dataframe is created
from Video import df #import the dataframe
from bokeh.models import HoverTool,ColumnDataSource #provides info from datafames

from bokeh.plotting import figure,show,output_file

#convert the start and end times to strings
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #Convert to that format
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df) #type

p=figure(x_axis_type="datetime",height=100,width=500,responsive=True,title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start:","@Start_string"),("End:","@End_string")]) #create a hover object
p.add_tools(hover)#when quad is hovered over

q=p.quad(left="Start",right="End",bottom =0,top=1,color="green",source=cds) # for every quad

output_file("Graph1.html")
show(p)