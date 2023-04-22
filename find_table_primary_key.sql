-- 使用SQL查询postgresql数据库中每个表的主键名字
SELECT tc.table_name, kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
WHERE tc.constraint_type = 'PRIMARY KEY'
AND tc.table_schema = 'ju_ems'
ORDER BY tc.table_name;


-- 使用SQL查询mysql数据库中每个表的主键名字
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = '803_dev'
AND CONSTRAINT_NAME = 'PRIMARY'
ORDER BY TABLE_NAME;


-- 使用SQL查询oracle数据库中实例名为owr的每个表的主键名字
SELECT cols.table_name, cols.column_name
FROM all_constraints cons, all_cons_columns cols
WHERE cons.constraint_type = 'P'
AND cons.constraint_name = cols.constraint_name
AND cons.owner = cols.owner
AND cols.owner = 'owr'
ORDER BY cols.table_name;
