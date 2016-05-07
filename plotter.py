from dropbox_functions import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# -- PLAN FOR visual_sim() -- #
# Able to save data from simulation in a csv (comma delimted text file)
# Then, visual_sim() is pointed to that file, maybe there is a function/lib to read it?
# Then, simulation is made based upon this data

def visual_sim ()

def make3dPlot ( name, t, saveFolder, xData, yData, zData, limits, clrs = None ):
	print ("Creating 3D plot...")

	print ( "	Initializing Figure..."  )
	fig = plt.figure()
	
	print ( "	Making 3D Axes..." )
	ax = fig.add_subplot(111, projection='3d')
	ax.set_title("Positions - " + t + " myr")

	if limits is not None:
		ax.set_xlim3d( [ limits[0], limits[1] ] )
		ax.set_ylim3d( [ limits[2], limits[3] ] )
		ax.set_zlim3d( [ limits[4], limits[5] ] )
		ax.set_autoscale_on(False)

	print ( "	Plotting Data...")
	if clrs is not None:
		print ("		Coloring...")
		#colors = ['red', 'blue']
		#levels = [0, 1]

		#cmap, norm = mpl.colors.from_levels_and_colors(levels=levels, colors=colors, extend='max')

		#ax.scatter(x,y,c=z, s=150, marker='<', edgecolor='none', cmap=cmap, norm=norm)
		ax.scatter( xData, yData, zData, c=clrs)
	else:
		ax.scatter ( xData, yData, zData ) 
	
	print ("	Saving Figure...")

	if ".png" not in name:
		name = name + ".png"
	print ("POS NAME = " + name)
	plt.savefig(name)

	moveToDropbox(name, saveFolder)

	print ("Done Creating 3D Plot.")

def HRPlot(name, t, saveFolder, xData, yData, clrs):
        print "Plotting HR Diagram.."
      	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_title("HR diagram - " + t + " myr" )
	ax.set_xlabel("Effective Temperature (K)")
	ax.set_ylabel("Luminosity (solar luminosity)")

	ax.scatter( xData, yData, c=clrs )
	ax.axis([50000, 2500., 0.00001, 1000000])

	if ".png" not in name:
		name = name + ".png"
	
	print ("NAME = " + name)
	plt.savefig(name)

	moveToDropbox(name, saveFolder)
