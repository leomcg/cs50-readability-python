from cs50
import get_string

def main():
  s = get_string("Input: \n");
num_words = 0
num_sentences = 0
num_letters = 0

for i in range(len(s)):
  alphabet = list('abcdefghijklmnopqrstuvwxyz')
  if s[i].lower() in alphabet:
  num_letters += 1
if (i == 0 and s[i] != ' ') or(i != len(s) - 1 and s[i] == ' '
    and s[i + 1] != ' '):
  num_words += 1
if s[i] == '.'
or s[i] == '!'
or s[i] == '?':
  num_sentences += 1

L = (num_letters / num_words) * 100
S = (num_sentences / num_words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index >= 16:
  print('Grade 16+')
elif index < 1:
  print('Before Grade 1')
else :
  print("Grade " + str(index))
main()