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

### 1-2. 네트워크 관련 패키지 설치

    sudo apt install net-tools

### 1-3. NATS 설치

#### 1-3-1. Python 버전 확인

    python3 version

#### 1-3-2. NATS 설치

    pip install nats-py

## 2. Pi 설정

### 1-1. 기본 설정 (ㅁㄴㅇ)

update software 만 스킵하고 나머지는 다 기본 설정으로 진행합니다.

### 2-1. Pi 카메라 설정
