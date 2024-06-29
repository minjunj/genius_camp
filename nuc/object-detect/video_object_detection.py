import os
import argparse
import cv2
import numpy as np
import nats
import io
import asyncio
from object_detection_functions import YOLOModel, read_classes, show_detected_objects


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight_path", type=str, default="./yolov3-tiny.weights")
    parser.add_argument("--cfg_path", type=str, default="./yolov3-tiny.cfg")
    parser.add_argument("--class_path", type=str, default="./coco.names")
    parser.add_argument("--subject", default='pc23')
    args = parser.parse_args()

    # Model 정의
    print("모델을 로딩합니다... ")
    model = YOLOModel(args.weight_path, args.cfg_path)
    print("모델 로딩이 완료되었습니다")

    # Connect to NATS
    nc = await nats.connect("demo.nats.io")
    sub = await nc.subscribe(args.subject)
    classes = read_classes(args.class_path)
    
    print("객체 검출을 시작합니다. 이미지 창에서 esc 버튼을 누르면 종료합니다.")

    try:
        while True:
            # Wait for a message

            msg = await sub.next_msg()
            # Decode JPEG frame
            buffer = io.BytesIO(msg.data)
            img_array = np.frombuffer(buffer.getvalue(), dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            # Display the frame
            cv2.imshow("NATS Video Stream", img)

            outs = model.inference(image)
            show_detected_objects(image, outs, classes, threshold=0.4)

            # Exit if Esc is pressed
            if cv2.waitKey(1) == 27:
                break
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, exiting...")
    except:
        pass
    
    print("객체 검출을 종료합니다")

if __name__ == "__main__":
    asyncio.run(main())