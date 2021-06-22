drop table dept;

create table dept (
deptno number(3),
dname varchar2(20),
loc varchar2(20)
);

drop table sawontable;

create table sawontable (
sabun number(3),
saname varchar2(10),
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date,
sasex varchar2(6),
samgr number(3)
);

drop table gogektable;

create table gogektable (
gobun number(3),
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3)
);

select owner, constraint_name,table_name  
from user_constraints;