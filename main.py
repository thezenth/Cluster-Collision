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

def two_cluster_simulation(n_stars_1, n_stars_2, timestep, total_runtime):
    dt = timestep | units.Myr
    rt = total_runtime | units.Myr

    convert_nbody = nbody_system.nbody_to_si(100.0 | units.MSun, 1 | units.parsec)

    #Create 1st plummer sphere
    print ("Populating star clusters")
    plummer_1 = new_plummer_sphere(n_stars_1, convert_nbody)
    plummer_1.x += 10.0 | units.lightyear #Move stars 10 ly to the "right"
    plummer_1.mass = new_salpeter_mass_distribution(n_stars_1) #Provide mass for stars based on salpeter mass distribution

    #Create 2nd plummer sphere
    plummer_2 = new_plummer_sphere(n_stars_2, convert_nbody)
    plummer_2.x -= 10.0 | units.lightyear #Move stars 10 ly to the "left"
    plummer_2.mass = new_salpeter_mass_distribution(n_stars_2) #Provide mass for stars based on salpeter mass distribution

    #Creates a set of particles, "stars", and then adds each plummer sphere to it
    stars = Particles()
    stars.add_particles(plummer_1)
    stars.add_particles(plummer_2)

    Simulation time!
    #Actually, initializing codes first
    print ("Initializing Hermite...")
    hermite_code = Hermite(convert_nbody) #instantiate(?) hermite code, feed it unit converter
    ###### space for any other paramters ######
    print ("    Adding particles")
    hermite_code.particles.add_particles(stars) #add "stars" particle set
