import numpy as np
import kagglehub
import matplotlib.pyplot as plt
from skimage import io

path = './files'

img = io.imread(f'{path}/Mara.jpeg')
plt.imshow(img)