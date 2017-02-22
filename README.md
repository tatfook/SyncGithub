## SyncGithub
Synchronizing sources from github.com to git.tatfook.com.
We use [CI:Sync-From-Github-To-Tatfook](http://ci.paraengine.com/job/Sync-From-Github-To-Tatfook/) to invoke this project.
### CI Command
```
python SyncGithub/src/main.py
```
### How to use CI to sync a new project
- Create a new project on [github](https://github.com/NPLPackages), for example "MyProject".
- Create a same name project on [git.tatfook.com](https://git.tatfook.com:8443/npl), for example "MyProject".
- Checkout [SyncGithub](https://git.tatfook.com:8443/npl/SyncGithub) and edit main.py and
- insert a new line of ["MyProject","https://github.com/NPLPackages/MyProject.git","https://git.tatfook.com:8443/npl/MyProject.git"] to the array of depots.
- Commit your changed
- Run [CI:Sync-From-Github-To-Tatfook](http://ci.paraengine.com/job/Sync-From-Github-To-Tatfook/)

### Internal Logics
- Pull the project from github.com to the folder of "from_source" where are source projects.
- Pull the project from git.tatfook.com to the folder of "to_source" where are destination projects.
- Copy all files from "from_source/*" to "to_source/*" except "from_source/*/.git".
- Push projects under the folder of "to_source".
- Note: One project which can be synchronized should existed on github.com and git.tatfook.com.

### Config
We can change the values in [main.py](https://git.tatfook.com:8443/npl/SyncGithub/blob/master/src/main.py) to control which depot can be synchronized.
```python
depots = [
	# depots in NPLPackages
	# Project name			Source depot													Dest depot
	["NplCefBrowser",		"https://github.com/NPLPackages/NplCefBrowser.git",				"git@git.tatfook.com:npl/NplCefBrowser.git"],
	["main",				"https://github.com/NPLPackages/main.git",						"git@git.tatfook.com:npl/main.git"],
	["NplCef3",				"https://github.com/NPLPackages/NplCef3.git",					"git@git.tatfook.com:npl/NplCef3.git"],
	["NplCadLibrary",		"https://github.com/NPLPackages/NplCadLibrary.git",				"git@git.tatfook.com:npl/NplCadLibrary.git"],
	["NplClusterManager",	"https://github.com/NPLPackages/NplClusterManager.git",			"git@git.tatfook.com:npl/NplClusterManager.git"],
	["paracraft",			"https://github.com/NPLPackages/paracraft.git",					"git@git.tatfook.com:npl/paracraft.git"],
	["CPL",					"https://github.com/NPLPackages/CPL.git",						"git@git.tatfook.com:npl/CPL.git"],
	["JsDeps",				"https://github.com/NPLPackages/JsDeps.git",					"git@git.tatfook.com:npl/JsDeps.git"],
	["ModelVoxelizer",		"https://github.com/NPLPackages/ModelVoxelizer.git",			"git@git.tatfook.com:npl/ModelVoxelizer.git"],
	["WebServerExample",	"https://github.com/NPLPackages/WebServerExample.git",			"git@git.tatfook.com:npl/WebServerExample.git"],
	["wiki",				"https://github.com/NPLPackages/wiki.git",						"git@git.tatfook.com:npl/wiki.git"],
	["NPLPackages",			"https://github.com/NPLPackages/NPLPackages.git",				"git@git.tatfook.com:npl/NPLPackages.git"],


	# depots in tatfook
	["wikicraft",			"https://github.com/tatfook/wikicraft.git",						"git@git.tatfook.com:npl/wikicraft.git"],
	["NPLGitCloud",			"https://github.com/tatfook/NPLGitCloud.git",					"git@git.tatfook.com:npl/NPLGitCloud.git"],
	["EarthMod",			"https://github.com/tatfook/EarthMod.git",						"git@git.tatfook.com:npl/EarthMod.git"],
	["NplCloudIDE",			"https://github.com/tatfook/NplCloudIDE.git",					"git@git.tatfook.com:npl/NplCloudIDE.git"],
	["WorldShare",			"https://github.com/tatfook/WorldShare.git",					"git@git.tatfook.com:npl/WorldShare.git"],
	["NplCefBrowserDev",	"https://github.com/tatfook/NplCefBrowserDev.git",				"git@git.tatfook.com:npl/NplCefBrowserDev.git"],
	["_E4_B8",				"https://github.com/tatfook/_E4_B8.git",						"git@git.tatfook.com:npl/_E4_B8.git"],
	["EarthGIS",			"https://github.com/tatfook/EarthGIS.git",						"git@git.tatfook.com:npl/EarthGIS.git"],
	["BMaxToParaXExporter",	"https://github.com/tatfook/BMaxToParaXExporter.git",			"git@git.tatfook.com:npl/BMaxToParaXExporter.git"],
	["NPLCAD",				"https://github.com/tatfook/NPLCAD.git",						"git@git.tatfook.com:npl/NPLCAD.git"],
	["CDN",					"https://github.com/tatfook/CDN.git",							"git@git.tatfook.com:npl/CDN.git"],
	["NplVoxelizer",		"https://github.com/tatfook/NplVoxelizer.git",					"git@git.tatfook.com:npl/NplVoxelizer.git"],
	["website_peitian",		"https://github.com/tatfook/website_peitian.git",				"git@git.tatfook.com:npl/website_peitian.git"],
	["HTML5Monitor",		"https://github.com/tatfook/HTML5Monitor.git",					"git@git.tatfook.com:npl/HTML5Monitor.git"],
	["GitUploader",			"https://github.com/tatfook/GitUploader.git",					"git@git.tatfook.com:npl/GitUploader.git"],
	["SummerOfCode",		"https://github.com/tatfook/SummerOfCode.git",					"git@git.tatfook.com:npl/SummerOfCode.git"],
	["FirstApp",			"https://github.com/tatfook/FirstApp.git",						"git@git.tatfook.com:npl/FirstApp.git"],


	["NPLRuntime",			"https://github.com/LiXizhi/NPLRuntime.git",					"git@git.tatfook.com:npl/NPLRuntime.git"],
	
]
```

### Git global config on linux /etc/gitconfig
```
[http]
    sslVerify = false
[user]
    email = yourname@***.com
    name = yourname

```
### How to use ssh to pull/push a repository on linux
- Generating a new SSH key pair [[help]](https://help.github.com/articles/connecting-to-github-with-ssh/)
- Copy the private file of "git.tatfook.priviate.key" to ~/.ssh/
- Copy the text from the public file of "git.tatfook.priviate.key.pub" to your account under github.com/git.tatfook.com
- Adding below text to /etc/ssh/ssh_config, [Where is ssh config](https://linux.die.net/man/5/ssh_config)
```
Host git.tatfook.com
RSAAuthentication yes
IdentityFile ~/.ssh/git.tatfook.priviate.key
 ```
- Run git
```
git clone git@git.tatfook.com:npl/FirstApp.git
```

### How to use ssh to pull/push a repository on windows
- Generating a new SSH key pair [[help]](https://help.github.com/articles/connecting-to-github-with-ssh/)
- Copy the private file of "git.tatfook.priviate.key" to ~/.ssh/
- Copy the text from the public file of "git.tatfook.priviate.key.pub" to your account under github.com/git.tatfook.com
- Adding below text to [Git installed folder]/etc/ssh/ssh_config, [Where is ssh config](https://linux.die.net/man/5/ssh_config)
```
Host git.tatfook.com
RSAAuthentication yes
IdentityFile ~/.ssh/git.tatfook.priviate.key
 ```
- Run git
```
git clone git@git.tatfook.com:npl/FirstApp.git
```
- Screenshot

![20170222160105](https://cloud.githubusercontent.com/assets/5885941/23205842/50cbc52a-f926-11e6-9bc1-f423d41fa477.jpg)
