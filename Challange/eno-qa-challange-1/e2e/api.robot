*** Settings ***
Library    RequestsLibrary
Test Setup  open session
Test Teardown   close session

*** Variables ***
${pet_base_url}  https://petstore3.swagger.io
${postman_base_url}  https://postman-echo.com

*** Keywords ***
open session
    Create Session    api    ${pet_base_url}

close session
    Delete All Sessions

*** Test Cases ***
Test Challenge 2
    ${resp} =   GET On Session    api    /api/v3/pet/findByStatus       params=status=available
    Status Should Be    200     ${resp}
    FOR    ${element}    IN    @{resp.json()}
        ${body}=    Create Dictionary   name=${element['name'].upper()}
        ${header}=  Create Dictionary   Content-Type=application/json
        ${postResp} =    POST    ${postman_base_url}/post  json=${body}  headers=${header}
        Status Should Be    200     ${postResp}
        Should Be Equal    ${element['name'].upper()}    ${postResp.json()['json']['name']}
    END



