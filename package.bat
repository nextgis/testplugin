mkdir testplugin
xcopy *.py testplugin
xcopy README.md testplugin
xcopy metadata.txt testplugin
zip -r testplugin.zip testplugin
del /Q testplugin
rd testplugin