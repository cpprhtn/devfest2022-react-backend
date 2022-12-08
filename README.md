# setup
```
docker-compose up -d --build
```
# fastapi REST api 명세서
http://localhost:8000/docs

# Backend(API) Page

### 기술스택

- docker
    - fastapi (python)
    - mysql
    

## 프론트에서 필요한 API(mock-data)

- [https://stackflow.so/](https://stackflow.so/) 참고

```sql
-- 물품리스트 (11개)
CREATE TABLE productinfo (
    id INT NOT NULL,
    userID INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    img VARCHAR(200) NOT NULL,           
    price FLOAT NOT NULL,          
    dates DATE, /*'YYYY-MM-DD'*/
    category VARCHAR(30) NOT NULL,
    info VARCHAR(500) NOT NULL,
    chats INT NOT NULL,
    favorites INT NOT NULL,
    views INT NOT NULL,
    PRIMARY KEY (id)
);

-- 유저정보 (4명)
CREATE TABLE userinfo (
    userID INT NOT NULL,
    profileImg VARCHAR(200) NOT NULL,
    userName VARCHAR(30) NOT NULL,
    location VARCHAR(30) NOT NULL,
    rating FLOAT NOT NULL,
    PRIMARY KEY (userID)
);
```

# /product [GET]

**Request URL**

**`http://localhost:8000/product`**

**Response body (product table + user table의 location join)**

```
[
  {
    "id": 0,
    "name": "스팸 선물세트",
    "price": 20000,
    "category": "Food",
    "chats": 1,
    "views": 212,
    "userID": 0,
    "img": "https://t1.daumcdn.net/cfile/tistory/99F5F73A5B92899F06",
    "dates": "2022-12-01",
    "info": "명절때 선물하기 좋은 스팸 선물 세트입니다. 저희가족이 스팸을 안먹어서 싸게 내놓습니다.",
    "favorites": 2,
    "location": "강남구"
  },
  {
    "id": 1,
    "name": "가정용 크리스마스 트리",
    "price": 15000,
    "category": "Interior",
    "chats": 1,
    "views": 212,
    "userID": 0,
    "img": "https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/product/3981205773/B.jpg?593000000",
    "dates": "2022-12-04",
    "info": "쿠*에서 3만원 주고 구매했습니다. 구매하실분 연락주세요.",
    "favorites": 2,
    "location": "강남구"
  },
	...
	}
]
```

# /product/{product_id} [GET]

**Request URL**

**`http://localhost:8000/product/{}`**

**Response body (product table + user table의 location join)**

```jsx
/*
**http://localhost:8000/product/3
*/

{
  "id": 3,
  "name": "키크론 K6 키보드 팝니다",
  "price": 92500,
  "category": "Digital device",
  "chats": 4,
  "views": 506,
  "userID": 1,
  "img": "https://dnvefa72aowie.cloudfront.net/origin/article/202211/D74125630419D841D4966C7CCA42A367F0D44604C407DC94254BA534E0E3C54B.jpg?q=95&s=1440x1440&t=inside",
  "dates": "2022-12-05",
  "info": "키크론 K6와 팜레스트를 판매합니다. 다른 키보드를 구매하게 되어서 내놓습니다. 실사용은 1주일도 안되어 매우 깨끗합니다. 들어있는 구성품은 다 들어있습니다.",
  "favorites": 11,
  "location": "해운대"
}
```

# users/{user_id} [GET]

**Request URL**

**`http://localhost:8000/users/{}`**

**Response body (product table + user table의 location join)**

```jsx
/*
**http://localhost:8000/product/3
*/

{
  "profileImg": "https://i.pinimg.com/originals/a7/ee/b8/a7eeb85a1d27390ebdf770f8cf31e434.jpg",
  "userName": "a2z",
  "rating": 36.9,
  "userID": 3,
  "location": "강서구",
  "other": [
    {
      "name": "스팸 선물세트",
      "img": "https://t1.daumcdn.net/cfile/tistory/99F5F73A5B92899F06",
      "price": 20000
    },
    {
      "name": "가정용 크리스마스 트리",
      "img": "https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/product/3981205773/B.jpg?593000000",
      "price": 15000
    },
    {
      "name": "아기 유모차",
      "img": "https://img.danawa.com/prod_img/500000/004/241/img/15241004_1.jpg?shrink=330:330&_v=20210914090811",
      "price": 76000
    },
    {
      "name": "키크론 K6 키보드 팝니다",
      "img": "https://dnvefa72aowie.cloudfront.net/origin/article/202211/D74125630419D841D4966C7CCA42A367F0D44604C407DC94254BA534E0E3C54B.jpg?q=95&s=1440x1440&t=inside",
      "price": 92500
    },
    {
      "name": "해피해킹 hybrid Type-S 새상품",
      "img": "https://blog.kakaocdn.net/dn/cigrn9/btqP6oiVfQH/O47ZMxCL0Qbx5hsRzaqh80/img.jpg",
      "price": 320000
    },
    {
      "name": "아이폰 11 퍼플",
      "img": "https://blog.kakaocdn.net/dn/bTlpkQ/btqBHxngxhs/7St98RyVybaCBNPJnhoIv0/img.png",
      "price": 105000
    },
    {
      "name": "필립스 면도기",
      "img": "https://img.hankyung.com/photo/201805/01.16830265.1.jpg",
      "price": 12000
    },
    {
      "name": "다이슨 v8 청소기",
      "img": "https://t1.daumcdn.net/cfile/tistory/2350DA3657FE8D2A1B",
      "price": 83000
    }
  ]
}
```


### 간단한 명세서
- 물품 리스트(많으면 많을수록 좋음 - 최소 10개)
    - id
    - 사진
    - 제목
    - 가격
    - 작성자 이름
    - 며칠 전에 작성했는지
- 리스트의 상세 API(id로 호출)
    - 작성자 프로필(프로필 사진, 이름, 사는 곳, rating-0~100)
    - 제목
    - 카테고리
    - 설명
    - chats ∙ favorites ∙ views 갯수
    - Other Item 리스트(사진, 제목, 가격) - 8개
