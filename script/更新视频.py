"""
自动复制一个文件夹的视频到另外一个文件夹.
另外一个文件夹会触发syncthing来同步到我们平板和手机
配置文件config.json
config.json [
    {
        "Linux": {
            "source_device": "/run/media/wangx/software/",
            "target_device": "/run/media/wangx/samsung/"
        },
        "Windows": {
            "source_device": "W:",
            "target_device": "S:"
        },
        "folder": {
            "source": "复制视频的文件夹",
            "target": "复制到的文件夹",
        },
        "current": "当前复制的最后一个文件的文件名",
        "max": 3, 最多复制多少集
    },
]
"""

import json
import logging
import platform
import shutil
from pathlib import Path

import filetype
from flockcontext import FlockOpen


logging.basicConfig(
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s",
    filename="info.log",
    encoding="utf-8")
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())


if platform.system() == "Windows":
    DEVICE = Path("S:/")
    DEVICE_KEY = "windows_device"
elif platform.system() == "Linux":
    DEVICE = Path("/run/media/wangx/samsung")
    DEVICE_KEY = "linux_device"

CONFIG_FILES = [
        DEVICE.joinpath("局域网/config.json"),
        DEVICE.joinpath("共享给小米平板5/config.json"),
]


class MoveTask:
    """
    从source拷贝文件到target, 直到达到 max_数量
    """

    def __init__(self,  # pylint: disable=too-many-arguments
                 source: Path, target: Path,
                 current: str, max_: int,
                 create_link=False
                ):
        self.source = Path(source)
        self.target = Path(target)
        self.target.mkdir(parents=True, exist_ok=True)
        self.max_ = max_
        self.current = current
        self.create_link = create_link

    def run(self) -> str:
        """返回最后一个复制的文件"""
        cnt = self.get_target_cnt()
        if cnt >= self.max_:
            return None
        remain = self.get_source_files()
        if not remain:
            LOGGER.error("%s看完了, 请删除配置", self.source)
            return None
        file_path = None
        for file_path in remain[0:self.max_-cnt]:
            source = self.source.joinpath(file_path.name)
            target = self.target.joinpath(file_path.name)
            LOGGER.info("%s => %s", source, target)
            if source.is_file():
                if self.create_link:
                    target.hardlink_to(source)
                else:
                    shutil.copyfile(source, target)
            else:
                shutil.copytree(source, target)
            LOGGER.info("复制完成")
        if file_path is None:
            return None
        return file_path.name

    def get_target_cnt(self):
        """
        获取目标文件夹当前的视频数量
        """
        return len([
            f
            for f in self.target.iterdir()
            if self.is_video(f)
        ])

    def get_source_files(self):
        """
        获取源文件夹没有看过的视频列表
        """
        all_video_files = [
            f
            for f in self.source.iterdir()
            if self.is_video(f) and f.name > self.current
        ]
        return sorted(all_video_files)

    @staticmethod
    def is_video(path):
        """判断一个文件是否是视频文件或者是否是文件夹"""
        return path.is_dir() or filetype.video_match(path)


def main():
    """运行"""
    LOGGER.info("开始运行")
    for config_file in CONFIG_FILES:
        with open(config_file, encoding="utf-8") as f:
            info = json.load(f)

        for item in info:
            if platform.system() not in item:
                LOGGER.warning("还有没有迁移的文件夹: %s", item)
                continue
            source_device = item[platform.system()]["source_device"]
            target_device = item[platform.system()]["target_device"]
            new_current = MoveTask(
                    source=Path(source_device, item["folder"]["source"]),
                    target=Path(target_device, item["folder"]["target"]),
                    current=item["current"],
                    max_=item["max"],
                    create_link=source_device==target_device,
            ).run()
            if new_current is not None:
                item["current"] = new_current

        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4,
                      ensure_ascii=False)


if __name__ == "__main__":
    try:
        with FlockOpen("更新视频.lock", "w", timeout=300) as lock:
            main()
    except Exception as e:
        logging.exception(e)
        logging.error("执行报错")
        raise
