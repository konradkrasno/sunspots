from datetime import date

from notes.models import Store, Shop, Contractor, Note, NotePosition
from products.models import Manufacturer, Category, Product
from stock.models import Stock
from workers.models import Worker

test_data = {
    Manufacturer: [{"name": "Lipton"}, {"name": "Herbapol"}, {"name": "Tetley"}],
    Category: [{"name": "Grocery"}],
    Product: [
        {
            "name": "Black Tea Lipton",
            "group": "B",
            "code": "XYZ123",
            "batch_number": "03.2021",
            "unit": "pc.",
            "purchase_price": 7.00,
            "sales_price_net": 10.10,
            "tax_rate": 23,
            "best_before_date": date(year=2022, month=3, day=1),
            "description": "Delicious black tea",
            "manufacturer_id": 1,
            "category_id": 1,
        },
        {
            "name": "Red Tea Lipton",
            "group": "B",
            "code": "XYZ234",
            "batch_number": "03.2021",
            "unit": "pc.",
            "purchase_price": 11.00,
            "sales_price_net": 15.10,
            "tax_rate": 23,
            "best_before_date": date(year=2022, month=3, day=1),
            "description": "Delicious red tea",
            "manufacturer_id": 1,
            "category_id": 1,
        },
        {
            "name": "Fruit Tea Herbapol",
            "group": "B",
            "code": "XYZ345",
            "batch_number": "02.2021",
            "unit": "pc.",
            "purchase_price": 2.10,
            "sales_price_net": 5.00,
            "tax_rate": 23,
            "best_before_date": date(year=2022, month=2, day=1),
            "description": "Delicious fruit tea",
            "manufacturer_id": 2,
            "category_id": 1,
        },
        {
            "name": "Earl Grey Tea Tetley",
            "group": "B",
            "code": "XYZ456",
            "batch_number": "01.2021",
            "unit": "pc.",
            "purchase_price": 4.10,
            "sales_price_net": 6.00,
            "tax_rate": 23,
            "best_before_date": date(year=2022, month=1, day=1),
            "description": "Delicious earl grey tea",
            "manufacturer_id": 3,
            "category_id": 1,
        },
    ],
    Worker: [
        {
            "first_name": "Tom",
            "last_name": "Hagen",
            "position": "seller",
            "active": True,
        },
        {
            "first_name": "Luca",
            "last_name": "Brasi",
            "position": "storeman",
            "active": True,
        },
    ],
    Stock: [{}] * 7,
    Store: [
        {
            "name": "Store-Warsaw-01",
            "address": "Sasanki 10",
            "postal_code": "06-852",
            "city": "Warsaw",
            "stock_id": 1,
        },
        {
            "name": "Store-Warsaw-02",
            "address": "Niezapominajki 15",
            "postal_code": "03-798",
            "city": "Warsaw",
            "stock_id": 2,
        },
        {
            "name": "Store-Poznan-01",
            "address": "Konwaliowa 15",
            "postal_code": "04-132",
            "city": "Poznan",
            "stock_id": 3,
        },
    ],
    Shop: [
        {
            "name": "Shop-Warsaw-01",
            "address": "Sosnowa 15",
            "postal_code": "04-101",
            "city": "Warsaw",
            "stock_id": 4,
        },
        {
            "name": "Shop-Warsaw-02",
            "address": "Akacjowa 20",
            "postal_code": "04-115",
            "city": "Warsaw",
            "stock_id": 5,
        },
        {
            "name": "Shop-Poznan-01",
            "address": "Grabowa 8",
            "postal_code": "04-228",
            "city": "Poznan",
            "stock_id": 6,
        },
        {
            "name": "Shop-Poznan-02",
            "address": "Lipowa 8",
            "postal_code": "05-466",
            "city": "Poznan",
            "stock_id": 7,
        },
    ],
    Contractor: [
        {
            "type": "client",
            "first_name": "Jan",
            "last_name": "Kowalski",
            "company_name": "",
            "email": "kowalski@gmail.com",
            "address": "Mysia 8",
            "postal_code": "03-654",
            "city": "Warsaw",
        },
        {
            "type": "supplier",
            "first_name": "Adam",
            "last_name": "Nowak",
            "company_name": "nowak-invest",
            "email": "nowak@invest.com",
            "address": "Lisia 20",
            "postal_code": "06-312",
            "city": "Cracow",
        },
    ],
    Note: [
        {
            "type": "supply",
            "handover_type": "external",
            "number": "EXT-SUP-1",
            "from_store_id": None,
            "from_shop_id": None,
            "from_contractor_id": 2,
            "to_store_id": 1,
            "to_shop_id": None,
            "to_contractor_id": None,
            "worker_id": 2,
        },
        {
            "type": "dispatch",
            "handover_type": "internal",
            "number": "INT-DIS-1",
            "from_store_id": 1,
            "from_shop_id": None,
            "from_contractor_id": None,
            "to_store_id": None,
            "to_shop_id": 1,
            "to_contractor_id": None,
            "worker_id": 2,
        },
        {
            "type": "dispatch",
            "handover_type": "external",
            "number": "EXT-DIS-1",
            "from_store_id": None,
            "from_shop_id": 1,
            "from_contractor_id": None,
            "to_store_id": None,
            "to_shop_id": None,
            "to_contractor_id": 2,
            "worker_id": 1,
        },
    ],
    NotePosition: [
        {
            "note_id": 1,
            "product_id": 1,
            "quantity": 1000,
            "price_net": 7.00,
            "tax_rate": 23,
            "discount_value": 0,
        },
        {
            "note_id": 1,
            "product_id": 2,
            "quantity": 1000,
            "price_net": 11.00,
            "tax_rate": 23,
            "discount_value": 0,
        },
        {
            "note_id": 1,
            "product_id": 3,
            "quantity": 1000,
            "price_net": 2.10,
            "tax_rate": 23,
            "discount_value": 0,
        },
        {
            "note_id": 1,
            "product_id": 4,
            "quantity": 1000,
            "price_net": 4.10,
            "tax_rate": 23,
            "discount_value": 0,
        },
        {
            "note_id": 2,
            "product_id": 1,
            "quantity": 500,
        },
        {
            "note_id": 2,
            "product_id": 2,
            "quantity": 500,
        },
        {
            "note_id": 2,
            "product_id": 3,
            "quantity": 500,
        },
        {
            "note_id": 2,
            "product_id": 4,
            "quantity": 500,
        },
        {
            "note_id": 3,
            "product_id": 1,
            "quantity": 2,
            "price_net": 10.10,
            "tax_rate": 23,
            "discount_value": 0,
        },
        {
            "note_id": 3,
            "product_id": 2,
            "quantity": 5,
            "price_net": 15.10,
            "tax_rate": 23,
            "discount_value": 0,
        },
    ],
}
