-- genre id for all shows --
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = show_id ORDER BY title, genre_id;
