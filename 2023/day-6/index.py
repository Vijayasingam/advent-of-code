
example = [
  "7:9",
  "15:40",
  "30:200"
]

input = [
  "42:308",
  "89:1170",
  "91:1291",
  "89:1467"
]

part_two_input = [
  "42899189:308117012911467",
]

def multiply_list(list):
 
    # Multiply elements one by one
    result = 1
    for x in list:
        result = result * x
    return result

def can_win_race(duration, speed, points_to_win):
  race = duration - speed
  points_won = race * speed
  if(points_won > points_to_win):
    print('Points', speed, duration, points_won, points_to_win)
    return True
  return False

def process_race_duration(duration, points_to_win):
  chances_to_win = []
  for travel in range(duration):
    result = can_win_race(duration, travel, points_to_win)
    if (result == True):
      chances_to_win.append(travel)
  return len(chances_to_win)

def process_race_data(map):
  chances_to_win = []
  for key in map:
    [time, points] = key.split(':')
    chances_to_win_the_race = process_race_duration(int(time), int(points))
    chances_to_win.append(chances_to_win_the_race)
  print(multiply_list(chances_to_win))

def main():
  process_race_data(part_two_input)
# part two - 24655068
if __name__ == "__main__":
  main()