import re

s = 'camelCaseCamelo'

pattern = '(?<=[a-z])(?=[A-Z])'

new_pattern = ' '

new_string = re.sub(pattern, new_pattern, s)

print(new_string)