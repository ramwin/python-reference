
## pyenv

### 安装

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc  # 让系统有pyenv
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc  # 让系统能优先读取pyenv的变量
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
pyenv install 3.7.5  # 安装指定版本的系统
如果下载不下来，可以
cd .pyenv/cache/
wget https://cdn.npm.taobao.org/dist/python/3.7.5/Python-3.7.5.tar.xz
然后在 pyenv install 3.7.5
然后在你需要设置的目的下创建
echo "3.7.5" > .python-version
最后，在path里添加, 这个是每次都校验
if command -v pyenv 1>/dev/null 2>&1; then  
  eval "$(pyenv init -)"  
fi
实际上，只要运行 eval "$(pyenv init -)"就可以
```
