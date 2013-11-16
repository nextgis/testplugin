set plugin_name=testplugin

mkdir %plugin_name%
xcopy *.py %plugin_name%
xcopy README.md %plugin_name%
xcopy metadata.txt %plugin_name%
zip -r %plugin_name%.zip %plugin_name%
del /Q %plugin_name%
rd %plugin_name%