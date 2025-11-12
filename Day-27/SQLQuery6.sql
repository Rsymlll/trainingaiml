use OurDb
--Constraint, not null, primary key: not null and unique ,
create table Emp
(Id int primary key, 
Fname nvarchar(50) not null,
Lname nvarchar(50)
)
select*from Emp
insert into Emp values (1, 'Sam', 'Discosta')
insert into Emp (Id,Fname) values (2, 'Rameez')
select*from Emp
insert into Emp (Id,Lname) values (6, 'Khan')
--Cannot insert the value NULL into column 'Fname', table 'OurDb.dbo.Emp'; column does not allow nulls. 
insert into Emp (Id,Fname) values (2, 'Deep')
--Violation of PRIMARY KEY constraint 'PK__Emp__3214EC07AD9C33E7'. 
--Cannot insert duplicate key in object 'dbo.Emp'. The duplicate key value is (2)

delete from Emp
select*from Emp

drop table Emp
select*from Emp
----------------------------------------------------
--default
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default('Kuala Lumpur')
)
insert into Emp values (1,'Sam','John','Brisbane')
insert into Emp values (2,'Rina','Kumari','Delhi')
select*from Emp
insert into Emp (Id, Fname, Lname) values(3,'Alina','Khan')
select*from Emp 
--Check
drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default('Kuala Lumpur'),
Salary float not null check(Salary>=10000 and Salary<=50000)
)
insert into Emp (Id, Fname, Lname,Salary) values(3,'Alina','Khan',12000)
insert into Emp values (2,'Rina','Kumari','Delhi',19000)

drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
insert into Emp values (1,'Maan','9876543210')
select*from Emp
insert into Emp values (3,'Riya','898383')

--unique
drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
select*from Emp
alter table Emp add City nvarchar(50) not null
alter table Emp drop column City
select*from Emp
--------------------------------------
drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
insert into Emp values (1,'Sam','9876543210','sam@yahoo.com')
insert into Emp values (2,'Ravi','9876543210','rav1256@gmail.com')
insert into Emp values (1,'Sam','9876543210','sam@yahoo.com')
-------------------------------------------------------------------------------
--identity(seed,increment)
drop table Student
create table Student
(SId int identity,
SName varchar(50) not null,
Sfee float)
insert into Student(SName,Sfee) values ('Ravi',5000.50)
 insert into Student(SName,Sfee) values ('Ani',3000.50)
  insert into Student(SName,Sfee) values ('Joy',4500.50)
 select*from Student
 insert into Student(SName,SFee) values ('Riya',4500.20)
 ---------------------------------------------------------------
 drop table Salary
 create table Salary
 (Grade varchar(1) primary key,
 BasicSalary float,
 HRA as BasicSalary*0.10 persisted,
 TA as BasicSalary*0.15 persisted,
 DA as BasicSalary*0.20 persisted
 )

 insert into Salary values('A',10000)
 select*from Salary
 insert into Salary values('B',5000)

 select Grade,BasicSalary,HRA,TA,DA, BasicSalary+TA+DA+HRA as 'Net Salary' from Salary
 insert into Salary values ('C',2000)
 insert into Salary values ('D',1000)

 select max(BasicSalary) as 'Max Basic' from Salary
 select min(BasicSalary) as 'Min Basic' from Salary
 select avg(BasicSalary) as 'Average Basic' from Salary
 --------------------------------------------------------------------------
 --foreign key
 create table Category
 (CatId int primary key,
 CategoryName nvarchar(50)not null unique
 )
 insert into Category values (1,'Electronics'),(2,'Clothing'),(3,'Home Decoration'),(4,'Mobile')
 select*from Category order by CatId
 create table Product
 (PId int primary key identity,
 PName nvarchar(50) not null,
 PPrice float not null,
 ProductCategory int foreign key references Category
 )
 insert into Product values ('IPhone-17',5000,4)
 insert into Product values ('Nothing-31', 2000,4)
 insert into Product values ('Washing Machine', 4000,1)
 select*from Product
 insert into Product values('Shirt',200,2)
 insert into Product values('T-Shirt',199,2)
 insert into Product values('Jeans',399,2)
 insert into Product values('Remote',209,5)
 --The INSERT statement conflicted with the FOREIGN KEY constraint "FK__Product__Product__693CA210".
 --The conflict occurred in database "OurDb", table "dbo.Category", column 'CatId'.
 select*from Category
 select*from Product
 --select column from table1 join table2 on CommonColumn
 select*from Product join Category on Product.ProductCategory=Category.CatId

 select p.PId,p.PName,p.PPrice,p.ProductCategory,c.CategoryName 
 from Product join Category c 
 on p.ProductCategory=C.CatId