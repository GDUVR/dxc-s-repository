from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

import cv2

#请仔细阅读以下代码，发现并修改需要自行填写的部分，确保代码可以正常运行。
                                                                                                                                                                                                           
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".bmp"}  
FOLDER_PATH = r"C:\Users\ROG\Downloads\Recruitment_Test\Recruitment_Test\02_image_recognition\generated_images"


def image_paths(folder: Path) -> Iterable[Path]:
    """Yield supported image files directly inside *folder*."""
    return (
        path
        for path in sorted(folder.iterdir())
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def is_green_dominant(path: Path) -> bool:
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"无法读取图片：{path}")

    blue, green, red = cv2.split(image)
    green_pixels = (green > red) & (green > blue)
    red_pixels = (red > green) & (red > blue)
    blue_pixels = (blue > red) & (blue > green)
    return int(green_pixels.sum()) > max(
        int(red_pixels.sum()), int(blue_pixels.sum())
    )


def count_green_dominant_images(folder: Path) -> int:
    if not folder.is_dir():
        raise NotADirectoryError(f"文件夹不存在：{folder}")

    paths = list(image_paths(folder))
    if not paths:
        raise ValueError(f"文件夹中没有找到支持的图片：{folder}")

    green_dominant_images = []
    total = len(paths)
    for index, path in enumerate(paths, start=1):
        green_dominant_images.append(is_green_dominant(path))
        width = 30
        completed = int(width * index / total)
        bar = "#" * completed + "-" * (width - completed)
        sys.stdout.write(
            f"\r识别进度: [{bar}] {index}/{total} ({index / total:.1%})"
        )
        sys.stdout.flush()

    print()
    return sum(green_dominant_images)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="根据指定的图片文件夹内容生成答案"
    )
    parser.add_argument(
        "folder",
        type=Path,
        nargs="?",
        help="图片文件夹路径",
    )
    args = parser.parse_args()

    folder = args.folder or (Path(FOLDER_PATH) if FOLDER_PATH else None)
    if folder is None:
        parser.error("请先在 run.py 的 FOLDER_PATH 中填写图片文件夹路径")

    count = count_green_dominant_images(folder)
    print(f"你的答案是：{count}")


if __name__ == "__main__":
    main()
