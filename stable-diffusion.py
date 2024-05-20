from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe = pipe.to("cpu")

prompt = ("An english sir in his estate. The sir should appear proud. The image should also have"
          "sir's emblem which is a lion on a red background. In the background of the image the castle of the sir"
          "should be present")
image = pipe(prompt).images[0]

image.save("stable_diffusion_v_1_5_english_sir_enhanced.png")