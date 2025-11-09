import os
import shutil

def transcode_variants(original_path: str, ffmpeg_path: str):
    base = os.path.splitext(original_path)[0]
    outputs = {
        "Original": original_path,
        "1080p": f"{base}_1080p.mp4",
        "720p": f"{base}_720p.mp4",
        "480p": f"{base}_480p.mp4",
    }
    for k, v in outputs.items():
        if k == "Original":
            continue
        shutil.copyfile(original_path, v)
    return outputs
