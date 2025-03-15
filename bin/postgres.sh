#!/bin/bash


django() {

    project_name=$(basename $PWD)
    project_path="$PWD"
    manage_path="${project_path}/${project_name}/manage.py"

    if [ ! -f $manage_path ] ; then  # No project/manage.py
        echo "Error: Could not locate Django manage.py file."
        return -1
    fi

    if [ $# -eq 0 ] ; then
        echo "Django project detected."
    fi

    while [ ! $# -eq 0 ]
        do
            case "$1" in

                --help | -h)
                        echo "Django shortcut, unknown commands are forwarded to manage.py"
                        echo "  -c, --check         Run Django manage.py check."
                        echo "  --req           Install requirements."
                        echo "  -r, --run           Run server."
                        echo "  -s, --shell         Run Django shell plus."
                        echo "  -sd, --shell            Run Django shell plus. Debug DB (print sql)"
                        echo ""
                    ;;

                --check | -c)
                        python $manage_path check
                    ;;

                --shell | -s)
                        python $manage_path shell_plus --bpython
                    ;;

                --shell | -sd)
                        python $manage_path shell_plus --bpython --print-sql
                    ;;

                --run | -r)
                        python $manage_path runserver
                    ;;

                --req)
                        pip install -r $project_path/requirements.txt
                    ;;

                --mig | -m)
                        python $manage_path makemigrations
                        python $manage_path migrate
                    ;;

                --reset_migrations)
                        find . -path "*migrations*" -not -regex ".*__init__.py" -a -not -regex ".*migrations" | xargs rm -rf
                        python $manage_path makemigrations
                        ;;

                *)
                    python $manage_path "$@"
                    ;;

            esac
            shift
        done

}