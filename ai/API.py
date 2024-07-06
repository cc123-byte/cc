import requests
import base64
import cv2 as cv


# 车辆检测接口
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.21307ba36106483485c5fea146d34bd4.2592000.1722686404.282335-89983801'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        num = data['vehicle_num']['car']
        for item in data['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
        # 定义要绘制的文字
            text = item['type']
            position = (x1, y1-2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # 红色
            thickness = 2
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
            # cv.imshow('Rectangle', img)
            # return img
    return img, num


    #人流量统计接口
def person_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.f76289cfc91c1df6003bfe3e6f092da3.2592000.1722741578.282335-90912586'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num1 = 0
    if response:
        data = response.json()
        num1 = data['person_num']
        # 定义要绘制的文字
        text = 'num'
        position = (0, 0)
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (0, 0, 255)  # 红色
        thickness = 2
        img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
    return num1

# 等待按键，然后关闭窗口
    # cv.waitKey(0)
    # cv.destroyAllWindows()

