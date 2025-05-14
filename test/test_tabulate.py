#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tabulate


def main():
    data = [
            {
                "需求REQID": "REQ12345",
                "需求用例": "Test1<br>Test2",
            },
            {
                "需求REQID": "REQ12346",
                "需求用例": "Test3<br>Test4",
            }
    ]
    with open("/mnt/d/tmp/result.html", "w") as f:
        htmlescape = tabulate.htmlescape
        # tabulate.htmlescape = lambda text: htmlescape(text).replace("\n", "<br>")
        f.write(tabulate.tabulate(
                data,
                headers="keys",
                tablefmt="unsafehtml"
        ).replace("<table>", "<table border='1'>"))


if __name__ == "__main__":
    main()
