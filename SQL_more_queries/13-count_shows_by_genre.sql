-- number of shows by genre --
SELECT NAME AS genre, count(id) As number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON genre_id = id
GROUP BY genre ORDER BY number_of_shows DESC;
