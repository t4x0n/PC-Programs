REM %FILENAME% %ISSUE_PATH% %XML_FILE% ',v1

set FILENAME=%1
set NEW_FILENAME=%2
set ISSUE_PATH=%3
set XML_FILE=%4

rem RENOMEIA IMAGEM ORIGINAL TIFF PARA PMC

if exist %XML_FILE% copy %XML_FILE% %ISSUE_PATH%\pmc\%NEW_FILENAME%.xml
if exist %XML_FILE% copy %XML_FILE% %ISSUE_PATH%\pmc_work\%FILENAME%\%NEW_FILENAME%.xml

if exist %ISSUE_PATH%\pdf\%FILENAME%.pdf copy %ISSUE_PATH%\pdf\%FILENAME%.pdf %ISSUE_PATH%\pmc\%NEW_FILENAME%.pdf
