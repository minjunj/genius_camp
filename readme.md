# 2024년 영재캠프 NUC to PI MQ .feat NATS

## 환경 설정

### ubuntu 24.04LTS (Not WSL)<br>

### rasberry pi 4B 2024년 3월 15일 릴리즈 Raspberry Pi OS with desktop

---

이번 세션에서는 ssh 를 통한 원격 접속은 사용하지 않습니다.

## Step 0. 시작하기 앞서..

# 모든 명령어는 ~ 에서 진행됩니다.

# Step 1. 환경설정

## 1. NUC에 ubuntu 24.04 설치

#### 1-1. 기본 설치

    sudo apt-get update && sudo apt-get upgrade -y

#### 1-2. 기본 패키지 설치

    sudo apt install net-tools

    sudo apt install vim

    sudo apt install git

## 2. 라즈베리파이 기본 설정

#### 2-1. 기본 설정

update software 만 스킵하고 나머지는 다 기본 설정으로 진행합니다.

#### 2-2. 기본 패키지 설치

    sudo apt-get update && sudo apt-get upgrade -y

    sudo apt-get install net-tools

    sudo apt-get install vim

    sudo apt-get install git

#### 2-3. 레포지토리 다운

    git clone https://github.com/minjunj/genius_camp.git

# Step 2. PI Camera 설정 (라즈베리 파이에서 진행)

## 1. Pi 카메라 장착

    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2

카메라를 꼽으면 재부팅 시켜줍니다.<br>

- 해당 버전(24년 3월 15일 릴리즈 기준) 부터는 따로 설정이 사라지고 알아서 잡고, 라이브러리 다운로드를 하는 듯합니다. 기존 picamera가 deprecated 되면서 picamera2로 올라감.

## 2. PI Camera 테스트

#### 2-1. PI Camera 라이브러리 다운로드

    sudo apt install -y python3-picamera2

#### 2-2. PI Camera 테스트

    python3 genius_camp/pi/camera.py

# Step 3. 라즈베리파이에서 NATS 설정하기

## 1. PI NATS Publish

## 2. NATS 라이브러리 설치

    sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
    pip3 install nats-py

## 3. NATS 테스트 (라즈베리파이에서)

테스트를 위한 파일 실행

    python3 genius_camp/pi/nats-test.py

아래와 같이 응답이 온다면 정상<br>
`Received: Msg(_client=<nats client v2.4.0>, subject='foo', reply='', data=b'Hello from Python!', headers=None, _metadata=None, _ackd=False, _sid=1)`

NUC에서 작동 확인을 위해 아래의 파일을 실행시켜 두기

    python3 genius_camp/pi/nats-main.py

# Step 4. NUC에서 NATS 설정하기

### 1. NUC NATS Publish

## 2. 라이브러리 설치

    sudo apt install python3-pip

    sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED

    pip install nats-py

    sudo pip install pillow --upgrade

    sudo apt-get install python3-tk

    sudo apt install -y libatlas-base-dev

    sudo pip3 install opencv-python

    sudo pip3 install -U numpy

## 3. 레포지토리 다운

    git clone https://github.com/minjunj/genius_camp.git

## 4. NATS 테스트 (NUC에서)

테스트를 위한 파일 실행

    python3 genius_camp/nuc/nats-test.py

- 반드시 Step 3-3. 의 마지막 명령어가 실행되어있는 상태에서 해주세요.

# Step 5. 라즈베리 파이로 부터 영상 전송

## \* 지금까지 실행시킨 .py 들은 모두 control + c 로 정지 시켜주세요.

### 라즈베리파이에서 실행

    python3 genius_camp/pi/result.py --subject {원하는 이름}

### NUC에서 실행

    python3 genius_camp/nuc/result.py --subject {원하는 이름}

### 라즈베리파이에서 먼저 실행시키지 않으면 NUC에서 작동 되지 않습니다.

# Step 6. pi 카메라 객체 인식

## PI에서

    python3 genius_camp/pi/result.py --subject {원하는 이름}

## NUC에서

    cd genius_camp/nuc/object-detect
    python3 video_object_detection.py --subject {원하는 이름}
