RED="\033[1;31m"
YELLOW="\033[1;33m"
GREEN="\033[1;32m"
BLUE="\033[1;34m"

NOFORMAT="\033[0m"

info() {
    printf "[${BLUE}INFO${NOFORMAT}] $1\n"
}

ok() {
    printf "[ ${GREEN}OK${NOFORMAT} ] $1\n"
}

warning() {
    printf "[${YELLOW}WARN${NOFORMAT}] $1\n"
}

error() {
    printf "[${RED}ERROR${NOFORMAT}] $1\n"
}
