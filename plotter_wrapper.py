import plotter as pltr
import os
import sys 

dir_name = raw_input("Directory: ")
working= os.environ.get("WORKING_DIRECTORY","/home/noah/amuse/output/" + dir_name)
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )

i = 0
for f in os.listdir("."):
    plt_data = pltr.read_csv(f, 125)
    pltr.to_plot(plt_data, "/home/noah/amuse/output/" + dir_name + "/plot_" + str(i) + ".png")
    i += 1
