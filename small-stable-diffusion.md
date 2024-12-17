# Small Stable Diffusion

Using the "small" Stable Diffusion models can allow your code to work on a less powerful machine. 

## Installing Pytorch

Start by ensuring the `gen-ai` conda environment is active. In previous other examples, this environment included the needed libraries, but in the case of PyTorch, this will have to be installed manually as the version you need will depend on your CUDA version. The instructions can be found here: https://pytorch.org/get-started/locally/

If everything worked properly, you should be able to see that Pytorch has detected a GPU.

```python
import torch

print(torch.cuda.is_available())
```

Running this code should give an output of "True."

## Creating Images

To start with, we're going to need some imports to get Stable Diffusion running. Additionally, we're also going to use the `argparse` library to help decide what prompt we'll use for creating the image.

```python
import argparse

import torch
from diffusers import StableDiffusionPipeline
```

Now we just need to do some basic setup with argparse. We just need to let it know what when we enter `--prompt` or `-p` on the command line, the text following it will be our prompt.

```python
parser = argparse.ArgumentParser(
    description="Generate an image with the Small Stable Diffusion model"
)
parser.add_argument("--prompt", "-p", type=str, help="The image prompt")

args = parser.parse_args()
```

Now the `args.parse` value will store our prompt. Finally, we send this prompt to Stable Diffusion and save the image. By default, the image will be saved to wherever your _working directory_ is.

```python
MODEL_ID = "OFA-Sys/small-stable-diffusion-v0"
pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

img = pipe(args.prompt + " 4K").images[0]
img.save("output.png")
```

This will generate an image in 50 steps. This will take around a minute or less depending on your hardware.