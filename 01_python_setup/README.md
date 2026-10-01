## 题目说明

本题要求你在 Windows 下安装 Python 3.10，为后续题目（图片识别、脚本运行）准备好运行环境。

> **如果你的电脑已经安装过 Python 3.8 及以上版本**，可以直接跳过本题，无需重新安装。执行 `python --version` 确认当前版本号即可。

## 1. 下载安装包

前往 Python 官方下载页面，选择 **3.10.x** 版本（不要选择 3.11 及以上，也不要选择 3.9 及以下）：

```text
https://www.python.org/downloads/release/python-3100/
```

在页面底部找到 **Windows installer (64-bit)**，下载 `python-3.10.x-amd64.exe`。

## 2. 安装

双击运行安装包，注意以下两点：

1. **勾选 “Add python.exe to PATH”**（安装界面底部的复选框），这样安装完成后可以直接在命令行使用 `python` 命令。
2. 点击 **Install Now** 完成默认安装即可，无需修改其他选项。

## 3. 验证安装

安装完成后，打开一个新的 CMD 或 PowerShell 窗口（必须是新打开的，已经打开的窗口不会读取到新的 PATH），执行：

```text
python --version
pip --version
```

确认输出的版本号是 `Python 3.10.x`。如果提示找不到命令，检查安装时是否勾选了 “Add python.exe to PATH”，或重新安装一次。

## 常见问题

- **安装完 `python --version` 提示找不到命令：** 大概率是安装时没有勾选 “Add to PATH”。可以重新运行安装包，选择 “Modify”，勾选该选项。
- **系统里已经装了其他版本的 Python：** 建议先确认 `python --version` 输出的是 3.10.x；如果不是，检查是否有多个 Python 版本导致 PATH 顺序冲突。
