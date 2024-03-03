import os
import subprocess

def zzz():
    try:
        zorok = "/home/studio-lab-user/.zrok/bin"
        os.makedirs(zorok, exist_ok=True)
        subprocess.run(["curl", "-sLO", "https://github.com/openziti/zrok/releases/download/v0.4.23/zrok_0.4.23_linux_amd64.tar.gz"], check=True)
        subprocess.run(["tar", "-xzf", "zrok_0.4.23_linux_amd64.tar.gz", "-C", zorok, "--wildcards", "*zrok"], check=True)
        os.remove("zrok_0.4.23_linux_amd64.tar.gz")
        print("""
现在开始注册你的 ZROK 帐户。
复制下面这条命令：
~/.zrok/bin/zrok invite
粘贴到终端中。（如果你是新手不知道怎么打开终端，可以直接用快捷键 Ctrl+Shift+L 打开，然后找到 Terminal 点击即可）

或者你可以看这个简短的教程 https://dlink.host/sharepoint/aHR0cHM6Ly9kYW9odW8tbXkuc2hhcmVwb2ludC5jb20vOnY6L2cvcGVyc29uYWwvcnVhbmppYW5fZGFvaHVvX29ubWljcm9zb2Z0X2NvbS9FVzNTaE9aZkhvUkxtYUQwenBHanhqb0JQQzdaZ2VaWTBlZk44d3YwdUQtYWNBP25hdj1leUp5WldabGNuSmhiRWx1Wm04aU9uc2ljbVZtWlhKeVlXeEJjSEFpT2lKUGJtVkVjbWwyWlVadmNrSjFjMmx1WlhOeklpd2ljbVZtWlhKeVlXeEJjSEJRYkdGMFptOXliU0k2SWxkbFlpSXNJbkpsWm1WeWNtRnNUVzlrWlNJNkluWnBaWGNpTENKeVpXWmxjbkpoYkZacFpYY2lPaUpOZVVacGJHVnpUR2x1YTBOdmNIa2lmWDAmZT04bWdxVHQ.mp4
""")

    except Exception as e:
        print(f"An error occurred: {e}")

zzz()