use SalesDb
create table Products
(ProductID int primary key,
ProductName nvarchar(100),
Category nvarchar(50),
UnitPrice decimal(10,2)
)
insert into Products values (1,'Laptop Xiaomi','Electronics','1200')
select*from Products
insert into Products values
(2,'Wireless keyboard','Electronics','1200'),
(3,'Wireless mouse','Electronics','1200'),
(4,'Table','Furniture','1300'),
(5,'PenBox','Stationary','15'),
(6,'Chair','Furniture','1200'),
(7,'Notebook','Stationary','10')
select*from Products

create table Sales
(SalesID int primary key identity,
ProductId int foreign key references Products(ProductId),
Region nvarchar(50) check (Region in('East','West','North','South')),
Quantity int, 
SalesDate date,
)
--YY-MM-DD
insert into Sales (ProductId,Region,Quantity,SalesDate) values (1,'East',5,'2024-5-03')
select*from Sales
insert into Sales
(ProductId,Region,Quantity,SalesDate)
values (2,'West',5,'2024-5-15'),
(3,'North',5,'2024-7-18'),
(4,'South',7,'2024-1-13'),
(1,'West',3,'2024-4-04'),
(3,'East',8,'2024-2-23'),
(2,'South',21,'2024-5-23'),
(2,'East',19,'2024-8-18'),
(2,'North',15,'2024-5-03')

select*from Products
select*from Sales

truncate table Sales
INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
(1, 'East', 5, '2024-01-10'),
(2, 'West', 10, '2024-01-12'),
(3, 'North', 3, '2024-02-05'),
(4, 'South', 8, '2024-02-10'),
(5, 'East', 2, '2024-03-01'),
(1, 'West', 7, '2024-03-15'),
(3, 'North', 4, '2024-04-03'),
(2, 'South', 6, '2024-04-10'),
(5, 'East', 3, '2024-05-02'),
(4, 'West', 9, '2024-05-10')
 