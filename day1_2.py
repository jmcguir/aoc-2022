with open('day1_input', 'r') as inputfile:
  elf_list = list()
  temp_value = 0
  for line in inputfile:
    if line == '\n':
      elf_list.append(temp_value)
      temp_value = 0
    else:
      temp_value += int(line)
  elf_list.sort(reverse=True)
  total = 0
  print(elf_list[:3])
  for elf in elf_list[:3]:
    total = total + elf
  print(total)


