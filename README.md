# 2021 Hackathon : 교내 건물들 간 최단거리 찾기

### 💡 아이디어 배경
- 기존의 지도앱에서 교내에서의 길이 잘 검색되지 않아 최단경로를 검색했을 떄 실제로 차이가 남. <br>
  - 현재 네이버나 다음 등 사람들이 많이 이용하는 포털 사이트 상의 지도는 계단을 고려하지 않고 주로 큰 길을 다룸. <br/>
  -> 한계점을 보완하자.
- COVID 19로 인해 비대면으로 수업하는 학생들은 학교 안의 길을 잘 모름.
- 신입생과 교내 길을 잘 모르는 사람들을 위한 교내 건물들 간 최단거리 제공 서비스를 제공하자.

  - 학교에서 이동할 때 가장 빠른 경로를 알아서 찾아주는 건물 간 이동할 때 최적으로 이동할 수 있도록 도와줌.
  - 프린트기, 편의점, 흡연부스, 카페, 서점, 식당, 은행 등 학교의 편의시설의 정보도 제공.

<br/>

### 🔎 프로젝트 설명
직접 학교 구석구석을 다니면서 길을 확인하였고, 현재 코로나 19로 인해 운영되지 않는 곳은 제외하였다. 건물의 입구 노드와, 직선으로 가지 못해 꺾어야 하거나 더 가깝게 가기 위한 곳에 각각 노드를 두고 opencv를 이용하여 노드를 자동으로 인식하게 하였습니다. 이를 토대로 노드들을 잇는 선 중에 건물의 외각선을 지나지 않는 경로만 추출하여 이를 csv 파일로 저장하고 이를 바탕으로 q-routing을 통해 특정 구간의 최적경로를 파악하는 인공지능 알고리즘을 구현하였다.
<br/>

❤️ <font color='red'>**빨간색 노드**</font> : 건물 입구 <br/>
💛 <font color='orange'>**노란색 노드**</font> : 코너 <br/>

<p align='center'>
<img src='https://user-images.githubusercontent.com/86948867/178370953-a15b3c7b-7646-4a6f-b146-2e8170a46312.png' />
<img src='https://user-images.githubusercontent.com/86948867/178370967-7960a11d-e85e-4aa9-866c-990bc2a5cc9a.png' />
<img src='https://user-images.githubusercontent.com/86948867/178370978-6275ee83-ce4e-4ea1-b226-2eb35c6eb505.png' />
</p>

<p align='center'>
<img src='https://raw.githubusercontent.com/seul1230/seul1230.github.io/main/assets/img/2021_hackathon_img/final_video.gif' width="50%" />
</p>

<br/><br/>


### 🏆 프로젝트 결과
은상
