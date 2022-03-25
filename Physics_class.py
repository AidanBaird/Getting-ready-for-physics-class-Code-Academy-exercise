# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Create a function with an input of fahrenheit to calculate the celsius then call the function with 100 fahrenheit then reverse the equation for the next function
def f_to_c(f_temp = 100):
  c_temp = (f_temp - 32) * 5/9
  #print(c_temp)
  #print("")
  return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  #print(f_temp)
  #print("")
  return f_temp

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  force = mass * acceleration
  #print(force)
  #print("")
  return force

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies", train_force, "Newtons of force.")
print("")

def get_energy(mass, c = 3*10**8):
  energy = mass * c ** 2
  #print(energy)
  #print("")
  return energy

bomb_energy = get_energy(bomb_mass)


print("A 1kg bomb supplies", bomb_energy, "joules")
print("")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  #print(work)
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does", train_work, "joules", "of work over", train_distance, "meters")


