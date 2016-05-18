# -- BASIC -- #
import os
import numpy as np

# -- AMUSE -- #
from amuse.units import nbody_system
from amuse.units import units
from amuse.ic.plummer import new_plummer_sphere
from amuse.datamodel import Particles
from amuse.community.hermite0.interface import Hermite
from amuse.ic.salpeter import new_salpeter_mass_distribution



def write_csv_log(f_name, particle_set, time, mass_u=units.kg, dist_u=units.lightyear):
    f1 = open(f_name, "w") #Open file (make new one), and write to it (using "w")
    f1.write("TIME=" + str(time) + "\n")
    f1.write("id,mass,x,y,z\n") #Write column headers of id, mass, and position in x,y,z
    #f1.write("___," + mass_u + )
    for i in range(0,len(particle_set)): #for every particle from 0 to length-1
        part = particle_set[i] #Get specific particle

        ident = str(i)
        mass = str(part.mass.value_in(mass_u))
        xpos = str(part.position.x.value_in(dist_u))
        ypos = str(part.position.y.value_in(dist_u))
        zpos = str(part.position.z.value_in(dist_u))

        f1.write(
            ident + "," + #using num instead of id for now, including the "X", "Y", and "Z" as identifiers
            mass + "M," + #.value_in(units.djoarn) means getting the value in those units, and excludes the unit on the end
            xpos + "X," +
            ypos + "Y," +
            zpos + "Z" +
            "\n"
        ) #Write id, mass, and position (x,y,z) and include \n to ensure it goes to newline on the next entry
    f1.close()

def do_simulation(nme, num_sim_1, num_sim_2, timestep, total_runtime):

    name = nme #Name of the specific simulation
    outputPath = "output/" + name #Where the output csv files will go

    dt = timestep | units.Myr #timestep
    rt = total_runtime | units.Myr #total runtime
    t = 0.0 | units.Myr #current runtime

    convert_nbody = nbody_system.nbody_to_si(100.0 | units.MSun, 1 | units.parsec)

    #Create 1st plummer sphere
    print ("Populating star clusters")
    plummer_1 = new_plummer_sphere(num_sim_1, convert_nbody)
    plummer_1.x += 10.0 | units.lightyear #Move stars 10 ly to the "right"
    plummer_1.mass = new_salpeter_mass_distribution(num_sim_1) #Provide mass for stars based on salpeter mass distribution

    #Create 2nd plummer sphere
    plummer_2 = new_plummer_sphere(num_sim_2, convert_nbody)
    plummer_2.x -= 10.0 | units.lightyear #Move stars 10 ly to the "left"
    plummer_2.mass = new_salpeter_mass_distribution(num_sim_2) #Provide mass for stars based on salpeter mass distribution

    #Creates a set of particles, "stars", and then adds each plummer sphere to it
    stars = Particles()
    stars.add_particles(plummer_1)
    stars.add_particles(plummer_2)

    #Simulation time!
    #Actually, initializing codes first
    print ("Initializing Hermite...")
    hermite_code = Hermite(convert_nbody) #instantiate(?) hermite code, feed it unit converter
    ###### space for any other paramters ######
    print ("    Adding particles")
    hermite_code.particles.add_particles(stars) #add "stars" particle set

    print ("Creating folder at output path")
    os.mkdir(outputPath) #Make folder in output folder
    print ("Outputting start CSV")

    i = 0

    name_num_length = len(str(int(round(rt.value_in(units.Myr) / dt.value_in(units.Myr)))))
    name_num = format(i, '0' + str(name_num_length) + 'd') #0nd, where n is the length of the string, and 0 means to padd with zeros
    f_start_name = outputPath + "/csv_" + name + name_num  + ".txt" #ex: /home/noah/amuse/output/SimOne/plot_SimOne_0000.png
    write_csv_log(f_start_name, hermite_code.particles, 0.0) #Write first CSV log at time 0.0

    print ("Begin simulation...")
    #Now it is simulation time
    while (t < rt):
        print ("Time:" + str(t))
        hermite_code.evolve_model(t) #evolve it up to that time, t

        t += dt

        print ("    Outputting to CSV")

        name_num = format(i, '0' + str(name_num_length) + 'd')
        file_name = outputPath + "/csv_" + name + name_num + ".txt" #File name for csv's is like "outputPath/time_t.csv"
        write_csv_log(file_name, hermite_code.particles, t.value_in(units.Myr))

        i += 1

        #Note: if you want to include SSE or SEBA codes (stellar evolution), make sure to reset the mass _after_ running that code for each step, as the mass of those stars may change due to stellar evolution
        #Ex: hermite_code.particles.mass = stellar_evolution_code.particles.mass
        #Also: File name should go up to end time, because there is a log for time 0.0, and then time is incremented *before* the file is named

    print ("Simulation complete.")
    hermite_code.stop()
