# Aim
這個 repository 的 目的是記錄 ffmpeg 的語法例子。

The aim of this repository is to store ffmpeg's code examples.

# pre-requisite
- [ ] `ffmpeg.exe`. ffmpeg shall be downloaded from [FFmpeg](https://ffmpeg.org/download.html#build-windows).
- [ ] A little bit Windows Command line knowledge.


# Examples
以下的例子會以一問一答的方式呈現。程式碼會顥示在程式碼框內，程式中變數會用角括號包裹，例如`<變數>`，只要將變數替換就可。

**Question: How to check current ffmpeg version? (如何查詢當前 ffmpeg 的版本?)**
``` cmd
> ffmpeg -version
```


**Q**: What is the basic syntax of ffmpeg? (ffmpeg 基本語法結構)

**A**: `ffmpeg -i input.mp4 output.avi`
每個輸入參數用 <空格> 分開，如果輸入參數中有空格，用引數包裹(例如:folder name has space in between).
