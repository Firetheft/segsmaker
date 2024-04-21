import os
import subprocess

jalanan = [
    'rm -rf ~/tmp/* ~/tmp ~/ComfyUI/models/checkpoints ~/ComfyUI/models/loras ~/ComfyUI/models/vae ~/ComfyUI/models/controlnet ~/ComfyUI/models/diffusers',
    'ln -vs /tmp ~/tmp',
    'ln -vs /tmp/checkpoints ~/ComfyUI/models/checkpoints',
    'ln -vs /tmp/loras ~/ComfyUI/models/loras',
    'ln -vs /tmp/vae ~/ComfyUI/models/vae',
    'ln -vs /tmp/controlnet ~/ComfyUI/models/controlnet',
    'ln -vs /tmp/diffusers ~/ComfyUI/models/diffusers',
    'unzip -o ~/ComfyUI/models/embeddings.zip -d ~/ComfyUI/models/embeddings'
    'rm ~/ComfyUI/models/embeddings.zip']

for janda in jalanan:
    bocil = os.path.expanduser(janda)
    subprocess.run(bocil, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)