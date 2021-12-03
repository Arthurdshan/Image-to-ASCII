import cv2

ascii_characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize(image, scale_percent=20):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    resized_img = cv2.resize(image, (width, height),
                             interpolation=cv2.INTER_AREA)

    return resized_img


def pixels_to_ascii(image):
    characters = []
    rows, cols = image.shape

    for i in range(rows):
        for j in range(cols):
            k = image[i, j]
            characters.append(ascii_characters[k//25])

    img_data = ''.join(characters)
    return img_data


def main():
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


if __name__ == "__main__":
    main()
