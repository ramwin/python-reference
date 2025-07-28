#!/usr/bin/env python3
import os
from pathlib import Path

import click
from docx import Document


def convert_docx_to_markdown(docx_path, markdown_path):
    """将单个 Word 文档转换为 Markdown 文件"""
    doc = Document(docx_path)
    markdown_content = []
    
    for paragraph in doc.paragraphs:
        style = paragraph.style.name
        
        if style.startswith('Heading'):
            level = int(style[-1])
            markdown_heading = '#' * level
            markdown_content.append(f"{markdown_heading} {paragraph.text}")
        else:
            markdown_content.append(paragraph.text)
    
    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))

@click.command()
@click.argument('filenames', nargs=-1)
@click.option('--verbose', is_flag=True, help='显示详细信息')
def main(filenames, verbose):
    """批量将 Word 文档 (.docx) 转换为 Markdown 文件 (.md)"""
    if not filenames:
        click.echo("请提供至少一个 Word 文件路径！")
        return
    
    for filename in filenames:
        if not os.path.exists(filename):
            click.echo(f"文件 {filename} 不存在！")
            continue
        
        if not filename.lower().endswith('.docx'):
            click.echo(f"文件 {filename} 不是 Word 文档（.docx）！")
            continue
        
        # 生成输出文件路径
        output_path = Path(filename).parent.joinpath(
                ".markdown", filename
        ).with_suffix(".md")
        output_path.parent.mkdir(exist_ok=True)
        
        if verbose:
            click.echo(f"正在处理文件：{filename}")
            click.echo(f"输出文件路径：{output_path}")
        
        try:
            convert_docx_to_markdown(filename, output_path)
            if verbose:
                click.echo(f"转换完成！已保存为：{output_path}")
        except Exception as e:
            click.echo(f"处理文件 {filename} 时出错：{str(e)}")

if __name__ == '__main__':
    main()
