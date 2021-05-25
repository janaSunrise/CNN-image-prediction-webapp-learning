import argparse
import random
import os
import sys

from PIL import Image


def create_noise(src, dst):
    """Creates noise in our dataset to train the de-noising model"""
    for image in os.listdir(src):
        if image.endswith((".jpg", ".png", ".jpeg")):
            img = Image.open(os.path.join(src, image))
            dims = img.size
            fact = random.uniform(0.2, 0.45)
            height, width = round(dims[0] * fact), round(dims[1] * fact)

            compress_result = img.resize((height, width), Image.ANTIALIAS)
            decompress_result = compress_result.resize(dims, Image.NEAREST)
            decompress_result.save(os.path.join(dst, f"{image[:-4]}_deres.jpg"), quality=95)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility script to generate de-resolution data")
    parser.add_argument("-src", required=True, help="Path to the folder containing images")
    parser.add_argument("-dst", required=True, help="Final destination to save the images")
    args = parser.parse_args()

    args.src, args.dst = os.path.expanduser(args.src), os.path.expanduser(args.dst)

    if not os.path.exists(args.src):
        print("Specified source path does not exist. Please check them again.")
        sys.exit(1)

    if not os.path.exists(args.dst):
        os.makedirs(args.dst)
        print("Destination source did not exit. Created the path manually.")

    create_noise(src=args.src, dst=args.dst)
