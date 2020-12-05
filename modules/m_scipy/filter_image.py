from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import wget
from scipy import fft
import math


def afficher_tf(tf):
    """ Affiche le spectre d'une image

    Args :
    tf -- la transformée de Fourier d'une image
    """
    magnitude_spectrum = 20 * np.log(np.abs(tf))
    plt.imshow(magnitude_spectrum.astype(np.uint8))
    plt.show()


def create_square_mask(image_to_mask, length):
    center = (math.floor(image_to_mask.shape[0] / 2), math.floor(image_to_mask.shape[1] / 2))
    delta = math.floor(length/2)
    image_to_mask[center[0]-delta:center[0]+delta, center[1]-delta:center[1]+delta] = 0
    return image_to_mask


# copier la joconde dans votre dossier Jupyter
filename = wget.download('https://python.gel.ulaval.ca/media/notebook/joconde.jpg')

# lire l'image
image = np.array(Image.open(filename).convert('L'))

image_fft = fft.fft2(image)
fft_shift = fft.fftshift(image_fft)
fft_masked = create_square_mask(fft_shift, 80)

img_filtre = fft.ifft2(fft_masked)
img_filtre = np.absolute(img_filtre)



