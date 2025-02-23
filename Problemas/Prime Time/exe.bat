@echo off
REM Elimina el ejecutable anterior si existe
if exist p10200.exe del p10200.exe

REM Compilar el programa en C++
g++ -o p10200 p10200.cpp

REM Verificar si la compilación fue exitosa
if %errorlevel% neq 0 (
    echo Error: La compilacion fallo.
    pause
    exit /b
)

REM Eliminar el archivo de salida anterior si existe
if exist 1.out del 1.out

REM Ejecutar el programa con entrada y salida redirigidas
p10200.exe 1.in  1.out

REM Verificar si el archivo de salida se generó correctamente
if exist 1.out (
    echo Salida generada correctamente:
    type 1.out
) else (
    echo Error: No se genero el archivo 1.out.
)

echo.
echo Ejecucion finalizada.
pause
