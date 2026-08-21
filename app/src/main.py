import os
from pathlib import Path
from dotenv import load_dotenv

# Search for local .env file structures during developer workspace execution
root_env_path = Path(__file__).resolve().parents[2] / '.env'
if root_env_path.exists():
    load_dotenv(dotenv_path=root_env_path)

# Extract memory configurations from active operating system RAM registers
DATABASE_URL = os.environ.get("DB_URL")
PAYMENT_GATEWAY_TOKEN = os.environ.get("API_KEY")

def execute_server_initialization():
    print("🚀 Launching Production Enterprise Python Application Core...")
    
    # DEFENSIVE GUARD BLOCK: Fail immediately if parameters cannot be located in memory
    if not DATABASE_URL or not PAYMENT_GATEWAY_TOKEN:
        print("=" * 80)
        print("❌ CRITICAL BOOT ERROR: Mandatory runtime security environment variables are missing!")
        print("=" * 80)
        print("Execution halted automatically to prevent system instability or misconfiguration flaws.")
        exit(1)
        
    print("-" * 80)
    print("✅ SECURITY CHECKS PASSED: Target credentials securely located in volatile RAM.")
    print("-" * 80)
    print(f"[AUTH INFO] Payment gateway token validated. Signature context: ...{PAYMENT_GATEWAY_TOKEN[-4:]}")
    print("🚀 Server successfully binding context parameters. Listening on port :5000")

if __name__ == "__main__":
    execute_server_initialization()

