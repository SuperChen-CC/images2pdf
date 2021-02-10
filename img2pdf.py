import os
from PIL import Image
from natsort import natsorted
from pikepdf import Pdf, Encryption


# Get the file name used for natsort
def take_filename(item):
    return item.split('/')[-1].split('.')[0]


if __name__ == '__main__':
    # images path(folder)
    image_path = ''
    # pdf file name without suffix
    file_name = ''
    images = [os.path.join(image_path, filename) for filename in os.listdir(image_path)]
    images = natsorted(images, key=take_filename)

    image_list = []

    for image in images:
        print(image)
        image_list.append(Image.open(image).convert('RGB'))
    image_list[0].save(f'tmp/{file_name}.pdf', save_all=True, append_images=image_list[1:])
    with Pdf.open(f'tmp/{file_name}.pdf') as pdf:
        # owner: owner password
        # user: view password
        pdf.save(f'{file_name}.pdf', encryption=Encryption(owner='owner-pwd', user='user-pwd'))
    os.remove(f'tmp/{file_name}.pdf')
