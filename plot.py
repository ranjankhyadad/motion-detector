from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
 
fig = figure(x_axis_type = "datetime",height = 100, width = 500, title = "Motion Graph")
fig.yaxis.minor_tick_line_color = None
fig.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips = [("Start", "@start_string"),("End", "@end_string")])
fig.add_tools(hover)

quad = fig.quad(left ="Start", right = "End", top=1, bottom=0, source = cds)

output_file("stats.html")
show(fig)
