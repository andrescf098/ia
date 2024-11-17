from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
import glob
import tqdm
import matplotlib.pyplot as plt

url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg'

def read_image(url):
    image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
    return image

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
def ocr(image, processor, model):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

def eval_new_data(data_path=None, num_samples=4, model=None):
    image_paths = glob.glob(data_path)
    for i, image_path in enumerate(image_paths):
        if i == num_samples:
            break
        image = read_image(image_path)
        text = ocr(image, processor, model)
        plt.figure(figsize=(7, 4))
        plt.imshow(image)
        plt.title(text)
        plt.axis('off')
        plt.show()

eval_new_data('https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg', num_samples=4, model=model)