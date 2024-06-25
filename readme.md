# 2024년 영재캠프 NUC to PI MQ .feat NATS

## 환경 설정

### ubuntu 24.04 (Not WSL)<br>

### rasberry pi 4B 2024년 3월 15일 릴리즈 Raspberry Pi OS with desktop

---

이번 세션에서는 ssh 를 통한 원격 접속은 사용하지 않습니다.

# Step 1. 환경성정

## 1. NUC에 ubuntu 24.04 설치

### 1-1. 기본 설치

    sudo apt-get update && sudo apt-get upgrade -y

### 1-2. 기본 패키지 설치

    sudo apt install net-tools

    sudo apt install vim

    sudo apt install git

### 1-3. NATS 설치

#### 1-3-1. Python 버전 확인

    python3 version

#### 1-3-2. NATS 설치

    pip install nats-py

## 2. Pi 설정

### 2-1. 기본 설정

update software 만 스킵하고 나머지는 다 기본 설정으로 진행합니다.

### 2-2. 기본 패키지 설치

    sudo apt-get update && sudo apt-get upgrade -y # 패키지 업데이트 과정이 꽤 오래걸림.

    sudo apt-get install net-tools

    sudo apt-get install vim

    sudo apt-get install git

### 2-3. 레포지토리 다운

    git clone https://github.com/minjunj/genius_camp.git

### 2-4. Pi 카메라 설정

    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2

카메라를 꼽으면 재부팅 시켜줍니다.<br>

- 해당 버전(24년 3월 15일 릴리즈 기준) 부터는 따로 설정이 사라지고 알아서 잡고, 라이브러리 다운로드를 하는 듯합니다. 기존 picamera가 deprecated 되면서 picamera2로 올라감.

### 2-5. PI Camera 테스트

#### 2-5-1. PI Camera 라이브러리 다운로드

    sudo apt install -y python3-picamera2

#### 2-5-2. PI Camera 테스트

    python3 genius_camp/pi/camera.py

### 2-6. PI NATS Produce

#### 2-6-1. NATS 라이브러리 설치

    sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
    pip3 install nats-py

#### 2-6-2. NATS 테스트
