angry = False
bored = False
hungry = False
tired = False

if angry and hungry and bored:
  print("T-Rex eats the Triceratops.")
elif tired and hungry:
  print("T-Rex eats the Iguanadon.")
elif hungry and bored:
  print("T-Rex eats the Stegasaurus.")
elif tired:
  print("T-Rex goes to sleep.")
elif angry and bored:
  print("T-Rex fights with the Velociraptor.")
elif angry or bored:
  print("T-Rex roars.")
else:
  print("T-Rex gives a toothy smile.")

