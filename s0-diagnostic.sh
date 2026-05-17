#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# S0 SYSTEM PILOT: HARDWARE COMPATIBILITY & LIFTOFF CONFIGURATION
# ARCHITECTURE: LAYER 0 EDGE ORCHESTRATION
# ==============================================================================

CRIMSON='\033[1;31m'
SILVER='\033[1;37m'
DARK_GRAY='\033[1;30m'
NC='\033[0m'

clear
echo -e "${CRIMSON}============================================================${NC}"
echo -e "${SILVER}           🔴 SOVEREIGN ZERO (S0) // COMMAND PILOT 🔴        ${NC}"
echo -e "${CRIMSON}============================================================${NC}"
echo -e "${DARK_GRAY}[*] Booting localized core diagnostics...${NC}"
sleep 1

# 1. Hardware Architecture Scrutiny
ARCH=$(uname -m)
echo -ne "${SILVER}[*] Auditing hardware instruction set... ${NC}"
if [ "$ARCH" != "aarch64" ] && [ "$ARCH" != "arm64" ]; then
    echo -e "${CRIMSON}[FAIL] Architecture detected: $ARCH${NC}"
    exit 1
else
    echo -e "${SILVER}[OK] Native ARM64 environment verified.${NC}"
fi

# 2. File Sandbox and Local Path Isolation Check
TERMUX_HOME="/data/data/com.termux/files/home"
if [ "$HOME" != "$TERMUX_HOME" ]; then
    export HOME=$TERMUX_HOME
fi
echo -e "${SILVER}[OK] Local paths locked to $HOME.${NC}"

# 3. Storage Boundary Check (Android Permission Intercept & Hard Lock)
echo -e "${SILVER}[*] Interrogating shared memory partitions...${NC}"
if [ ! -d "$HOME/storage/shared" ]; then
    echo -e "${CRIMSON}[BLOCKED] Shared storage symlinks missing.${NC}"
    termux-setup-storage
    COUNTER=0
    while [ ! -d "$HOME/storage/shared" ]; do
        sleep 1
        COUNTER=$((COUNTER + 1))
        if [ $COUNTER -ge 15 ]; then
            echo -e "${CRIMSON}\n[CRITICAL] Storage access timeout. Halting.${NC}"
            exit 1
        fi
        echo -n -e "${DARK_GRAY}.${NC}"
    done
    echo -e "\n${SILVER}[OK] Storage handshake established dynamically.${NC}"
else
    echo -e "${SILVER}[OK] Shared storage pipeline accessible.${NC}"
fi

echo -e "${CRIMSON}------------------------------------------------------------${NC}"
echo -e "${SILVER}[SUCCESS]: Baseline environment is functional and secure.${NC}"
echo -e "${DARK_GRAY}Ready to initialize advanced workspace vaults.${NC}"
echo -e "${CRIMSON}============================================================${NC}"
