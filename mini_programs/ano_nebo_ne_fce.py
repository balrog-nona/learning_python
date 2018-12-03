def ano_ne(otazka):
  while True:
    odpoved = input("Chces si zahrat hru? ano/ne: ")
    odpoved = odpoved.lower()
    odpoved = odpoved.strip()
    if odpoved == "ano" or odpoved == "a":
      return True
    elif odpoved == "ne" or odpoved == "n":
      return False
    else:
      print("Nerozumim, bud ano nebo ne!")

if ano_ne("Chces si zahrat hru?"):
  print("To si ji budes muset nejdriv naprogramovat :]")
else:
  print("Skoda.")


  


  




