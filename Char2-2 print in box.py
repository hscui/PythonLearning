# print a sentence in a box with right width

sentence = input("Sentence:")
screen_width = 100
text_width = len(sentence)
box_width = text_width + 6
left_merge = (screen_width - box_width) // 2

print()
print(" "*left_merge+"+"+"-"*(box_width-4)+'+')
print(' '*left_merge+'| '+' '*text_width + ' |')
print(' '*left_merge+'| '+sentence+' |')
print(' '*left_merge+'| '+' '*text_width+' |')
print(" "*left_merge+"+"+"-"*(box_width-4)+'+')
print()

