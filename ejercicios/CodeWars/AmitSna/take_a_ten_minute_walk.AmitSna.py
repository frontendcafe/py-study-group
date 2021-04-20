is_valid_walk = lambda walk: len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")

def is_valid_walk(walk):
  return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")

def is_valid_walk(walk):
  if len(walk) != 10:
    return false
  coordinates = [0, 0]
  for step in walk:
    if step == "n":
      coordinates[1] += 1
    elif step == "s":
      coordinates[1] -= 1
    elif step == "e":
      coordinates[0] += 1
    elif step == "w":
      coordinates[0] -= 1
  return coordinates[0] == coordinates[1]
