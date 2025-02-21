#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from unittest import TestResult
import logging_config
from logging_config import logging


logger = logging.getLogger(__name__)
logging.getLogger("unittest").addHandler(logging_config.file_handler)


class Test(unittest.TestCase):

    def test_success(self):
        logger.info("成功的用例")
        self.assertEqual(1, 1)

    def test_fail(self):
        logger.info("失败的用例")
        self.assertEqual(1, 2)

    def test_error(self):
        logger.info("报错的用例")
        raise ValueError

    def tearDown(self):
        logger.info("调用teardown: %s", self._outcome.result)
        logger.info("should stop: %s", self._outcome.result.shouldStop)
        for failure in self._outcome.result.failures:
            logger.warning("存在报错: %s", failure[1])
        for error in self._outcome.result.errors:
            logger.error("存在报错: %s", failure[1])


if __name__ == "__main__":
    logger.info("开始直接测试")

    suite = unittest.TestSuite()
    suite.addTest(Test('test_error'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    logger.error(result.errors)
