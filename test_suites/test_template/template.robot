*** Settings ***
Test Template    Invalid Login Should Fail

*** Test Cases ***
Invalid Login 1    admin    wrong
Invalid Login 2    user     123456

*** Keywords ***
Invalid Login Should Fail
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Password    ${password}
    Submit Login
    Error Should Be Visible
