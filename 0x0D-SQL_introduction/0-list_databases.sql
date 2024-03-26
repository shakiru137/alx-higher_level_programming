# Start MySQL in safe mode without password authentication
sudo mysqld_safe --skip-grant-tables --skip-networking &

# Sleep for a moment to ensure MySQL is fully started
sleep 5

# Execute MySQL query to list databases
SHOW DATABASES;

# Stop MySQL safe mode
sudo killall mysqld_safe
