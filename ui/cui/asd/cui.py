import subprocess
import os

minyak = [
    ['rm', '-rf', '~/tmp/*', '~/tmp', '~/ComfyUI/models/checkpoints/tmp_models', '~/ComfyUI/models/loras/tmp_Lora', '~/ComfyUI/models/vae/tmp_vae', '~/ComfyUI/models/controlnet', '~/ComfyUI/models/diffusers'],
    ['ln', '-vs', '/tmp', '~/tmp'],
    ['ln', '-vs', '/tmp/models', '~/ComfyUI/models/checkpoints/tmp_models'],
    ['ln', '-vs', '/tmp/Lora', '~/ComfyUI/models/loras/tmp_Lora'],
    ['ln', '-vs', '/tmp/vae', '~/ComfyUI/models/vae/tmp_vae'],
    ['ln', '-vs', '/tmp/ControlNet', '~/ComfyUI/models/controlnet'],
    ['ln', '-vs', '/tmp/diffusers', '~/ComfyUI/models/diffusers'],
    ['unzip', '-o', '~/ComfyUI/models/embeddings.zip', '-d', '~/ComfyUI/models/embeddings'],
    ['rm', '~/ComfyUI/models/embeddings.zip']
]

for tepung in minyak:
    gorengan = [os.path.expanduser(arg) for arg in tepung]
    subprocess.run(gorengan, check=True)
