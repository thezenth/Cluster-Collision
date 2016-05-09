from amuse.units import nbody_system
from amuse.units import units
from amuse.ic.plummer import new_plummer_sphere
import numpy as np
from amuse.datamodel import Particles
from amuse.community.hermite0.interface import Hermite
from amuse.ic.salpeter import new_salpeter_mass_distribution

import os

def do_simulation(nme, number, timestep, total_runtime):

    name = nme #Name of the specific simulation
    outputPath = "output/" + name #Where the output csv files will go

    num = number #number of stars in each cluster

    dt = timestep | units.Myr #timestep
    rt = total_runtime | units.Myr #total runtime
    t = 0.0 | units.Myr #current runtime

    convert_nbody = nbody_system.nbody_to_si(100.0 | units.MSun, 1 | units.parsec)

    #Create 1st plummer sphere
    print ("Populating star clusters")
    plummer_1 = new_plummer_sphere(num, convert_nbody)
    plummer_1.x += 10.0 | units.lightyear #Move stars 10 ly to the "right"
    plummer_1.mass = new_salpeter_mass_distribution(num) #Provide mass for stars based on salpeter mass distribution

    #Create 2nd plummer sphere
    plummer_2 = new_plummer_sphere(num, convert_nbody)
    plummer_2.x -= 10.0 | units.lightyear #Move stars 10 ly to the "left"
    plummer_2.mass = new_salpeter_mass_distribution(num) #Provide mass for stars based on salpeter mass distribution

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

    print ("Begin simulation...")
    #Now it is simulation time
    while (t < rt):
        print ("Time:" + str(t))
        hermite_code.evolve_model(t) #evolve it up to that time, t
        t += dt #increment time
    
        print ("    Outputting to CSV")
        f_name = outputPath + "/time_" + str(t) + ".txt" #File name for csv's is like "outputPath/time_t.csv"
        f1 = open(f_name, "w") #Open file (make new one), and write to it (using "w")
        f1.write("id,mass,x,y,z\n") #Write column headers of id, mass, and position in x,y,z
        for i in range(0,len(hermite_code.particles)): #for every particle from 0 to length-1
            part = hermite_code.particles[i] #Get specific particle
            f1.write(
                str(i) + "," + #using num instead of id for now..
                str(part.mass) + "," +
                str(part.position.x) + "," +
                str(part.position.y) + "," +
                str(part.position.z) +
                "\n"
                ) #Write id, mass, and position (x,y,z) and include \n to ensure it goes to newline on the next entry
        f1.close()

        #Note: if you want to include SSE or SEBA codes (stellar evolution), make sure to reset the mass _after_ running that code for each step, as the mass of those stars may change due to stellar evolution
        #Ex: hermite_code.particles.mass = stellar_evolution_code.particles.mass

    print ("Simulation complete.")
    hermite_code.stop()
