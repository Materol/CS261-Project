#!/bin/bash

# Database can be initialised with ./cs261-database-setup.sh start postgres
# Database can be shutdown with ./cs261-database-setup.sh stop

# Setup postgres database in local directory
PGINSTALL="$PWD/cs261-db"

# Mark postgres variables to be passed to child process environments
export PGPATH="$PGINSTALL/postgres"
export PGHOST="$PGINSTALL/postgres/tmp"

# Abort if incorrect arguments are provided
# Shutdown the database server if stop command is provided
case $1 in
        stop)
    ./pg_ctl -D $PGPATH/data/ -l $PGPATH/datapg.log stop
    exit
                ;;
    start)
        ;;
        *)
        exit
            ;;
esac

if test -d "$PGINSTALL"
then
    echo "Database already exists."
else
# Create the database if it does not already exist
    mkdir -p $PGINSTALL/postgres/tmp $PGINSTALL/postgres/run
    ./initdb -D $PGINSTALL/postgres/data --locale=en_GB.utf8 --no-instructions 
    sed -e "s@.*unix_socket_directories = .*@unix_socket_directories = \x27$PGINSTALL/postgres/tmp\x27@" -e "s@\#listen_addresses = \x27localhost\x27@listen_addresses = \x27\x27@" ./postgresql.conf > $PGINSTALL/postgres/data/postgresql.conf
    cp ./pg_hba.conf $PGINSTALL/postgres/data/.
fi

# Start the database and login to postgres
./pg_ctl -D "$PGPATH/data/" -l "$PGPATH/datapg.log" start

./psql postgres