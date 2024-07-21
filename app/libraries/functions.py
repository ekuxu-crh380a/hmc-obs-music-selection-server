import os


def is_nvidia_surround() -> bool:
    return True if os.environ.get('USE_NVIDIA_SURROUND') == 'true' else False
