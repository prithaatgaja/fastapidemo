
from typing import Optional, List
from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse


router = APIRouter(
  prefix='/product',
  tags=['product']
)

products = ['Watch', 'camera', 'phone']

@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products

@router.get('/all')
def get_all_products():
   # return products
   data = " ".join(products)
   return Response(
         content=data,
         media_type='text/plain'
   )

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)
):
 return products



@router.get('/{id}', responses={
    200:{
        "content":
        {
            "text/html": 
                {
                "example" : "<div>product</div>"
                }
        },
        "description": "returns HTML as a Object"
    },
    400:{

        "content":
        {
            "text/plain": 
                {
                "example" : "<div>product not available</div>"
                }
        },
        "description": "returns plain as a Object"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "product not available"
        return PlainTextResponse(
            content=out,
            media_type='text/plain'
        )
    else:  
     product = products[id]
     out = f"""
     <head>
     <style>
      .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green:
        background-color: lightblue;
        text-align: center;
     }}
     </style>
     </head>
     <div class="product">{product}</div> 
     """
    return HTMLResponse(content=out, media_type="text/html")