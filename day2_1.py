def score_round(ops_throw,your_throw):
  translated_throw = str()
  throw_score = 0
  if your_throw == 'X':
    throw_score = 1
    translated_throw = 'A'
  if your_throw == 'Y':
    translated_throw = 'B'
    throw_score = 2
  if your_throw == 'Z':
    translated_throw = 'C'
    throw_score = 3



  if ops_throw == translated_throw:
    return throw_score + 3
  if ops_throw == 'A' and your_throw == 'Y':
    return throw_score + 6
  if ops_throw == 'A' and your_throw == 'Z':
    return throw_score + 0
  if ops_throw == 'B' and your_throw == 'X':
    return throw_score + 0
  if ops_throw == 'B' and your_throw == 'Z':
    return throw_score + 6
  if ops_throw == 'C' and your_throw == 'X':
    return throw_score + 6
  if ops_throw == 'C' and your_throw == 'Y':
    return throw_score + 0
    

with open('day2_input','r') as input_file:
  total_score = 0
  for line in input_file:
    split_line = line.strip().split(' ')
    total_score += score_round(split_line[0],split_line[1])
  print(total_score)
