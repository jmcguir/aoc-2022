with open('day1_input', 'r') as inputfile:
  elf_list = list()
  temp_value = 0
  for line in inputfile:
    if line == '\n':
      elf_list.append(temp_value)
      temp_value = 0
    else:
      temp_value += int(line)
  high_water_value = 0
  high_water_index = 0
  for index, elf in enumerate(elf_list):
    if elf > high_water_value:
      high_water_value = elf
      high_water_index = index
  print(high_water_value, high_water_index)


