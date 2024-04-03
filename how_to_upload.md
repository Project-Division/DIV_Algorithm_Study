# GITHUB UPLOAD

## 1. GIT 설치

- ### [설치 파일 다운로드](https://git-scm.com/downloads)
- ### GIT 설치 방법은 다루지 않겠습니다. 검색해주세요.


<br><br>
---

## 2. GIT 설치 완료 후 Clone

- ### GITHUB에 올려져 있는 GIT 저장소를 로컬 GIT 저장소로 가져오는 방법입니다.

- ### <span style="color: red;">Clone은 최초 1회만 해주시면 됩니다.</span>
    - ### Clone이 이미 되어있는 상태라면 Push부터 진행 해주시면 됩니다.

<br>

- ### 1. 현재 레포지토리의 Code버튼을 클릭한 후 URL을 복사해줍니다.

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/438ccd1b-c4b9-422c-a177-828fbe29bad8)

- ### 2. 내려받을 폴더에서 터미널 창을 열어줍니다.

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/0d230ec2-8c38-4b6a-bfbf-4d87d639fb9a)

- ### 3. 콘솔 창에 `git clone 복사한URL` 을 입력해줍니다. 마지막 줄에 done이 떴다면 정상적으로 완료된것입니다.

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/e458068a-b606-4114-8456-e2e878b26fe0)

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/8919c0ec-2434-4310-ad11-44a871db0679)

- ### 생성된 폴더에서 파일 생성 등 작업 해주시면됩니다.

<br><br>
---

## 3. PULL

- ### <span style="color: red;">GIT에 COMMIT, PUSH 하기 전 꼭 해주셔야 할 작업입니다.</span>

- ### 내 PC에서 마지막으로 pull, clone한 이후 다른 사람들이 업로드하여 브랜치가 수정되었을 수 있습니다.

- ### 수정되기 전 레포지토리로 push를 시도할 시 오류가 발생하므로 pull로 최신 상태를 유지하여야 합니다.

    <br>

- ### ```git pull```

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/0ab47260-6ecb-441e-a050-6e1d6b712d92)

---
<br><br>

## 4. COMMIT, PUSH

- ### COMMIT: 로컬 GIT에 변경한 사항을 반영하는 작업입니다.

    - ### `git commit -m "메시지"`
        - #### 커밋 기록에 남길 메시지를 메시지 자리에 넣으시면 됩니다.
            ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/bd29028f-86d0-4fe3-80d6-7a1546d26ae7)


- ### PUSH: 로컬 GIT을 GITHUB 원격 저장소로 업로드하는 작업입니다.
    - ### `git push`

---
<br><br>


## `요약` 클론이 되어있고, 업로드할 파일도 준비되었을 때 업로드하기

- ### 1. Clone 되어있는 저장소 폴더에서 터미널 창을 열기

    - ### README.md가 있는 디렉터리라고 생각하시면 됩니다.

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/b97250ee-0557-441b-bb35-64e6c34abcb9)

- ### 1. `git pull`

- ### 2. `git add .`

- ### 3. `git commit -m "메시지"`

- ### 4. `git push`