# 语音对话项目

## 简介

这是一个基于python开发的语音对话项目，旨在提供一个简单易用的平台，让用户能够通过语音与计算机进行自然对话。本项目利用了先进的语音识别和自然语言处理技术，为用户提供了一个全新的交互体验。

## 功能特性

- **语音识别**：将用户的语音转换成文本。
- **自然语言理解**：分析用户意图，并生成合适的回应。
- **语音合成**：将文本信息转化为语音播放给用户。

## 技术栈

- 编程语言：python
- 主要依赖：
  - SpeechRecognition（语音识别）: iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch  
  - TTS（语音合成）: ChatTTS、MELOTTS。
  - LLM（理解和生成自然语言）：glm-4-flash、Qwen2.5。
  
## 安装指南

须配置自己的.env 文件如下：
![image](https://github.com/user-attachments/assets/dce46a3a-9210-436e-9c4e-615f02065af9)

配置后执行 python main.py

根据代码提示安装对于的python库，到顺利运行即可。

