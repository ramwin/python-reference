#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
加密整个文件夹
"""


import base64
import getpass
import hashlib
import logging
import os
from pathlib import Path
from typing import List

import click
from cryptography.fernet import Fernet


logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler()])
LOGGER = logging.getLogger(__name__)


def check_password(password: str) -> None:
    """
    为了方便，只输入一次密码
    为了防止密码输入错误，所以要和已有的密码比对
    """
    valid_password_hash: List[str] = [
    ]
    check_salt = "check_pass:"
    md5 = hashlib.md5()
    md5.update((check_salt+password).encode("UTF-8"))
    if md5.hexdigest() not in valid_password_hash:
        LOGGER.error("输入密码和以前的不一致.")
        LOGGER.error("如果确认要用这个密码,请再次执行一遍确认md5一致后,把 %s 添加到valid_password_hash",
                     md5.hexdigest())
        raise ValueError("输入的密码和以前的不一致")


def get_key() -> Fernet:
    """用户输入密码，加盐后生成新的密码"""
    password = getpass.getpass("输入密码:")
    check_password(password)
    md5 = hashlib.md5()
    salt = "加密文件:"
    md5.update(salt.encode("UTF-8"))
    md5.update(password.encode("UTF-8"))
    password = md5.hexdigest()
    return Fernet(base64.urlsafe_b64encode(password.encode("utf-8")))


def encrypt_file(path: Path, fernet: Fernet):
    """
    加密文件
    添加.fernet后缀
    删除原文件
    """
    target_path = path.parent.joinpath(path.name + ".fernet")
    if target_path.exists():
        raise FileExistsError(target_path)
    with open(path, "rb") as source_file:
        content = source_file.read()
    encrypted_content = fernet.encrypt(content)
    with open(target_path, "wb") as target_file:
        target_file.write(encrypted_content)
    path.unlink()


@click.command()
@click.argument("path")
def main(path):
    """
    加密文件夹或者文件
    """
    fernet = get_key()
    if Path(path).is_file():
        encrypt_file(Path(path), fernet)
        return
    for _, _, files in os.walk(path):
        for path_str in files:
            path = Path(path_str)
            if path.suffix == ".fernet":
                continue
            encrypt_file(path, fernet)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
