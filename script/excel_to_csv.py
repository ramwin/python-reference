#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path

import click
import openpyxl
import pandas


def format(x):
    if isinstance(x, float):
        return f"{x:.2f}"
    if isinstance(x, int):
        return str(x)
    if x is None:
        return ""
    return str(x).replace("\n", "-").replace("\r", "-")


@click.command()
@click.argument("source")
def main(source: str) -> None:
    path = Path(source)
    wb = openpyxl.load_workbook(path, data_only=True)
    target = path.parent.joinpath(".cache" + path.stem)
    target.mkdir(exist_ok=True)
    for sheet_name in wb.sheetnames:
        with open(target.joinpath(sheet_name).with_suffix(".csv"), "w") as f:
            for row in wb[sheet_name]:
                for cell in row[:-1]:
                    f.write(format(cell.value))
                    f.write(",")
                f.write(format(row[-1].value))
                f.write("\n")
    # df_dict = pandas.read_excel(path, sheet_name=None)
    # target.mkdir(exist_ok=True)
    # for sheet_name, dataframe in df_dict.items():
    #     dataframe.to_csv(target.joinpath(sheet_name).with_suffix(".csv"),  float_format='%.2f')


if __name__ == "__main__":
    main()
