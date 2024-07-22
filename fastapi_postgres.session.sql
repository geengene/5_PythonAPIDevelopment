-- SELECT id as product_id, name, price , inventory FROM products ORDER BY price DESC;
-- SELECT * FROM products WHERE name LIKE 'TV%';
-- SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 5;
-- INSERT INTO products (name, price, inventory) VALUES ('tortilla', 4, 1000), ('car', 20000, 5), ('toast', 1, 40) returning *; 
-- DELETE FROM products WHERE id = 1 RETURNING *;
-- UPDATE products SET is_sale = true, inventory = 100 WHERE inventory = 0;
SELECT * FROM posts;
