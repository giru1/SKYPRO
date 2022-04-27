CREATE TABLE animal_types(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(30));

create table animal_type_animal_id(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     id_type INTEGER ,
     id_animal INTEGER,
     FOREIGN KEY (id_type) REFERENCES animal_types(id),
     FOREIGN KEY (id_animal) REFERENCES animal_fin(id)
);

CREATE TABLE animal_color(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color varchar(30));

create table animal_color_animal_id(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     id_color INTEGER ,
     id_animal INTEGER,
     FOREIGN KEY (id_color) REFERENCES animal_color(id),
     FOREIGN KEY (id_animal) REFERENCES animal_fin(id)
);

CREATE TABLE animal_breed(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        breed varchar(30));

create table animal_breed_animal_id(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     id_breed INTEGER ,
     id_animal INTEGER,
     FOREIGN KEY (id_breed) REFERENCES animal_breed(id),
     FOREIGN KEY (id_animal) REFERENCES animal_fin(id)
);

CREATE TABLE animal_outcome(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        outcome varchar(30),
        oc_month INT,
        oc_year INT,
        oc_subtype VARCHAR(60)
        );


create table animal_outcome_animal_id(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     id_outcome INTEGER ,
     id_animal INTEGER,
     FOREIGN KEY (id_outcome) REFERENCES animal_outcome(id),
     FOREIGN KEY (id_animal) REFERENCES animal_fin(id)
);

CREATE TABLE animal_fin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age_upon_outcome varchar(30),
        animal_id varchar(30),
        name VARCHAR(50),
        date_of_birth DATE);


INSERT INTO animal_color (color) SELECT DISTINCT (trim(color1)) FROM animals;
INSERT INTO animal_color (color) SELECT DISTINCT (trim(color2)) as d FROM animals where d not in
                                                    (select animal_color.color from animal_color);

drop table animal_color;

insert into animal_color_animal_id (id_color, id_animal)
        select animal_color.id, animals."index" from animals
        join animal_color on trim(animals.color1) = animal_color.color;