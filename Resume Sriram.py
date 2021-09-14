# Text Variables
Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my portfolio.'
Name = 'SRIRAM R'
Title = 'Junior Python Developer'
Contact = 'Ceske Budejovice \n\n\n604-282-862\n\n\nsriram21003@gmail.com\n\n\nlinkedin.com/in/sriram-r-03\n\n\ngithub.com/Rite2ram'
ProjectsHeader = 'About'
ProjectOneTitle = 'Motivated computer science graduate seeking growth opportunity \nas an entry level Python Developer.'
WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Freelancer / 3d Visualizer'
WorkOneTime = '5/2019-Present'
WorkOneDesc = 'Key accomplishments in freelance projects\n- Strategically provided 3d Visualization for companies\n- Assisted by perfecting the 3d visualization of Exteriors and Interiors.\n- Portfolio published and can be viewed at:-\n    - https://youtu.be/LpQ2SY3Z0mM\n    - https://youtu.be/ooCXhafjAEw\n    - https://youtu.be/ALYGHCrH8HE.'
WorkTwoTitle = 'Sobha Ltd. / Manager(3D Visualizer)'
WorkTwoTime = '10/2012-4/2019'
WorkTwoDesc = '- Congregate from considerate requirement to final production\n- 3D Compositing, Layer rendering\n- Enhancing views after render'
WorkThreeTitle = 'Adi animation Studios Pvt. Ltd. / Production Manager (3D Visualizer)'
WorkThreeTime = '6/2006-5/2012'
WorkThreeDesc = '- Involved in initiation of two startups named Studio 9 and \n  Axon 3d animation\n- Congregate from considerate requirement to final production\n- 3D Compositing, Layer rendering\n- Enhancing views after render\n- Client co-ordination\n- Handling tecnical problems software or hardware related.'
EduHeader = 'EDUCATION'
EduOneTitle = 'Google (Coursera), Python Crash Course'
EduOneTime = '2021'
EduThreeTitle = 'Maya Academy of Advance Cinematics, Professional Animation Course'
EduThreeTime = '2005-2006'
EduTwoTitle = 'Madura Kamraj University, Bachelors of Computer Application'
EduTwoTime = '2000-2003'
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Git\n- Scripting and Developing\n   Skills in Python\n- Problem Solving\n- MS Office\n- 3DS Max\n- Adobe Photoshop\n- Adobe Premiere\n- Adobe After Effects\n- Vray \n- Corona'
ExtrasTitle = 'My Time'
LangTitle = 'Languages Known'
LangDesc = 'English\nHindi\nTamil\nCzech(Pursuing)'
CodeTitle = 'View Portfolio'
# Setting style for bar graphs
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'calibri'
fig, ax = plt.subplots(figsize=(8.5, 11))
# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=325)
plt.axhline(y=.722, xmin=0, xmax=1, color='#ffffff', linewidth=3)
# set background color
ax.set_facecolor('white')
# remove axes
plt.axis('off')
# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.92), weight='bold', fontsize=11, color ='#fdc338')
plt.annotate(Contact, (.72,.76), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ProjectsHeader, (.02,.875), weight='bold', fontsize=11, color='#fdc338')
plt.annotate(ProjectOneTitle, (.02,.84), weight='regular', fontsize=10)
plt.annotate(EduHeader, (.02,.80), weight='bold', fontsize=11, color='#fdc338')
plt.annotate(EduOneTitle, (.02,.775), weight='regular', fontsize=10)
plt.annotate(EduOneTime, (.05,.755), weight='regular', fontsize=10, alpha=.6)
plt.annotate(EduThreeTitle, (.02,.735), weight='regular', fontsize=10)
plt.annotate(EduThreeTime, (.05,.715), weight='regular', fontsize=10, alpha=.6)
plt.annotate(EduTwoTitle, (.02,.695), weight='regular', fontsize=10)
plt.annotate(EduTwoTime, (.05,.675), weight='regular', fontsize=10, alpha=.6)
plt.annotate(WorkHeader, (.02,.63), weight='bold', fontsize=11, color='#fdc338')
plt.annotate(WorkOneTitle, (.02,.61), weight='regular', fontsize=10)
plt.annotate(WorkOneTime, (.05,.59), weight='regular', fontsize=10, alpha=.6)
plt.annotate(WorkOneDesc, (.02,.465), weight='regular', fontsize=10)
plt.annotate(WorkTwoTitle, (.02,.43), weight='regular', fontsize=10)
plt.annotate(WorkTwoTime, (.05,.41), weight='regular', fontsize=10, alpha=.6)
plt.annotate(WorkTwoDesc, (.02,.353), weight='regular', fontsize=10)
plt.annotate(WorkThreeTitle, (.02,.325), weight='regular', fontsize=10)
plt.annotate(WorkThreeTime, (.05,.305), weight='regular', fontsize=10, alpha=.6)
plt.annotate(WorkThreeDesc, (.02,.183), weight='regular', fontsize=10)
plt.annotate(LangTitle,(.02,.14), weight='bold', fontsize=11, color='#fdc338')
plt.annotate(LangDesc,(.02,.07), weight='regular', fontsize=10)
plt.annotate(SkillsHeader, (.7,.4), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.195), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7,.7), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(CodeTitle, (.7,.16), weight='bold', fontsize=10, color='#ffffff')


