import matplotlib.pyplot as plt
import matplotlib

###########################
### FONT STUFF ############
###########################

# Changing font-size on entire figure
plt.rcParams.update({'font.size': 22})

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

# or
matplotlib.rc('font', **font)