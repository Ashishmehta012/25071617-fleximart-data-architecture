
    -- Total Revenue by Year
    SELECT d.year, SUM(f.total_amount) 
    FROM fact_sales f 
    JOIN dim_date d ON f.date_key = d.date_key 
    GROUP BY d.year;
    