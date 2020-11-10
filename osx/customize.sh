#! /bin/zsh

# Show full path in Finder
defaults write com.apple.finder _FXShowPosixPathInTitle -boolean True; killall Finder

# Put the Dock on the right
# https://support.apple.com/guide/terminal/edit-property-lists-apda49a1bb2-577e-4721-8f25-ffc0836f6997/mac
defaults write com.apple.dock orientation right

# Enable three finger drag
#defaults -currentHost write NSGlobalDomain com.apple.trackpad.threeFingerSwipeGesture -boolean True