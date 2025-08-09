import math
import matplotlib.pyplot as plt
import numpy as np

# year setup
start_year = 2025
end_year = 2050
years = list(range(start_year,end_year+1))

# demographic setup
pop2025 = 71614788
pop = pop2025
TFR = 0.95

poplist = []
yearlist = []

growth_rate = ((TFR/2.1)-1)/30

migration_rate = 50000

# simulation
for x in range(end_year-start_year+1):
    poplist.append(pop)
    yearlist.append(2025+x)

    print(f"{2025+x}: {pop}")
    pop = round(pop * (1+growth_rate))
    pop += migration_rate


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# plot data
plt.plot(yearlist, poplist)

# labels + title
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Simulation')

# display
plt.show()