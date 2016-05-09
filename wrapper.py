import cluster_collision

sim_name = raw_input("Simulation Name: ")
numb = float(raw_input("Number of Stars: ")) #Turn these inputs into floats at very beginning!
time_step = float(raw_input("Timestep (Myr): "))
total_time = float(raw_input("Total Runtime: "))

#Run simulation
cluster_collision.do_simulation(
            sim_name,
            numb,
            time_step,
            total_time
        )
