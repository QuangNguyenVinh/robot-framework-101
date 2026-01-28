*** Variables ***
${BASE_URL}    https://www.google.com

*** Keywords ***
Setup Test
    Open Browser    ${BASE_URL}    chrome

Teardown Test
    Close Browser
    
Global Setup
    Log    This is global setup
    
Global Teardown
    Log    This is global teardown
