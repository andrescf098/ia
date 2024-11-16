import stow
import tarfile
import os
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

dataset = os.path.join("Datasets", "IAMHandwriting")

def download_dataset(url, extract_to="Datasets", chuck_size=1024*1024):
    http_response = urlopen(url)

    data = b""
    iterations = http_response.length // chuck_size +1
    for i in range(iterations):
        data += http_response.read(chuck_size)

    zip_file = ZipFile(BytesIO(data))
    zip_file.extractall(path=extract_to)

if not stow.exists(dataset):
    download_dataset('https://git.io/J0fjL', extract_to='Datasets')

    file = tarfile.open(stow.join(dataset, "words.tgz"))
    file.extractall(stow.join(dataset, "words"))