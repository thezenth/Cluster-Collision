import cluster_collision

sim_name = raw_input("Simulation Name: ")
numb = int(raw_input("Number of Stars: ")) #Turn these inputs into integers at very beginning!
time_step = int(raw_input("Timestep (Myr): "))
total_time = int(raw_input("Total Runtime: "))

#Run simulation
cluster_collision.do_simulation(
            sim_name,
            numb,
            time_step,
            total_time
        )
