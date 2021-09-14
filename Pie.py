import matplotlib.pyplot as plt

# Setting labels for items in Chart
MYTIME = ['Trekking', 'Photography', 'Music', 'Road Trips', 'Arch Viz']

# Setting size in Chart based on
# given values
TimeGiven = [10, 10, 10, 20, 40]

# colors
colors = ['#feefca', '#fee099', '#fdd269', '#fdc338',
          '#fcb508', ]
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
plt.rcParams.update({'font.size': 12})
# Pie Chart
plt.pie(TimeGiven, colors=colors, labels=MYTIME,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)

# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

# Displaing Chart
#plt.show()
plt.savefig('pie2.png', dpi=300, bbox_inches='tight')