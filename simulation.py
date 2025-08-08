import math

# year setup
start_year = 2050
end_year = 2080
years = list(range(start_year,end_year+1))

# demographic setup
pop2025 = 71614788
pop = pop2025
TFR = 0.95

growth_rate = ((TFR/2.1)-1)/30

# simulation
for x in range(years):
    pop = pop * (1-growth_rate)
    print(f"{2050+x}: {pop}")