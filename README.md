# 인공지능 객체 인식 및 스티칭을 이용한 농촌 CCTV관리 플랫폼
![시연영상](https://user-images.githubusercontent.com/71459076/179457519-234acee4-494a-45f9-82bc-4a9126fbfa1a.PNG)
![시연영상1](https://user-images.githubusercontent.com/71459076/179457503-c4b86558-5682-4d79-9787-5a650ce90b5e.PNG)
![시연영상2](https://user-images.githubusercontent.com/71459076/179457513-91559e51-5c40-4ab1-a528-36519698cb16.PNG)

- 🏆 제5회 광운대학교 산학연계 SW프로젝트 우수상 수상작 
- 참여업체 - (주)세가온



## 소개
비교적 CCTV 감시 체계가 잡혀있지 않은 농촌의 치명적인 문제점인 유해 동물 농작물 침입을 해결하고자 한 대의 움직이는 CCTV를 이용하여 적은 비용으로 최대 효율을 낼 수 있는 플랫폼 개발
## 팀 - 5Light(오광)
- [황도경](https://github.com/Dokyung-Hwang)
- [김충섭](https://github.com/kchs94)
- [임채명](https://github.com/LimLight94)
- [박종서](https://github.com/jj441)
- [한성범](https://github.com/winterbeom)

## 영상처리 순서도
![스크린샷 2021-11-04 오후 10 10 46](https://user-images.githubusercontent.com/49181228/140319359-cc5aeca9-abb6-4e81-a483-5227a4cb81ed.png)


## 시연 영상
https://user-images.githubusercontent.com/49181228/140323151-ca7d25a7-8d62-454b-9cdc-fe51b617d9f6.mp4

## 기능
#### [영상처리](https://github.com/LimLight94/5Light_ImageProcessing)
- Video Panorama - 입력으로 들어오는 video의 연속된 프레임을 한 장의 큰 화면으로 합쳐서 보여주는 기능
- Object Detection - Yolo v4-tiny 모델을 사용하여 학습된 물체의 확률을 계산한 뒤, 영상 내에 있는 제일 확률이 높은 물체를 인식해 출력해주는 기능
- Panorama Detection - Video Panorama + Object Detection로, 하나의 큰 화면을 만드는 동시에, 영상 내에 있는 물체를 인식하는 기능
#### Server
- 로그인 및 회원가입 - 유저 정보를 받아 회원가입 및 로그인 기능
- 영상 이벤트 수신 - http 통신을 통해 영상 이벤트를 수신하고 보여줌
- Push 알림 - FCM(Firebase Cloud Messaging)을 통해 영상 이벤트 발생 시 푸시 알람 기능

## 적용 기술
- Django
- MySQL
- AWS - EC2, RDS
- FCM

### Library
- OpenCV-contrib-python(4.5.2.52)
- OpenCV-Python(4.5.2.52)
- YOLO(v4)
- imutils(0.5.4)
- Numpy(1.20.3)


## License
```
Copyright 2021 5Light

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
