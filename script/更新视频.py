"""
自动更新电视剧. 读取配置文件config.json
config.json [
    {
        "source": "复制视频的文件夹",
        "target": "复制到的文件夹",
        "current": "当前复制的最后一个文件的文件名",
        "max": 3, 最多复制多少集
    }
]
"""

import json
import logging
from pathlib import Path
import shutil

import filetype


CONFIG_FILE = "C:/Users/wangx/局域网/config.json"
logging.basicConfig(
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s",
    filename="info.log",
    encoding="utf-8")


class MoveTask:
    """
    从source拷贝文件到target, 直到达到 max_数量
    """

    def __init__(self, source: Path, target: Path, current: str, max_: int):
        self.source = Path(source)
        self.target = Path(target)
        self.max_ = max_
        self.current = current

    def run(self) -> str:
        """返回最后一个复制的文件"""
        cnt = self.get_target_cnt()
        if cnt >= self.max_:
            return None
        remain = self.get_source_files()
        if not remain:
            logging.error("%s看完了, 请删除配置", self.source)
            return None
        for file_path in remain[0:self.max_-cnt]:
            source = self.source.joinpath(file_path.name)
            target = self.target.joinpath(file_path.name)
            logging.info("%s => %s", source, target)
            shutil.copyfile(source, target)
            logging.info("复制完成")
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
        return path.is_file() and filetype.video_match(path)


def main():
    logging.info("开始运行")
    with open(CONFIG_FILE, encoding="utf-8") as f:
        info = json.load(f)

    for item in info:
        new_current = MoveTask(
            source=item["source"],
            target=item["target"],
            current=item["current"],
            max_=item["max"]
        ).run()
        if new_current is not None:
            item["current"] = new_current

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4,
                  ensure_ascii=False)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception(e)
        logging.error("执行报错")
        raise
