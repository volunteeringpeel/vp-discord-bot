use ue1nsds7guapeehr;

drop table if exists execList;

create table if not exists execList (
    userID      text not null,
    username    text not null,
    channel     text not null
);