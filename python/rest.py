from flask  import Flask, request, jsonify
from datetime import datetime
from db import connect_db

app = Flask(__name__)

@app.route('/productSave', methods=['POST'])
def test_endpoint():
    data = request.get_json()
    title = str(data.get('title'))
    detail = str(data.get('detail'))
    price = int(data.get('price'))

    # ' or 1 = 1; delete from product --
    if not title or not detail or price is None or price < 0:
        return jsonify({'error': 'Missing required fields'}), 400

    con = connect_db() # db açılıyor
    cursor = con.cursor() # query için ortam oluşturuluyor
    sql = "INSERT INTO product (title, detail, price) VALUES (?, ?, ?)"
    productCursor = cursor.execute(sql, (title, detail, price))
    con.commit() # değişiklikler db ye işleniyor
    con.close() # db kapanıyor
    return jsonify({'id': productCursor.lastrowid}), 200

@app.route('/productList', methods=['GET'])
def productList():
    con = connect_db() # db açılıyor
    sql = 'select * from product'
    cursor = con.cursor()
    productCursor = cursor.execute(sql)
    products = []
    for row in productCursor:
        products.append({
            'id': row['id'],
            'title': row['title'],
            'detail': row['detail'],
            'price': row['price']
        })
    con.close() # db kapanıyor
    return jsonify(products), 200


@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    con = connect_db() # db açılıyor
    sql = 'select * from product where id = ?'
    cursor = con.cursor()
    productCursor = cursor.execute(sql, (id,))
    row = productCursor.fetchone() # tek kayıt alınıyor
    con.close() # db kapanıyor
    if row:
        product = {
            'id': row['id'],
            'title': row['title'],
            'detail': row['detail'],
            'price': row['price']
        }
        return jsonify(product), 200
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/productUpdate', methods=['POST'])
def product_update():
    data = request.get_json()
    id = int(data.get('id'))
    title = str(data.get('title'))
    detail = str(data.get('detail'))
    price = int(data.get('price'))

    con = connect_db() 
    cursor = con.cursor()
    sql = 'update product set title = ?, detail = ?, price = ? where id = ?'
    updateCursor = cursor.execute(sql, (title, detail, price, id))
    con.commit()
    con.close()
    if updateCursor.rowcount > 0:
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=False, port=5000)