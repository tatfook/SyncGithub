#coding=utf-8
import glob
import os
import string
import shutil
source_root = "from_source"
dest_root = "to_source"
init_depots_root = "init_depots"
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
def gitPull():
	print "gitPull-------------------------->"
	# Create source folder
	if not os.path.exists(source_root):
		os.makedirs(source_root)
	# Create destination folder
	if not os.path.exists(dest_root):
		os.makedirs(dest_root)
	for line in depots:
		depot_name = line[0]
		src_git = line[1]
		dest_git = line[2]
		gitPullOne(depot_name,src_git,source_root)
		gitPullOne(depot_name,dest_git,dest_root)
def gitPullOne(depot_name,git_url,root):
	print "gitPullOne-------------------------->"
	print git_url
	result = os.system("git ls-remote %s" % git_url)
	if result != 0:
		print "[Warning]:can't visit %s" % git_url
		return
	os.chdir("%s" % root)
	if os.path.isfile(depot_name + "/README.md"):
		os.chdir(depot_name)
		os.system("git reset --hard" )
		os.system("git pull" )
		os.chdir("..")
	else:
		os.system("git clone %s" % (git_url))
	os.chdir("..")
def gitPush():
	print "gitPush-------------------------->"
	for line in depots:
		depot_name = line[0]
		print line[2]
		os.chdir("%s/%s" % (dest_root,depot_name))
		os.system("git add ." )
		os.system("git commit -m'autosync'")
		os.system("git push")
		os.chdir("../..")
def getProjects(directory):
	"""
	Get project name.
	"""
	if os.path.exists(directory):
		for root, dirnames, filenames in os.walk(directory):
			return dirnames
def searchFiles(directory):
	"""
	Search a directory and return all its names of file except the directory of ".git"
	"""
	ignore_folder = directory + "/.git"
	matches = []
	if os.path.exists(directory):
		for root, dirnames, filenames in os.walk(directory):
			root = string.replace(root,"\\","/")
			if not bool(ignore_folder in root):
				for name in filenames:
					r = os.path.join(root, name)
					r = string.replace(r,"\\","/")
					matches.append(r)
	return matches
def cloneFiles(source_folder,dest_folder):
	"""
	Clone files
	"""
	print "cloneFiles-------------------------->"
	print "source_folder: %s" % source_folder
	print "dest_folder: %s" % dest_folder
	
	source_files = searchFiles(source_folder)
	dest_files = searchFiles(dest_folder)
	
	# Copy files
	for name in source_files:
		source_path = name
		dest_path = name.replace(source_root,dest_root)
		if os.path.exists(source_path):
			print "copy %s -> %s" % (source_path, dest_path)
			dir = os.path.dirname(dest_path)
			if not os.path.exists(dir):
				os.makedirs(dir)
			shutil.copy(source_path,dest_path)
def cloneAll():
	for line in depots:
		name = line[0]
		source_folder = source_root + "/" + name
		dest_folder = dest_root + "/" + name
		# Check destination folder
		if os.path.exists(dest_folder):
			cloneFiles(source_folder,dest_folder)
def main():
	gitPull()
	cloneAll()
	gitPush()
if __name__ == "__main__":
    main()