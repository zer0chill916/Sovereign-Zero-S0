#!/usr/bin/env python3
# ==============================================================================
# S0 SYSTEM PILOT: CRYPTOGRAPHIC LEDGER ENGINE & BALANCE ORCHESTRATION
# LAYER 1: LOCAL PROTOCOL VALIDATION
# ==============================================================================

import os
import json
import hashlib
import time
import sys

# Terminal UI Colors
CRIMSON = '\033[1;31m'
SILVER = '\033[1;37m'
DARK_GRAY = '\033[1;30m'
NC = '\033[0m'

class S0LedgerEngine:
    def __init__(self, node_dir="~/.config/s0/"):
        self.node_path = os.path.expanduser(node_dir)
        self.ledger_file = os.path.join(self.node_path, "local_ledger.json")
        self.ensure_infrastructure()

    def ensure_infrastructure(self):
        """Creates secure directory layers and initializes the genesis state."""
        try:
            if not os.path.exists(self.node_path):
                os.makedirs(self.node_path, mode=0o700)
                
            if not os.path.exists(self.ledger_file):
                # Generate a unique genesis identifier for this independent node
                seed_string = f"{time.time()}-{os.getpid()}"
                node_uuid = hashlib.sha256(seed_string.encode()).hexdigest()
                
                initial_state = {
                    "node_identity": node_uuid,
                    "balance_s0": 10.00000000,  # Baseline operational token allocation
                    "sequence_nonce": 0,
                    "last_sync_timestamp": int(time.time()),
                    "network_tier": 1
                }
                
                with open(self.ledger_file, 'w') as f:
                    json.dump(initial_state, f, indent=4)
                print(f"{SILVER}[+]{NC} Genesis block created successfully for Node: {DARK_GRAY}{node_uuid[:16]}...{NC}")
        except Exception as e:
            print(f"{CRIMSON}[CRITICAL] Infrastructure allocation failed: {e}{NC}")
            sys.exit(1)

    def verify_and_deduct(self, execution_cost=0.0001):
        """Validates current token balances prior to executing an advanced local script."""
        if not os.path.exists(self.ledger_file):
            print(f"{CRIMSON}[ERROR] Local ledger file missing. Integrity compromised.{NC}")
            return False

        try:
            with open(self.ledger_file, 'r') as f:
                data = json.load(f)

            current_balance = data.get("balance_s0", 0.0)
            
            if current_balance >= execution_cost:
                # Deduct micro-fuel transaction fee for advanced script execution
                data["balance_s0"] = round(current_balance - execution_cost, 8)
                data["sequence_nonce"] += 1
                data["last_sync_timestamp"] = int(time.time())

                with open(self.ledger_file, 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"{SILVER}[OK]{NC} Fuel allocated: {CRIMSON}-{execution_cost} $S0{NC} | Remaining: {SILVER}{data['balance_s0']} $S0{NC}")
                return True
            else:
                print(f"{CRIMSON}[BLOCKED] Insufficient $S0 fuel balance.{NC}")
                print(f"{DARK_GRAY}[!] Current Balance: {current_balance} $S0 | Required: {execution_cost} $S0{NC}")
                print(f"{SILVER}[*] Visit your preferred crypto hub to acquire node fuel.{NC}")
                return False
        except Exception as e:
            print(f"{CRIMSON}[ERROR] Cryptographic execution failed: {e}{NC}")
            return False

if __name__ == "__main__":
    print(f"{CRIMSON}============================================================{NC}")
    print(f"{SILVER}         🔴 S0 LEDGER BACKEND // INITIALIZATION 🔴          {NC}")
    print(f"{CRIMSON}============================================================{NC}")
    
    pilot_engine = S0LedgerEngine()
    
    # Test execution simulation to ensure path stability
    print(f"{DARK_GRAY}[*] Simulating live script handshake...{NC}")
    pilot_engine.verify_and_deduct()
    print(f"{CRIMSON}============================================================{NC}")
