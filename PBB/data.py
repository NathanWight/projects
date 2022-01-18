import math
user = int(input("Year of interest: "))
user_range = input("Year range of interest (year,year): ")
average = 0
count = 0
over_average = 0
total_count = 0
highest_life = 0
highest_country = "error"
overall_country = "error"
overall_life = 0
lowest_life = 1000
lowest_country = "error"
lowest_year = 1000000
highest_year = 0
low_country = "error"
low_life = 10000
variance = []
range_year = 0
range_low_life = 10000
range_highest_life = 0
range_average = 0
range_country_high = "error"
range_country_low = "error"
range_count = 0
user_parts = user_range.split(",")


intl_year = int(user_parts[0].strip())
int_year = int(user_parts[1].strip())
high_year = int_year
low_year = intl_year
with open("life-expectancy.csv") as text:
     next(text)

     
     for line in text:
          parts = line.split(",")
          country = parts[0].strip()
          code = parts[1].strip()
          year = int(parts[2].strip())
          life = float(parts[3])
          over_average += life
          total_count += 1
          #variance.append(life - total_average)

          if year < lowest_year:
               lowest_year = year 
          if year > highest_year:
               highest_year = year

          if life < lowest_life:
               lowest_life = life
               lowest_country = country
          
          if low_year <= year <= high_year:
               range_average += life
               range_count += 1
               if life < range_low_life:
                    range_low_life = life
                    range_country_low = country 
          
          if range_highest_life < life:
               range_highest_life = life
               range_country_high = country







          if life > overall_life:
                    overall_life = life
                    overall_country = country
          if year == user:
               average += life
               count += 1
               if life > highest_life:
                    highest_life = life
                    highest_country = country
               if life < low_life:
                    low_life = life
                    low_country = country
total_range = range_average / range_count
total_average = over_average / total_count
average = average / count
total_years = highest_year - lowest_year
#Total averages 
print()
print(f"The overall max life expectancy over the last {total_years} years was: {overall_life} in:  {overall_country}")
print(f"The overall lowest life expectancy over the last {total_years} years was: {lowest_life} in: {lowest_country}")
print(f"The average life expectancy over the last {total_years} years was: {total_average}")

print()

# year wanted
print(f"The average life expectancy in {user} was: {average}")
print(f"The highest life expectany in {user} was: {highest_life} in: {highest_country}")
print(f"The lowest life expectany in {user} was: {low_life} in: {low_country} ")
print()

print(f"The average life expectance between {low_year} and {high_year} was: {total_range}")
print(f"The highest life expectany between {low_year} and {high_year} was: {range_highest_life} in: {range_country_high}")
print(f"The lowest life expectany between {low_year} and {high_year} was: {range_low_life} in: {range_country_low} ")

with open("life-expectancy.csv") as text:
     next(text)
     for line in text:
          parts = line.split(",")
          life = float(parts[3])
          over_average += life
          total_count += 1
          variance.append((life - total_average)**2)
variances = sum(variance) / total_count
standard = math.sqrt(variances)
print(f"The standaard deviation is: {standard} years with a variation of: {variances} years")


                

          
