import argparse

import torch
from diffusers import StableDiffusionPipeline

parser = argparse.ArgumentParser(
    description="Generate an image with the Small Stable Diffusion model"
)
parser.add_argument("--prompt", "-p", type=str, help="The image prompt")

args = parser.parse_args()

MODEL_ID = "OFA-Sys/small-stable-diffusion-v0"
pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

img = pipe(args.prompt + " 4K").images[0]
img.save("output.png")