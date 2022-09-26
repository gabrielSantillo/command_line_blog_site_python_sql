insert into client (username, joined_on, password)
values ('gabriel', '2022-09-25', '123'), ('natalia', '2021-07-09', '123'), ('chicaho', '2020-01-15', '123');

insert into post (client_id, content, title)
values (1, 'Making my first post.', 'First'), (1, 'Making my second post.', 'Second'), (2, 'Making the third post.', 'Third'), 
(2, 'Making the fourth.', 'Fourth'), (3, 'Au au au au', 'Au'), (3, 'Rughw rughw', 'Rughw');

call select_user_id('gabriel', '123');

call add_post_user(1, 'testing content', 'testing title');

call get_all_posts();

call get_post_by_id(2);

call get_all_usernames();

call get_post_by_username('gabriel');