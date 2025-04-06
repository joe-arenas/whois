from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import AsyncSessionLocal
from app.models.domain import Domain
from app.services.rdap_lookup import rdap_lookup  # We will create this next
from datetime import datetime

router = APIRouter()

@router.get("/lookup")
async def lookup(domain: str, db: AsyncSession = Depends(AsyncSessionLocal)):
    # Check if domain exists in the database
    result = await db.execute(select(Domain).filter(Domain.name == domain))
    db_domain = result.scalars().first()

    if db_domain:
        return {"domain": db_domain.name, "status": db_domain.last_status, "last_checked": db_domain.last_checked}

    # If not in DB, do an RDAP lookup (simulate here for now)
    rdap_data = await rdap_lookup(domain)  # This function will be implemented

    # Save new domain in DB
    new_domain = Domain(name=domain, last_status="active", last_checked=datetime.utcnow())
    db.add(new_domain)
    await db.commit()

    return {"domain": domain, "status": "active", "rdap_data": rdap_data}
