import cluster_collision

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
