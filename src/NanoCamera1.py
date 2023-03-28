import torch
import torchvision
import cv2

# 加载预训练的物体识别模型
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# 获取默认的COCO标签
COCO_INSTANCE_CATEGORY_NAMES = model.class_names

# 使用OpenCV打开摄像头
cap = cv2.VideoCapture('/dev/video0')

while True:
    # 读取帧
    ret, frame = cap.read()

    # 转换为PyTorch tensor格式
    tensor = torchvision.transforms.functional.to_tensor(frame)

    # 对图像进行预测
    outputs = model([tensor])

    # 遍历预测结果并标记边界框
    for i in range(len(outputs[0]['boxes'])):
        box = outputs[0]['boxes'][i]
        score = outputs[0]['scores'][i]
        label = COCO_INSTANCE_CATEGORY_NAMES[outputs[0]['labels'][i]]
        if score > 0.5:
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {score:.2f}", (int(box[0]), int(box[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(label)

    # 显示结果
    # cv2.imshow('Object Detection', frame)

    # 按下q退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()

