import math
import cv2

scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# scale = " .:-=+*#%@"

'''
receives the image width and height to calculate the aspect ratio
and returns the new resized dimensions for the new image
'''
def new_dimensions(width, height, max_width = 80):
    if width > max_width:
        new_height = math.floor(height * max_width / width)
    return max_width, new_height

'''
returns the ascii character corresponding to the k value 
passed by parameter
'''
def get_ascii_value(k):
    return math.floor((len(scale) - 1) * k / 255)
    
'''
returns the new resized image
'''
def resize(image):
    width = image.shape[1]
    height = image.shape[0]
    
    new_width, new_height = new_dimensions(width, height)

    resized_img = cv2.resize(image,
                             (new_width, new_height),
                             interpolation=cv2.INTER_AREA)

    return resized_img

'''
returns a string with all the ascii characters from the image
'''
def pixels_to_ascii(image):
    characters = []
    rows, cols = image.shape

    for i in range(rows):
        for j in range(cols):
            k = image[i, j]
            characters.append(scale[get_ascii_value(k)])

    img_data = ''.join(characters)
    return img_data

path = input('Enter the path to the image:')
image = cv2.imread(path, 0)

resized_img = resize(image)

img_data = pixels_to_ascii(resized_img)

pixel_count = len(img_data)
ascii_image = "\n".join([img_data[index: (index + resized_img.shape[1])]
                        for index in range(0, pixel_count, resized_img.shape[1])])

print(ascii_image)

f = open('ascii_image.txt', 'w')
f.write(ascii_image)
f.close()