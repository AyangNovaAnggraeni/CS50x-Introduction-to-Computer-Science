SELECT title, rating FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE movies.year = '2010' ORDER BY rating DESC, title ASC;
