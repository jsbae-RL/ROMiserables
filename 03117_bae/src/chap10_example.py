from fastapi import FastAPI  # FastAPI 모듈을 가져옴
from pydantic import BaseModel  # 데이터 검증을 위해 Pydantic의 BaseModel을 가져옴

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# Pydantic을 사용하여 요청 바디의 데이터 모델을 정의
class Item(BaseModel):
    name: str  # 상품 이름 (문자열)
    price: float  # 상품 가격 (실수형)
    is_offer: bool = None  # 할인 여부 (기본값 None)

# 루트 엔드포인트('/')를 처리하는 함수 정의
# 엔드 포인트는 응용 프로그램의 기본 종점을 의미
# 사용자가 API의 기본 URL에 액세스하면이 엔드 포인트가 실행
# `@app.get("/") : http get이 `/`에 대한 요청이 이루어지면(다시 말해 호출되면)
# `read_root()`에 대한 기능을 트리거해야한다고 Fastapi에게 알려줍니다.(출력합니다. 출력을 위한 데이터의 정의)

# REST API의 구성
# "/" = 자원
# app.get = HTTP Method
# return {'hello': 'world'} : 행위의 내용
@app.get("/")
def read_root():
    return {'hello': 'world'}  # JSON 형태의 응답 반환

# 특정 ID의 아이템을 조회하는 엔드포인트
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    - `item_id` (int): 경로 매개변수로 받아오는 아이템 ID
    - `q` (str, 선택적): 쿼리 매개변수 (기본값 None)
    - 요청 예시: GET /items/5?q=test
    - 응답 예시: {"item_id": 5, "q": "test"}
    """
    return {'item_id': item_id, 'q': q}  # JSON 형태의 응답 반환

# 특정 ID의 아이템 정보를 업데이트하는 엔드포인트
# 사용자는 PUT 요청을 통해 새로운 아이템 데이터를 보낼 수 있으며, 해당 데이터를 받아서 처리하는 방식
# 즉, 클라이언트가 호출할때, 정의된 데이터 양식에 맞게 값을 주면서 입력
@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    """
    - `item_id` (int): 경로 매개변수로 받아오는 아이템 ID
    - `item` (Item): 요청 본문(body)에서 받아오는 아이템 정보
    - 요청 예시: PUT /items/5
      body: {"name": "Laptop", "price": 1500.99, "is_offer": true}
    - 응답 예시: {"item_name": 1500.99, "item_id": 5}
    """
    return {'item_name': item.price, 'item_id': item_id}  # 아이템 가격과 ID를 JSON 형태로 반환
