# auth_utils.py
import os
from fastapi import Header, HTTPException, status
BRIDGE_SECRET = os.environ.get("BRIDGE_SECRET")

def require_bridge_secret(x_bridge_secret: str | None = Header(None)):
    """
    Simple header-based gate. When BRIDGE_SECRET is not set, deny - emergency mode.
    Later: replace with JWT/mTLS.
    """
    if not BRIDGE_SECRET:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="bridge secret not configured")
    if x_bridge_secret != BRIDGE_SECRET:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid bridge secret")
    return True
