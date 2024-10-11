-- 코드를 입력하세요
SELECT PRODUCT_CODE, PRICE * SUM(SALES_AMOUNT) AS SALES
FROM PRODUCT P JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY PRICE DESC, PRODUCT_CODE ASC