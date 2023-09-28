@echo off
setlocal enabledelayedexpansion

for /f %%a in (extensions.txt) do (
    code --install-extension %%a
)

endlocal
