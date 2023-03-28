import pyttsx3

# 初始化语音合成引擎
engine = pyttsx3.init()

# 设置要朗读的文本
text = 'Hello, world!'

# 使用语音合成引擎朗读文本
engine.say(text)

# 等待朗读完成
engine.runAndWait()
