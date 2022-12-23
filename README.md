# doc2illustration

## 프로젝트 설명
**[배경]**<br/>
Stable Diffusion, Imagen, Dalle 2와 같이 거대 T2I 모델이 공개 된 후, 해당 모델을 이용하여 할 수 있는 다양한 Downstream Task가 등장함.
Content가 동일한 소수의 이미지(5~10장)를 참고한 후, 해당 이미지들의 특성을 반영하여 T2I를 수행하는 Personalized Model이 등장
해당 프로젝트를 통해 Personalized T2I 모델이 활용될 수 있는 분야를 탐구


**[진행]**<br/>
아동용 저작물에는 유아의 이해를 돕기 위해 텍스트와 그에 맞는 적절한 일러스트레이션이 삽입됨
일러스트레이션 제작에는 건 당 약 6~20만원의 비용이 들며, 동화책과 같이 중장기 프로젝트에는 더 큰 비용이 요구될 수 있음 
Bart-Summariziation | Dreambooth Pipeline을 통해  텍스트의 Context를 반영하며, Content가 일정한 일러스트레이션을 생성
본 프로젝트에서는 ‘동화 Text’ -> ‘아동용 일러스트레이션’ Generation Pipeline을 제시


## Pipeline
<img width="846" alt="Screen Shot 2022-12-23 at 5 58 27 PM" src="https://user-images.githubusercontent.com/101631683/209305961-8f1e04c6-743d-436c-81de-c40fdb55cb78.png">

## Results
<img width="1006" alt="Screen Shot 2022-12-23 at 6 04 36 PM" src="https://user-images.githubusercontent.com/101631683/209306411-ea1ce1c4-9aea-4083-b258-56fdd52cb6a4.png">

