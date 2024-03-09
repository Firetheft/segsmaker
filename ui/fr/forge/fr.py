import os
import subprocess

jalanan = [
    'rm -rf ~/tmp/* ~/tmp ~/stable-diffusion-webui-forge/models/Stable-diffusion/tmp_models ~/stable-diffusion-webui-forge/models/Lora/tmp_Lora ~/stable-diffusion-webui-forge/models/ControlNet ~/stable-diffusion-webui-forge/models/svd ~/stable-diffusion-webui-forge/models/z123',
    'mkdir -p ~/stable-diffusion-webui-forge/models/Lora',
    'mkdir -p ~/stable-diffusion-webui-forge/models/ESRGAN',
    'ln -vs /tmp ~/tmp',
    'ln -vs /tmp/models ~/stable-diffusion-webui-forge/models/Stable-diffusion/tmp_models',
    'ln -vs /tmp/svd ~/stable-diffusion-webui-forge/models/svd',
    'ln -vs /tmp/z123 ~/stable-diffusion-webui-forge/models/z123',
    'ln -vs /tmp/Lora ~/stable-diffusion-webui-forge/models/Lora/tmp_Lora',
    'ln -vs /tmp/ControlNet ~/stable-diffusion-webui-forge/models/ControlNet']

for janda in jalanan:
    bocil = os.path.expanduser(janda)
    subprocess.run(bocil, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)