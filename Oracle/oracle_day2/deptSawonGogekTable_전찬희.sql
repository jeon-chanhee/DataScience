drop table depttable;
drop table sawontable;
drop table gogektable;

create table deptTable (
deptno number(3),
dname varchar2(10),
loc varchar2(10)
);

create table gogektable (
gobun number(3),
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3)
);

create table sawontable (
sabun number(3),
saname varchar2(10),
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date,
sasex varchar2(4),
samgr number(3)
);

select*from tab;