from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg


#adding icons qrcode pie and graph
EduOneTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(EduOneTimeicon, zoom=0.009)
ab = AnnotationBbox(imagebox, (0.031, 0.76), pad=-1, frameon="True")
ax.add_artist(ab)
EduThreeTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(EduThreeTimeicon, zoom=0.009)
ab1 = AnnotationBbox(imagebox, (0.031, 0.72), pad=-1, frameon="True")
ax.add_artist(ab1)
EduTwoTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(EduTwoTimeicon, zoom=0.009)
ab2 = AnnotationBbox(imagebox, (0.031, 0.68), pad=-1, frameon="True")
ax.add_artist(ab2)
WorkOneTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(WorkOneTimeicon, zoom=0.009)
ab3 = AnnotationBbox(imagebox, (0.031, 0.595), pad=-1, frameon="True")
ax.add_artist(ab3)
WorkTwoTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(WorkTwoTimeicon, zoom=0.009)
ab4 = AnnotationBbox(imagebox, (0.031, 0.415), pad=-1, frameon="True")
ax.add_artist(ab4)
WorkThreeTimeicon = mpimg.imread('calendericon1.jpg')
imagebox = OffsetImage(WorkThreeTimeicon, zoom=0.009)
ab5 = AnnotationBbox(imagebox, (0.031, 0.31), pad=-1, frameon="True")
ax.add_artist(ab5)
plt.axhline(y=.668, xmin=0, xmax=1, color='#ffffff', linewidth=16)
pieicon = mpimg.imread('pie2.png')
imagebox = OffsetImage(pieicon, zoom=0.12)
ab6 = AnnotationBbox(imagebox, (0.825, 0.54), pad=-1, frameon="True")
ax.add_artist(ab6)
Locationicon = mpimg.imread('locationicon.png')
imagebox = OffsetImage(Locationicon, zoom=0.021)
ab7 = AnnotationBbox(imagebox, (0.675, 0.963), pad=-.09, frameon="True")
ax.add_artist(ab7)
Callicon = mpimg.imread('callicon.png')
imagebox = OffsetImage(Callicon, zoom=0.021)
ab8 = AnnotationBbox(imagebox, (0.675, 0.912), pad=-.09, frameon="True")
ax.add_artist(ab8)
Emailicon = mpimg.imread('emailicon.png')
imagebox = OffsetImage(Emailicon, zoom=0.021)
ab9 = AnnotationBbox(imagebox, (0.675, 0.865), pad=-.09, frameon="True")
ax.add_artist(ab9)
Linkicon = mpimg.imread('linkicon.png')
imagebox = OffsetImage(Linkicon, zoom=0.07)
ab10 = AnnotationBbox(imagebox, (0.675, 0.815), pad=-.09, frameon="True")
ax.add_artist(ab10)
Linkicon = mpimg.imread('linkicon.png')
imagebox = OffsetImage(Linkicon, zoom=0.07)
ab12 = AnnotationBbox(imagebox, (0.675, 0.76), pad=-.09, frameon="True")
ax.add_artist(ab12)
Langicon = mpimg.imread('Lang.png')
imagebox = OffsetImage(Langicon, zoom=0.045)
ab11 = AnnotationBbox(imagebox, (0.17, 0.072), pad=-1, frameon="True")
ax.add_artist(ab11)
arr_code = mpimg.imread('SRQRCode.png')
imagebox = OffsetImage(arr_code, zoom=0.25)
ab12 = AnnotationBbox(imagebox, (0.84, 0.073))
ax.add_artist(ab12)

#saving image
plt.savefig('Sriram_Resume.pdf', dpi=300, bbox_inches='tight')
#plt.show()