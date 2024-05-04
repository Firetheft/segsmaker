import subprocess
import os

minyak = [
    ['rm', '-rf', '~/tmp/*', '~/tmp', '~/ComfyUI/models/checkpoints', '~/ComfyUI/models/loras', '~/ComfyUI/models/vae', '~/ComfyUI/models/controlnet', '~/ComfyUI/models/diffusers'],
    ['mkdir', '-p', '~/stable-diffusion-webui-forge/models/ipadapter'],
    ['ln', '-vs', '/tmp', '~/tmp'],
    ['ln', '-vs', '/tmp/checkpoints', '~/ComfyUI/models/checkpoints'],
    ['ln', '-vs', '/tmp/loras', '~/ComfyUI/models/loras'],
    ['ln', '-vs', '/tmp/vae', '~/ComfyUI/models/vae'],
    ['ln', '-vs', '/tmp/controlnet', '~/ComfyUI/models/controlnet'],
    ['ln', '-vs', '/tmp/diffusers', '~/ComfyUI/models/diffusers'],
    ['unzip', '-o', '~/ComfyUI/models/embeddings.zip', '-d', '~/ComfyUI/models/embeddings'],
    ['rm', '~/ComfyUI/models/embeddings.zip']
]

for tepung in minyak:
    gorengan = [os.path.expanduser(arg) for arg in tepung]
    subprocess.run(gorengan, check=True)
