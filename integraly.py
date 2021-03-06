
def rectvalue(start_x, stop_x):
  return ((stop_x - start_x) * ((start_x + stop_x) / 2))
def trapvalue(start_x, stop_x):
  return 0.5*(stop_x - start_x)*(start_x + stop_x)
def simpIntegral(start_x, stop_x):
  return (stop_x - start_x) / 6.0 * (start_x + 4.0 * 0.5 * (start_x + stop_x) + stop_x)

start_x=float(input("start_x = "))
stop_x=float(input("stop_x = "))
print("Rect integral value: "+str(rectvalue(start_x, stop_x)))
print("Trap integral value: "+str(trapvalue(start_x, stop_x)))
print("Simp integral value: "+str(simpIntegral(start_x, stop_x)))
