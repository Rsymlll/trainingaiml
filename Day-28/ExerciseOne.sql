Create DATABASE ExerciseOne;
USE  ExerciseOne;
create table StudentMarks (
    StudentID int,
    StudentName nvarchar(50),
    Math int,
    Science int,
    English int,
    History int
)

--insert few records
insert into StudentMarks values 
    (1,'Sam',90,85,90,88)

insert into StudentMarks values 
    (2,'Azim',80,95,70,80),
    (3,'Syammil',94,75,80,83),
    (4,'Ali',82,89,90,98),
    (5,'Badri',92,83,80,78),
    (6,'Ahlam',70,95,91,78)

select*from StudentMarks