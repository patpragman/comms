# config file for the comms app
# Alex and Pat
# 10/2/21
from passlib.context import CryptContext


class Config:

    ssl_context = "adhoc"  # change in production
    secret_key = b"Seriously, fucking change me."

    pwd_context = CryptContext(schemes=["pbkdf2_sha256"],
                               deprecated="auto")  # this is the password context for passlib


class DatabaseConfig:
    """
    Basic Database configuration
    Pat Pragman
    10/2/21

    This class stores the SQL commands and the location of the database.
    In this app, we're not using an Object Relation Mapping, we're dealing
    with raw SQL.
    """

    path = "messages.db"

    # commands!

    message_upsert_sql = """
                            insert or replace into message (
                                id,
                                sender,
                                recipient,
                                message,
                                datetime)
                                
                            values (?,?,?,?,?);
                            """

    user_upsert_sql = """
                            insert or replace into user (
                                id,
                                username,
                                password)
                                
                                
                            values (?,?,?);
                            """

    add_user_sql = """
    
                        insert into users (
                                username,
                                password)
                                
                                
                            values (?,?);
    """

    select = """
                select * from {table};
    """

    select_where = """
                    select * from {table} where {};
    """

    user_exists = """
                    SELECT * FROM users WHERE username = '{user}';
    """