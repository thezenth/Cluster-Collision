import cluster_collision
import plotter as pltr
import os
import sys

sim_name = raw_input("Simulation Name: ")
numb_1 = float(raw_input("Number of Stars (Cluster 1): ")) #Turn these inputs into floats at very beginning!
numb_2 = float(raw_input("Number of Stars (Cluster 2): "))
time_step = float(raw_input("Timestep (Myr): "))
total_time = float(raw_input("Total Runtime: "))

#Run simulation
cluster_collision.do_simulation(
            sim_name,
            numb_1,
            numb_2,
            time_step,
            total_time
        )

dir_name = sim_name #raw_input("Directory: ")
working= os.environ.get("WORKING_DIRECTORY","/home/noah/amuse/output/" + dir_name)
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )

i = 0
for f in os.listdir("."):
    plt_data = pltr.read_csv(f, numb_1 + numb_2) #numb_1 + numb_2 is the total number of stars
    timeForName = str(f)[
                str(f).index("_")+1:str(f).index(".txt") #the time i
    ]
    pltr.to_plot(plt_data, str(f)[] + timeForName + " Myr","/home/noah/amuse/output/" + dir_name + "/plot_" + sim_name + "_" + str(i) + ".png")
    i += 1

