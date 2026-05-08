EXPLAIN SELECT products.*, categories.name
FROM products
JOIN products_categories ON products_categories.product_id = products.id
JOIN categories ON products_categories.category_id = categories.id
WHERE products_categories.category_id = 2