/*
Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')

 */


SELECT MAX(Salary) AS SecondHighestSalary
    FROM Employee
    WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee);

SELECT IFNULL(
    (SELECT distinct Salary as SecondHighestSalary FROM Employee order by Salary desc limit 1,1),
    null);

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);

SELECT (SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary;


