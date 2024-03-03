import subprocess
import os

minyak = [
    ['rm', '-rf', '~/tmp/*', '~/tmp', '~/stable-diffusion-webui-forge/models/Stable-diffusion/tmp_models', '~/stable-diffusion-webui-forge/models/Lora/tmp_Lora', '~/stable-diffusion-webui-forge/models/ControlNet'],
    ['mkdir', '-p', '~/stable-diffusion-webui-forge/models/Lora'],
    ['mkdir', '-p', '~/stable-diffusion-webui-forge/models/ESRGAN'],
    ['ln', '-vs', '/tmp', '~/tmp'],
    ['ln', '-vs', '/tmp/models', '~/stable-diffusion-webui-forge/models/Stable-diffusion/tmp_models'],
    ['ln', '-vs', '/tmp/Lora', '~/stable-diffusion-webui-forge/models/Lora/tmp_Lora'],
    ['ln', '-vs', '/tmp/ControlNet', '~/stable-diffusion-webui-forge/models/ControlNet']
    ['ln', '-vs', '/tmp/svd', '~/stable-diffusion-webui-forge/models/svd/tmp_svd']
]

for tepung in minyak:
    gorengan = [os.path.expanduser(arg) for arg in tepung]
    subprocess.run(gorengan, check=True)
