#!/bin/bash
# validate-all.sh - Run all validation checks for the skill library
# Usage: ./validate-all.sh [options]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
TOOLS_DIR="$PROJECT_ROOT/tools/validators"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SKIP_EXTERNAL=false
QUIET=false
OUTPUT_FILE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-external)
            SKIP_EXTERNAL=true
            shift
            ;;
        --quiet)
            QUIET=true
            shift
            ;;
        --output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "=== AI Agent Skill Library - Full Validation ==="
echo "Project root: $PROJECT_ROOT"
echo ""

# Run Python validation script
cd "$PROJECT_ROOT"
python3 "$TOOLS_DIR/validate_skill.py" "$PROJECT_ROOT/categories" --all \
    ${SKIP_EXTERNAL:+--skip-external-links} \
    ${QUIET:+--quiet} \
    ${OUTPUT_FILE:+--output "$OUTPUT_FILE"}

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "\n${GREEN}✅ All validations PASSED${NC}"
else
    echo -e "\n${RED}❌ Some validations FAILED${NC}"
fi

exit $EXIT_CODE