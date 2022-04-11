import graphics as gr
import sys
import time

def filter1(img, string):
    '''Creates an ASCII art from in text using the exotic.ppm image'''
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            (r,g,b)=img.getPixel(x,y)
            img.setPixel(x,y,gr.color_rgb((r+g+b)//3, (r+g+b)//3, (r+g+b)//3))
            if (r+g+b)//3 < 128:
                string = string + '1'
                
            else:
                string = string + '0'
            string = string + '\n'
        return string

def filter2(img, string):
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            (r,g,b)=img.getPixel(x,y)
            print(r,g,b)
            img.setPixel(x,y,gr.color_rgb((r+g+b)//3, (r+g+b)//3, (r+g+b)//3))
            # if (r+g+b)//3 > 230:
            #     string = string + 'B'
            if (r+g+b)//3 == 171 and 170:
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
            elif (r+g+b)//3 == 169 and 168:
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
            elif (r+g+b)//3 == 167 and 166:
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
            elif (r+g+b)//3 == 165 and 164:
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
            elif (r+g+b)//3 == 163 and 162:
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
                string = string + '|'
                string = string + '/'
            
            string = string + '\n'
        return string
            
            


def main():
    '''Saves and writrs the ascii text into a text file'''
    string = ''

    img = gr.Image(gr.Point(0,0), 'exotic.ppm')
    string = filter1(img, string)
    secondString = filter2(img, string)

    file = open('filter1.txt', 'w')
    file.write(string)
    # file.close()

    file = open('filter2.txt', 'w')
    file.write(secondString)

if __name__ == '__main__':
    main()
