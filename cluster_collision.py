from amuse.units import nbody_system
from amuse.units import units
from amuse.ic.plummer import new_plummer_sphere
import numpy as np
from amuse.datamodel import Particles
import amuse.community.hermite0.interface.Hermite

f_name = "~/amuse/output/AMUSE_to_csv_test.txt"
f = open(f_name, "w")
f.write("id,mass,x,y,z\n")
f.close()

num = 100

dt = 0.5 | units.Myr #timestep
rt = 10.0 | units.Myr #total runtime
t = 0.0 | units.

convert_nbody = nbody_system.nbody_to_si(100.0 | units.MSun, 1 | units.parsec)

#Create 1st plummer sphere
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
hermite_code = Hermite(convert_nbody) #instantiate(?) hermite code, feed it unit converter
###### space for any other paramters ######
hermite_code.add_particles(stars) #add "stars" particle set

#Now it is simulation time
while (t < rt):
    hermite_code.evolve_model(t) #evolve it up to that time, t
    t += dt
    
    f1_name = f_name + "_" + str(t)
    f1 = open(f_name, "w")
    
    for i in range(0,num)

    #Note: if you want to include SSE or SEBA codes (stellar evolution), make sure to reset the mass _after_ running that code for each step, as the mass of those stars may change due to stellar evolution
    #Ex: hermite_code.particles.mass = stellar_evolution_code.particles.mass

hermite_code.stop()
#Dad doesn't understand Git
