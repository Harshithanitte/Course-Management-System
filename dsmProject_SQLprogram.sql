create database elearning;
use elearning;

create table student
(
 sid varchar(10) primary key,
 sname varchar(30) not null,
 college varchar(100),
 email varchar(50),
 age int,
 gender char(1),
 dob date
 );
create table instructor
(
 iid varchar(10) primary key,
 iname varchar(30) not null,
 salary int,
 domain varchar(50)
 );
create table course
(
 cid varchar(10) primary key,
 title varchar(50) not null unique,
 fees int,
 duration int,
 iid varchar(10) references instructor(iid)
);

create table result
(
 sid varchar(10) references student(sid),
 cid varchar(10) references course(cid),
 percentage float,
 grade varchar(2),
 primary key(sid,cid)
);
create table domain
(
 did varchar(10),
 dname varchar(50) not null unique,
 iid varchar(10) references instructor(iid),
 training_period int,
 primary key(did,iid)
);

create table progress
(
 sid varchar(10) references student(sid),
 cid varchar(10) references course(cid),
 course_status int,
 deadline date,
 primary key(sid,cid)
 );

insert into student values('22s001','kavya','nmamit','kavya@gmail.com',20,'f','2002-09-23');
insert into student values('22s002','rahul','mit','rahul@gmail.com',21,'m','2001-11-29');
insert into student values('22s003','karthik','nmamit','karthik@gmail.com',20,'m','2002-04-12');
insert into student values('22s004','sahana','nitk','sahana@gmail.com',22,'f','2000-05-23');
insert into student values('22s005','nayana','nmamit','nayana@nammit.in',21,'f','2001-07-11');


insert into instructor values('i001','ravi adiga',25000,'cyber security');
insert into instructor values('i002','santhosh',30000,'data Science');
insert into instructor values('i003','gayatri g',45000,'IOT');
insert into instructor values('i004','sahana p',75000,'Artificial Intelligence');

insert into course values('c001','c',5000,6,'i003');
insert into course values('c002','python',4500,4,'i004');
insert into course values('c003','c++',6000,6,'i002');
insert into course values('c004','unix',6000,5,'i001');

insert into result values('22s001','c001',89,'A');
insert into result values('22s003','c004',76,'B');


insert into domain values('d001','cyber security','i001',8);
insert into domain values('d002','IOT','i003',12);
insert into domain values('d003','Data Science','i002',12);
insert into domain values('d004','Artificial Intelligence','i004',15);

insert into progress values('22s001','c001',100,'2022-11-25');
insert into progress values('22s001','c002',25,'2023-11-25');
insert into progress values('22s002','c002',40,'2022-12-13');
insert into progress values('22s003','c004',100,'2022-08-17');
insert into progress values('22s004','c003',78,'2023-03-07');
insert into progress values('22s005','c004',2,'2023-05-09');
 

select * from student;
select * from instructor;
select * from course;
select * from result;
select * from domain;
select * from progress;






