[app]
title = DurandTech Systen
package.name = durandtechsysten
package.domain = com.durandtechsysten.app
source.dir =.
source.include_exts = py,png
version = 2.0

[buildozer]
log_level = 2
warn_on_root = 0

[app:requirements]
requirements = python3,flet

[app:android]
icon = icon.png
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk_version = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.build_mode = debug
p4a.bootstrap = sdl2
