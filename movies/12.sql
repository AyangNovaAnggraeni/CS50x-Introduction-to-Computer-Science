
SELECT title
   FROM movies
   JOIN stars AS s1 ON movies.id = s1.movie_id
   JOIN stars AS s2 ON movies.id = s2.movie_id
   JOIN people AS p1 ON s1.person_id = p1.id
   JOIN people AS p2 ON s2.person_id = p2.id
   WHERE p1.name = 'Bradley Cooper' AND p2.name = 'Jennifer Lawrence';
