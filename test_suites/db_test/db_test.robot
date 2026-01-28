*** Settings ***
Resource    ../../resource/env.resource
Library    libraries.db.mongo_database.MongoDatabase    ${MONGO_URI}    ${DB_NAME}
*** Test Cases ***
Check connection
    Connect