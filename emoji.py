print('Вас приветствует конвертер смайликов в емоджи 😂🙂🙁😠😈')
text = (input('Введите текст для конвертации: '))
words = text.split(' ')
emojis = {
  ':)':'🙂',
  ':(':'🙁',
  'XD':'😂',
  '>:(':'😠',
  '>:)':'😈'
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

