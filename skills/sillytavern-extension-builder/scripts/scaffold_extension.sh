#!/usr/bin/env bash
set -euo pipefail

usage() {
    cat <<'USAGE'
Usage:
  scaffold_extension.sh [--template default|slash] <target-root> <extension-slug> [display-name] [author] [homepage]

Example:
  scaffold_extension.sh --template slash /path/to/SillyTavern/public/scripts/extensions/third-party my-cool-ext "My Cool Ext" "you" "https://github.com/you/my-cool-ext"
USAGE
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
    usage
    exit 0
fi

TEMPLATE_KIND="default"
while [ "$#" -gt 0 ]; do
    case "${1:-}" in
        --template)
            TEMPLATE_KIND="${2:-}"
            shift 2
            ;;
        *)
            break
            ;;
    esac
done

if [ "$#" -lt 2 ]; then
    usage
    exit 1
fi

TARGET_ROOT="$1"
EXT_SLUG="$2"
EXT_DISPLAY_NAME="${3:-$EXT_SLUG}"
EXT_AUTHOR="${4:-unknown}"
EXT_HOMEPAGE="${5:-https://github.com/your-org/$EXT_SLUG}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
case "$TEMPLATE_KIND" in
    default) TEMPLATE_DIR="${SCRIPT_DIR%/scripts}/assets/templates/extension" ;;
    slash) TEMPLATE_DIR="${SCRIPT_DIR%/scripts}/assets/templates/extension-slash" ;;
    *)
        echo "error: unsupported template kind: $TEMPLATE_KIND (expected: default or slash)" >&2
        exit 1
        ;;
esac
TARGET_DIR="${TARGET_ROOT%/}/${EXT_SLUG}"

if [ -e "$TARGET_DIR" ]; then
    echo "error: target directory already exists: $TARGET_DIR" >&2
    exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$TEMPLATE_DIR/manifest.json" "$TARGET_DIR/manifest.json"
cp "$TEMPLATE_DIR/index.js" "$TARGET_DIR/index.js"
cp "$TEMPLATE_DIR/style.css" "$TARGET_DIR/style.css"
cp "$TEMPLATE_DIR/settings.html" "$TARGET_DIR/settings.html"

escape_sed() {
    printf '%s' "$1" | sed -e 's/[\/&]/\\&/g'
}

replace_in_file() {
    local file="$1"
    sed -i.bak \
        -e "s/__EXT_SLUG__/$(escape_sed "$EXT_SLUG")/g" \
        -e "s/__EXT_DISPLAY_NAME__/$(escape_sed "$EXT_DISPLAY_NAME")/g" \
        -e "s/__EXT_AUTHOR__/$(escape_sed "$EXT_AUTHOR")/g" \
        -e "s#__EXT_HOMEPAGE__#$(escape_sed "$EXT_HOMEPAGE")#g" \
        "$file"
    rm -f "$file.bak"
}

replace_in_file "$TARGET_DIR/manifest.json"
replace_in_file "$TARGET_DIR/index.js"
replace_in_file "$TARGET_DIR/settings.html"

cat <<EOF
Created extension scaffold:
  $TARGET_DIR
Template:
  $TEMPLATE_KIND

Files:
  manifest.json
  index.js
  style.css
  settings.html
EOF
