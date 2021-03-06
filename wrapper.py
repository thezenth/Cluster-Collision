import cluster_collision
import plotter as pltr
import os
import sys

sim_name = raw_input("Simulation Name: ")
numb_1 = float(raw_input("Number of Stars (Cluster 1): ")) #Turn these inputs into floats at very beginning!
numb_2 = float(raw_input("Number of Stars (Cluster 2): "))
total_num = numb_1 + numb_2 #total numbr of stars
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
name_num_length = len(
    	str(
            int(round(total_time / time_step)) #first, round the float to nearest interger, then convert data type to integer
        ) #total_time / time_step is the number of csv files that will be generated, and then the length of this number is found, because if the highest file name will be 100, then the first file name needs to be formatted 001, if the highest file nameiwll be 20000, then the first needs to be 00001
)
print ("NAME NUM LENGTH=" + str(name_num_length))
print ("TOTAL/STEP=" + str(total_time/time_step))

print ("Creating plots...")

sortedFiles = sorted(os.listdir(".")) #get all the files in the directory, which should only be the .txt files
for f in sortedFiles:

    #print ("Reading csv file...")
    print ("FILE= " + f)
    plt_data = pltr.read_csv(f, total_num) #numb_1 + numb_2 is the total number of stars

    #Name funkiness

    #print ("Creating plot..")

    name_num = format(i, '0' + str(name_num_length) + 'd') #0nd, where n is the length of the string, and 0 means to padd with zeros
    plt_name = "/home/noah/amuse/output/" + dir_name + "/plot_" + sim_name + "_" + name_num + ".png" #ex: /home/noah/amuse/output/SimOne/plot_SimOne_0000.png

    timeLine = open(f, 'r').readline()
    timeForName = timeLine[ timeLine.index("=")+1:timeLine.index("\n") ]

    #str(f).index("_")+1:str(f).index(".txt") #the time, as a substring excised from the name

    pltr.to_plot(plt_data, timeForName + " Myr",plt_name)

    i += 1

print ("Finished plots.")

#Make movie from .png images
#avconv -r 10 -vf scale=-1:1080 -i filename_%nd.png NAME.avi
cmdStr = "avconv -r 10 -i " + "plot_" + sim_name + "_" + "%0" + str(name_num_length) + "d.png -vf scale=-1:1080 test.avi" #finds images with zero padding of length "name_num_length"
os.system(cmdStr)
