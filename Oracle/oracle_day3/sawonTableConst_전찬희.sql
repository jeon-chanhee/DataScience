create table sawon (
sabun number(3),
constraint sawon_sabun_pk primary key (sabun),
saname varchar2(10) constraint sawon_saname_nn  not null,
deptno number(3),
constraint sawon_deptno_fk foreign key (deptno)
references dept(deptno) on delete cascade,
sajob varchar2(10),
sapay number(10),
sahire date default sysdate,
sasex varchar2(6),
constraint sawon_sasex_ck CHECK(sasex in('남자','여자')),
samgr number(3),
constraint sawon_samgr_fk foreign key (samgr)
references sawon(sabun)
);