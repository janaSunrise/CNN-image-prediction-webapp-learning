from PIL import Image
import argparse
import random
import os

def create(src, dst):
    """
    Creates noise in our dataset to train the de-noising model
    """
    for image in os.listdir(src):
        if(image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg")):
            img = Image.open(os.path.join(src, image))
            dims = img.size
            fact = random.uniform(0.2, 0.45) 
            hgt = round(dims[0]*fact)
            wit = round(dims[1]*fact)
            CompressResult = img.resize((hgt,wit),Image.ANTIALIAS)
            DecompressResult = CompressResult.resize(img.size, Image.NEAREST)
            DecompressResult.save(image[:-4]+"_deres.jpg", quality=95)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="utility to create deresoulution data")
    parser.add_argument('-src', required=True, help='src path')
    parser.add_argument('-dst', required=True, help='dst path')
    args = parser.parse_args()
    create(src=args.src, dst=args.dst)
