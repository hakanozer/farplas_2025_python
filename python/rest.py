from flask import Flask, request, jsonify
from flasgger import Swagger
from db import connect_db

app = Flask(__name__)

swagger = Swagger(app, config={
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
})


@app.route('/productSave', methods=['POST'])
def productSave():
    """
    Yeni ürün ekler
    ---
    tags:
      - Product
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - detail
            - price
          properties:
            title:
              type: string
              example: "iPhone 15"
            detail:
              type: string
              example: "256GB, Siyah"
            price:
              type: integer
              example: 45000
    responses:
      200:
        description: Ürün başarıyla eklendi
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 12
      400:
        description: Hatalı veya eksik alan
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Missing required fields"
    """
    data = request.get_json()

    title = data.get('title')
    detail = data.get('detail')
    price = data.get('price')

    if not title or not detail or price is None or price < 0:
        return jsonify({'error': 'Missing required fields'}), 400

    con = connect_db()
    cursor = con.cursor()
    sql = "INSERT INTO product (title, detail, price) VALUES (?, ?, ?)"
    cursor.execute(sql, (title, detail, price))
    con.commit()
    product_id = cursor.lastrowid
    con.close()

    return jsonify({'id': product_id}), 200


@app.route('/productList', methods=['GET'])
def productList():
    """
    Tüm ürünleri listeler
    ---
    tags:
      - Product
    responses:
      200:
        description: Ürün listesi
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              title:
                type: string
                example: "MacBook Pro"
              detail:
                type: string
                example: "M3 Pro, 16GB RAM"
              price:
                type: integer
                example: 85000
    """
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM product")

    products = []
    for row in cursor:
        products.append({
            "id": row["id"],
            "title": row["title"],
            "detail": row["detail"],
            "price": row["price"]
        })

    con.close()
    return jsonify(products), 200


@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    """
    ID ile ürün getirir
    ---
    tags:
      - Product
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        example: 3
    responses:
      200:
        description: Ürün bulundu
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            detail:
              type: string
            price:
              type: integer
      404:
        description: Ürün bulunamadı
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Product not found"
    """
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM product WHERE id = ?", (id,))
    row = cursor.fetchone()
    con.close()

    if row:
        return jsonify({
            "id": row["id"],
            "title": row["title"],
            "detail": row["detail"],
            "price": row["price"]
        }), 200

    return jsonify({"error": "Product not found"}), 404


@app.route('/productUpdate', methods=['POST'])
def product_update():
    """
    Ürün günceller
    ---
    tags:
      - Product
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - id
            - title
            - detail
            - price
          properties:
            id:
              type: integer
              example: 5
            title:
              type: string
              example: "Samsung S24"
            detail:
              type: string
              example: "128GB, Gri"
            price:
              type: integer
              example: 32000
    responses:
      200:
        description: Güncelleme başarılı
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Product updated successfully"
      404:
        description: Ürün bulunamadı
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Product not found"
    """
    data = request.get_json()

    con = connect_db()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE product SET title=?, detail=?, price=? WHERE id=?",
        (data["title"], data["detail"], data["price"], data["id"])
    )
    con.commit()
    updated = cursor.rowcount
    con.close()

    if updated:
        return jsonify({"message": "Product updated successfully"}), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run(port=5000)
