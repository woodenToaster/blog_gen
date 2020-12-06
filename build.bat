
@echo off

if not exist "build" mkdir build
pushd build

set PREPROCESSOR_DEFINES=
set COMPILERFLAGS=/W4 /FC /Gm- /Zi /GR- /nologo /EHa- /MTd /Oi /Od
set LINK_LIBS=

cl %PREPROCESSOR_DEFINES% %COMPILERFLAGS% ..\blog_gen.cpp /link /incremental:no /opt:ref %LINK_LIBS% /SUBSYSTEM:CONSOLE

popd
if %errorlevel% neq 0 exit /b %errorlevel%