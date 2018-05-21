from ..utils.gadget import db

class Product(db.Model):
    __tablename__ = 'tb_product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    expiration_days = db.Column(db.Integer)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Product(id=[%s])>" % self.id

    def __hash__(self):
        return hash(self.id)

class Item(db.Model):
    __tablename__ = 'tb_item'
    id = db.Column(db.Integer, primary_key=True)
    date_produce = db.Column(db.Date)
    product_id = db.Column(db.Integer, db.ForeignKey('tb_product.id'))
    product = db.relationship("Product", back_populates="items")

    def __str__(self):
        return "<Item(id=%d, product=%s)>" % (self.id, self.product.name)

    def __repr__(self):
        return "<Item(id=%d)>" % self.id

    def __hash__(self):
        return hash(self.id)

Product.items = db.relationship("Item", order_by=Item.id, back_populates="product")
