import cv2
import torch
import time
import os
import pyttsx3

from PIL import Image
from transformers import pipeline


# 创建 Hugging Face 模型
classifier = pipeline('image-classification', model='google/vit-base-patch16-224', device=0)

# 创建摄像头对象
cap = cv2.VideoCapture('/dev/video0')
engine = pyttsx3.init()
engine.say('okokokok')
# 注意，没有本句话是没有声音的
engine.runAndWait()

while True:
    
    # 获取一帧图像
    ret, frame = cap.read()

    # 对图像进行预处理
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(image)

    # 使用 Hugging Face API 进行图像分类
    result = classifier(pil_image)

    # 获取预测结果
    label = result[0]['label']
    score = result[0]['score']

    # 输出预测结果
    print(f"Predicted: {label} (confidence: {score:.2f})")

    # 在图像上标注结果
    # cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 显示图像
    # cv2.imshow('image', frame)

    # 按下 q 键退出
    if cv2.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()



