import matplotlib.pyplot as plt
# Language Known

LangKnown = ["Pursing", "Native", "Native", "Proficiency"]

# Names for plotting
Lang = ["Czech", "Tamil", "Hindi", "English"]
# Define plot space
plt.rcParams.update({'font.size': 30})
fig, ax = plt.subplots(figsize=(10, 6))


# Define x and y axes
ax.plot(Lang, LangKnown)


plt.savefig('Lang.png', dpi=300, bbox_inches='tight')