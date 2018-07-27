# CODE TO DUMP OUT FONTS FROM PYFIGLET:
import pyfiglet

j = pyfiglet.FigletFont.getFonts()

for i in j:
    figlet = pyfiglet.Figlet(i)
    text = figlet.renderText('Osher')
    with open('text_file_holder.txt', 'a', encoding='utf-8') as fd:
        fd.write(i)
        fd.write('\n')
        fd.write(text)
