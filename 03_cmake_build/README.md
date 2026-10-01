请在 Windows 下完成。

## 1. 解压 CMake、MinGW 和题目工程

如果你已经配置好了g++和cmake,可以跳过这一步

将提供的 CMake 和 MinGW 压缩包完整解压到一个**完整路径不包含空格和中文字符**的位置。例如：

```text
C:\DevTools\cmake
C:\DevTools\mingw64
```

解压后，确认能找到以下文件：

```text
C:\DevTools\cmake\bin\cmake.exe
C:\DevTools\mingw64\bin\g++.exe
C:\DevTools\mingw64\bin\mingw32-make.exe
```

压缩包可能自带一层文件夹，请以实际位置为准。保留工具包的完整目录结构，不要只复制其中的 exe 文件。

**第一个空**：
解压题目文件，在这个目录下打开cmd或者powershell，输入
cmake --version
或者
g++ --version
把这时候的输出复制出来作为答案(hint: 这一步一般是一个错误输出)

## 2. 通过命令行添加 PATH

PATH 用来告诉终端去哪些目录寻找命令。需要添加的是上述工具的 **`bin` 目录**。

**注意**：下面的C:\DevTools\cmake\bin;C:\DevTools\mingw64\bin;应当根据g++和cmake.exe所在位置的实际情况确定，不能直接复制粘贴过来


下面分别给出 CMD 和 PowerShell 的操作方法，选择你正在使用的终端对应的一种。将示例路径替换成你的实际路径。

如果你用的是cmd,就执行：
```bat
set "PATH=C:\DevTools\cmake\bin;C:\DevTools\mingw64\bin;%PATH%"
```


如果你用的是powershell,就执行：
```powershell
$env:Path = "C:\DevTools\cmake\bin;C:\DevTools\mingw64\bin;" + $env:Path
```


以上命令保留原有 PATH，添加的内容**仅在当前终端及其启动的程序中生效**，足以完成本题。后续操作请继续使用同一个终端窗口；关闭后重新打开终端，需要重新执行对应命令。两种终端的 PATH 命令不能混用。

在当前终端执行以下命令，CMD 和 PowerShell 均可使用：

```text
cmake --version
g++ --version
```

确认前三条命令找到的是你刚解压的工具，后三条命令能正常显示版本。如果找到多个路径，检查第一项是否为本题工具所在位置。

## 3. 在 CMakeLists.txt 中填写学号

用文本编辑器打开题目文件中的 `CMakeLists.txt`，找到：

```cmake
set(STUDENT_ID "请填写自己的学号")
```

将引号内的内容替换为自己的完整学号，例如：

```cmake
set(STUDENT_ID "2026000042")
```

保留英文双引号，学号只填写数字，然后保存文件。

## 4. 配置并编译

回到刚才配置好 PATH 的终端，进入题目目录。

CMD 使用：

```bat
cd /d C:\freshman-task
```

PowerShell 使用：

```powershell
Set-Location C:\freshman-task
```

将示例路径替换为你的题目工程实际位置。确认当前目录下有 `CMakeLists.txt`，然后依次执行以下命令，两种终端均适用：

```text
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build
```

## 5. 运行程序

编译成功后，在同一个终端执行：

```text
.\build\challenge.exe
```

程序会显示你填写的学号和一个结果数字，然后等待回车。记录结果后，按回车退出。

**第二个空**：将程序的输出复制出来作为第二个空的答案

如果修改了学号，请保存 `CMakeLists.txt`，重新执行第 4 步的两条 CMake 命令，再运行程序。

**第三个空**：根据1-3中的操作，理解一下PATH的作用，可以问ai,但是这道题必须用自己的话一句话总结出来

## 常见问题

- **提示命令无法识别或找不到命令：** 检查解压位置和 PATH 中的 `bin` 路径是否一致，并确认在当前终端执行过对应的 PATH 命令。
- **提示学号不正确：** 检查 `STUDENT_ID` 是否已替换为完整的纯数字学号，并保存文件。
- **提示缺少 `lib/challenge.o`：** 检查题目是否完整解压；缺失时联系出题人。
- **更换编译器或生成器后配置失败：** 使用新的构建目录，例如将配置命令里的 `-B build` 改为 `-B build-new`，后续编译和运行路径也相应改为 `build-new`。