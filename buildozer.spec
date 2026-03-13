[app]

# (str) Title of your application
title = CyberExpert

# (str) Package name
package.name = cyberexpert

# (str) Package domain (needed for android)
package.domain = com.sakib

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (e.g. you can exclude test files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.2.0

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# OSX Specific
#
# author = © Copyright Info
# author.email = you@example.com
# author.website = https://example.com

# Android Specific
#
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for new android toolchain)
# Supported formats: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# presplash_color = #0A0A1A

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is 'org.kivy.android.PythonActivity'
# android.entrypoint = org.kivy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
# android.add_src =

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (list) Add java compile options
# android.compile_options = sourceCompatibility=1.8,targetCompatibility=1.8

# (str) Python for android distribution (eg. continuous, prebuilt, ...)
# android.p4a_distribution = continuous

# (str) Android app theme
# android.theme = @android:style/Theme.NoTitleBar

# (str) app style (eg. fullscreen, holographic, legacy, sensor)
# android.app_lib = 1

# (str) If True, you can pause for multidex
# android.multidex = False

# (str) If True, use play services features
# android.play_services = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (int) Number of threads to use for building, default logical cores count
# android.num_threads = 4

# (str) Display icon in the Android notification bar
# android.notification_icon = data/icon.png

# (str) The directory for the release signing key
# android.release_key.store =

# (str) The alias for the release signing key
# android.release_key.alias =

# (str) Password for the release signing key
# android.release_key.password =

# (str) Password for the release signing key, if different from key password
# android.release_key.alias_password =

# (str) The directory for the debug signing key
# android.debug_key.store =

# (str) The alias for the debug signing key
# android.debug_key.alias =

# (str) Password for the debug signing key
# android.debug_key.password =

# (str) Password for the debug signing key, if different from key password
# android.debug_key.alias_password =

# (str) Value to set for the debug/build.properties "key.store" property
# android.key.store =

# (str) Value to set for the debug/build.properties "key.alias" property
# android.key.alias =

# (str) Value to set for the debug/build.properties "key.store.password" property
# android.key.store.password =

# (str) Value to set for the debug/build.properties "key.alias.password" property
# android.key.alias.password =

# (bool) If True, then project will be compiled and packaged with the NiVidia
# Tegra NDK
# android.nvidia = False

# (bool) If True, then the generated parts of the project will be cleaned on
# each build
android.clean_on_build = True

# (bool) If True, then the android library will be compiled only once
# android.library_rebuild = False

# (list) Android extra macros
# android.macros =

# (bool) If True, enable verbose build output
android.log_level = 2

# (bool) If True, copy the library to the device, and run it immediately
# android.live = False

# (list) The architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) The Python for android (p4a) branch or tag
# android.p4a_branch = master

# iOS Specific
#
# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir = ../kivy-ios
# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s

# (str) Should automatically install the dependencies. Use only for project
# creation and first build, for compilation set to 0.
auto_install = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer version is older than this version number
# warn_on_root = 1

# (str) Path to build artifact storage in absolute or relative to cwd
# build_to = ./.buildozer