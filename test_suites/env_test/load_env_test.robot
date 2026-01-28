*** Settings ***
Library    libraries.utils.env_loader.EnvLoader
Suite Setup    Load    resource/env/.env.local
*** Test Cases ***
Check env file has been loaded
    Log    %{TITLE}
    Log    Current running test ${TEST_NAME}
