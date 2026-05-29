from flask import Flask, render_template, request, redirect, url_for, flash
from main import InventoryManager

app = Flask(__name__)
app.secret_key = 'inventory-secret-key'
manager = InventoryManager()

@app.route('/')
def index():
    return render_template('index.html', inventory=manager.inventory)

@app.route('/register', methods=['POST'])
def register():
    item_name = request.form.get('item_name', '')
    success, message = manager.register_item_web(item_name)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

@app.route('/update_stock', methods=['POST'])
def update_stock():
    item_name = request.form.get('item_name', '')
    try:
        qty = int(request.form.get('qty', -1))
    except ValueError:
        qty = -1
    success, message = manager.update_stock_web(item_name, qty)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

@app.route('/rename', methods=['POST'])
def rename():
    old_name = request.form.get('old_name', '')
    new_name = request.form.get('new_name', '')
    success, message = manager.rename_item_web(old_name, new_name)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    item_name = request.form.get('item_name', '')
    success, message = manager.delete_item_web(item_name)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

@app.route('/stock_in', methods=['POST'])
def stock_in():
    item = request.form.get('item', '')
    try:
        qty = int(request.form.get('qty', 0))
    except ValueError:
        qty = 0
    success, message = manager.stock_in_web(item, qty)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

@app.route('/stock_out', methods=['POST'])
def stock_out():
    item = request.form.get('item', '')
    try:
        qty = int(request.form.get('qty', 0))
    except ValueError:
        qty = 0
    success, message = manager.stock_out_web(item, qty)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)