# emergency_gate.py
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

BRIDGE_SECRET = os.environ.get("BRIDGE_SECRET")
ADMIN_ORIGINS = os.environ.get("ADMIN_ORIGINS", "")  # comma-separated allowed origins

def emergency_middleware(app: FastAPI):
    @app.middleware("http")
    async def block_dangerous(request: Request, call_next):
        # If secret not configured, block mutating or sensitive endpoints
        if not BRIDGE_SECRET:
            if request.method in ("POST", "PUT", "DELETE", "PATCH"):
                return JSONResponse(status_code=403, content={"detail":"Temporarily disabled - emergency gate active"})
            if request.url.path in ("/codex/verify_instance","/codex/archive_response","/codex/invoke_hush","/codex/awaken_from_hush","/codex/entries"):
                return JSONResponse(status_code=403, content={"detail":"Temporarily disabled - emergency gate active"})

        # Basic origin allowlist enforcement if ADMIN_ORIGINS is set
        origin = request.headers.get("origin")
        if origin and ADMIN_ORIGINS:
            allowed = [x.strip() for x in ADMIN_ORIGINS.split(",") if x.strip()]
            if allowed and origin not in allowed:
                # allow only safe GET endpoints otherwise block
                if request.url.path not in ("/", "/health", "/bondfire_report"):
                    return JSONResponse(status_code=403, content={"detail":"Origin not allowed"})
        return await call_next(request)
    return app
