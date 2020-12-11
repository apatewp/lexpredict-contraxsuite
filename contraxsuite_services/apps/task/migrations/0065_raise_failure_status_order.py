# Generated by Django 2.2.10 on 2020-04-20 15:04

from django.db import migrations, connection


def run_migration(_apps, _schema_editor):
    # give 'FAILURE' status less weight so as FAILURE to pop up
    # from child task to its parent
    with connection.cursor() as cursor:
        cursor.execute('''
create or replace function fix_task_progress_with_status(src_progress float, src_status int) returns float as $$
    declare
        first_finished_status constant int := 7;
    begin
        if src_status = 1 or src_status >= first_finished_status then
            return 100;
        else
            return src_progress;
        end if;
    end;
$$ language plpgsql;


create or replace function task_status_precedence(status varchar = 'PENDING') returns int as $$
    declare
        res int = 2;
        precedence hstore := 'FAILURE=>1, PENDING=>2, RETRY=>3, REJECTED=>4, RECEIVED=>5, STARTED=>6, REVOKED=>7, SUCCESS=>8'::hstore;
    begin
        if status is null then
            return 2;
        else
            res := precedence -> status;
            if res is null then
                return 2;
            else
                return res;
            end if;
        end if;
    end;
$$ language plpgsql;


create or replace function task_status_to_str(status int = null) returns varchar as $$
    declare
        res int = 1;
        precedence varchar array[8] := ARRAY['FAILURE', 'PENDING', 'RETRY', 'REJECTED', 'RECEIVED', 'STARTED', 'REVOKED', 'SUCCESS'];
    begin
        if status is null or status < 1 or status > 8 then
            return 'PENDING';
        else
            return precedence[status];
        end if;
    end;
$$ language plpgsql;
        ''')


def revert_migration(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute('''
create or replace function fix_task_progress_with_status(src_progress float, src_status int) returns float as $$
    declare
        first_finished_status constant int := 6;
    begin
        if src_status >= first_finished_status then
            return 100;
        else
            return src_progress;
        end if;
    end;
$$ language plpgsql;


create or replace function task_status_precedence(status varchar = 'PENDING') returns int as $$
    declare
        res int = 1;
        precedence hstore := 'PENDING=>1, RETRY=>2, REJECTED=>3, RECEIVED=>4, STARTED=>5, REVOKED=>6, FAILURE=>7, SUCCESS=>8'::hstore;
    begin
        if status is null then
            return 1;
        else
            res := precedence -> status;
            if res is null then
                return 1;
            else
                return res;
            end if;
        end if;
    end;
$$ language plpgsql;


create or replace function task_status_to_str(status int = null) returns varchar as $$
    declare
        res int = 1;
        precedence varchar array[8] := ARRAY['PENDING', 'RETRY', 'REJECTED', 'RECEIVED', 'STARTED', 'REVOKED', 'FAILURE', 'SUCCESS'];
    begin
        if status is null or status < 1 or status > 8 then
            return 'PENDING';
        else
            return precedence[status];
        end if;
    end;
$$ language plpgsql;

        ''')


class Migration(migrations.Migration):
    dependencies = [
        ('task', '0064_task_spawned_processes'),
    ]

    operations = [
        migrations.RunPython(run_migration, reverse_code=revert_migration)
    ]