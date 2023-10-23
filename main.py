from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# エントリIDと関連データのダミーデータ
data = {
    "A0000000001": [
        {
        "product_code": "A0000000001",
        "product_name": "だいこん",
        "sales_date": "2023/10/23",
        "quantity": 10,
        "unit_price": 50,
        "amount": 500
        },
        {
        "product_code": "A0000000001",
        "product_name": "だいこん",
        "sales_date": "2023/10/21",
        "quantity": 100,
        "unit_price": 10,
        "amount": 1000
        }
    ],
# 他のエントリIDとデータをここに追加
}

@app.get("/base_api/01/{product_code_list_str}")
def get_data(product_code_list_str: str):
    product_code_list = product_code_list_str.split(",")
    for product_code in product_code_list:
        if product_code in data:
            return data[product_code]
    else:
        return {"error": "エントリIDが見つかりません"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
