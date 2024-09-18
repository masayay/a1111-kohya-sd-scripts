import launch
import platform
import os
import shutil
import site
import glob
import re

dirname = os.path.dirname(__file__)
repo_dir = os.path.join(dirname, "kohya_ss")


def prepare_environment():
    sd_scripts_repo = os.environ.get("SD_SCRIPTS_REPO", "https://github.com/kohya-ss/sd-scripts.git")
    requirements_file = os.environ.get("REQS_FILE", "requirements.txt")
    disable_strict_version = False

    if not os.path.exists(repo_dir):
        launch.run(
            f'{launch.git} clone {sd_scripts_repo} "{repo_dir}"'
        )

    if platform.system() == "Linux":
        if not launch.is_installed("triton"):
            launch.run_pip("install triton", "triton")

    if disable_strict_version:
        with open(os.path.join(repo_dir, requirements_file), "r") as f:
            txt = f.read()
            requirements = [
                re.split("==|<|>", a)[0]
                for a in txt.split("\n")
                if not a.startswith("#")
            ]
            requirements = " ".join(requirements)
            launch.run(
                f'cd "{repo_dir}" && "{launch.python}" -m pip install {requirements}',
                desc=f"Installing requirements for kohya sd-scripts",
                errdesc=f"Couldn't install requirements for kohya sd-scripts",
            )
    else:
        launch.run(
            f'cd "{repo_dir}" && "{launch.python}" -m pip install -r requirements.txt',
            desc=f"Installing requirements for kohya sd-scripts",
            errdesc=f"Couldn't install requirements for kohya sd-scripts",
        )

    if platform.system() == "Windows":
        for file in glob.glob(os.path.join(repo_dir, "bitsandbytes_windows", "*")):
            filename = os.path.basename(file)
            for dir in site.getsitepackages():
                outfile = (
                    os.path.join(dir, "bitsandbytes", "cuda_setup", filename)
                    if filename == "main.py"
                    else os.path.join(dir, "bitsandbytes", filename)
                )
                if not os.path.exists(os.path.dirname(outfile)):
                    continue
                shutil.copy(file, outfile)


if __name__ == "__main__":
    prepare_environment()
