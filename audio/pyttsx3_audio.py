import pyttsx3
import os


def text_to_speech(text, output_file="output.mp3"):
    # 初始化语音引擎
    engine = pyttsx3.init()

    # 设置参数（可选）
    engine.setProperty('rate', 150)  # 语速（字/分钟，可调）
    engine.setProperty('volume', 0.8)  # 音量（0.0 ~ 1.0）

    # 选择语音（中文或英文）
    voices = engine.getProperty('voices')
    # 使用中文语音（Windows 示例）
    for voice in voices:
        if "Microsoft Mandarin" in voice.name:
            engine.setProperty('voice', voice.id)
            break

    # 生成语音并保存
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    # 播放音频（Windows 系统示例）
    os.system(f"start {output_file}")  # Windows
    # macOS: os.system(f"afplay {output_file}")
    # Linux: os.system(f"xdg-open {output_file}")


if __name__ == "__main__":
    input_text = input("请输入要转语音的文本：")
    text_to_speech(input_text)
