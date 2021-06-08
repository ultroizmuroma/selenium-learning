# homebrew


# selenium-learning

# pg-learning
Как установить postgres:
brew install postgres
brew services start postgresql
createdb
createuser -s postgres
Можно соединяться с localhost
```
CREATE TABLE public."user" (
id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
username varchar(255) NULL,
phone1 varchar(255) NULL,
phone2 varchar(255) NULL,
phone3 varchar(255) NULL
);

insert into "user" (phone1, description1, phone2, description2, phone3, description3) 
values
('89107702801', 'рабочий1', null, null, '89107702802', 'домашний1'),
('89107702803', 'рабочий2', null, null, '89107702804', 'домашний2'),
('89107702805', 'рабочий3', null, null, '89107702806', 'домашний3'),
(null, null, '88002000600', 'спам', null, null)
```