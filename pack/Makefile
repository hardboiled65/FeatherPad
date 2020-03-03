default:
	mkdir -p FeatherPad.AppDir/usr/lib
	# Find executable.
	# CMake
	if [ -d "../build/featherpad" ]; then \
		echo "It seems compiled with CMake."; \
		cp ../build/featherpad/featherpad FeatherPad.AppDir/usr/bin/; \
	else \
		cp ../featherpad/featherpad FeatherPad.AppDir/usr/bin/; \
	fi

clean:
	rm -rf FeatherPad.AppDir/usr/bin/featherpad
	rm -rf FeatherPad.AppDir/usr/lib
