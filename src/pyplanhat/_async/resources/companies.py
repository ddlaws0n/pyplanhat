"""Company resource for PyPlanhat SDK."""

from typing import Any

from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class Company(BaseModel):
    """Company resource from Planhat API.

    Represents a company with all documented fields from the Planhat API schema.
    Only the `name` field is required; all other fields are optional.
    """

    # Required field
    name: str

    # Key properties for upsert operations
    id: str | None = Field(
        default=None, validation_alias=AliasChoices("_id", "id"), serialization_alias="_id"
    )
    external_id: str | None = Field(
        default=None,
        validation_alias=AliasChoices("externalId", "external_id"),
        serialization_alias="externalId",
    )
    source_id: str | None = Field(
        default=None,
        validation_alias=AliasChoices("sourceId", "source_id"),
        serialization_alias="sourceId",
    )

    # Core fields
    owner: str | None = None  # Account Manager ID
    co_owner: str | None = Field(
        default=None,
        validation_alias=AliasChoices("coOwner", "co_owner"),
        serialization_alias="coOwner",
    )
    phase: str | None = None  # Lifecycle phase
    status: str | None = None  # prospect/coming/customer/canceled/lost
    domains: list[str] | None = None  # Auto-generated from enduser emails
    description: str | None = None

    # Contact information
    address: str | None = None
    country: str | None = None
    city: str | None = None
    zip: str | None = None
    phone_primary: str | None = Field(
        default=None,
        validation_alias=AliasChoices("phonePrimary", "phone_primary"),
        serialization_alias="phonePrimary",
    )
    web: str | None = None

    # Financial fields (auto-generated, read-only)
    mrr: float | None = None  # Monthly Recurring Revenue
    arr: float | None = None  # Annual Recurring Revenue
    nrr30: float | None = None  # Net Revenue Retention 30 days
    mrr_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("mrrTotal", "mrr_total"),
        serialization_alias="mrrTotal",
    )
    nrr_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("nrrTotal", "nrr_total"),
        serialization_alias="nrrTotal",
    )
    mr_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("mrTotal", "mr_total"),
        serialization_alias="mrTotal",
    )
    renewal_mrr: float | None = Field(
        default=None,
        validation_alias=AliasChoices("renewalMrr", "renewal_mrr"),
        serialization_alias="renewalMrr",
    )
    renewal_arr: float | None = Field(
        default=None,
        validation_alias=AliasChoices("renewalArr", "renewal_arr"),
        serialization_alias="renewalArr",
    )
    renewal_days_from_now: int | None = Field(
        default=None,
        validation_alias=AliasChoices("renewalDaysFromNow", "renewal_days_from_now"),
        serialization_alias="renewalDaysFromNow",
    )
    customer_from: str | None = Field(
        default=None,
        validation_alias=AliasChoices("customerFrom", "customer_from"),
        serialization_alias="customerFrom",
    )  # ISO date
    customer_to: str | None = Field(
        default=None,
        validation_alias=AliasChoices("customerTo", "customer_to"),
        serialization_alias="customerTo",
    )  # ISO date
    last_renewal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("lastRenewal", "last_renewal"),
        serialization_alias="lastRenewal",
    )  # ISO date

    # Health & Activity (auto-generated, read-only)
    h: int | None = None  # Health score
    csm_score: int | None = Field(
        default=None,
        validation_alias=AliasChoices("csmScore", "csm_score"),
        serialization_alias="csmScore",
    )  # CSM score 1-5
    last_active: str | None = Field(
        default=None,
        validation_alias=AliasChoices("lastActive", "last_active"),
        serialization_alias="lastActive",
    )  # ISO timestamp
    last_touch: str | None = Field(
        default=None,
        validation_alias=AliasChoices("lastTouch", "last_touch"),
        serialization_alias="lastTouch",
    )  # ISO timestamp
    last_touch_type: str | None = Field(
        default=None,
        validation_alias=AliasChoices("lastTouchType", "last_touch_type"),
        serialization_alias="lastTouchType",
    )
    alerts: list[Any] | None = None  # Alert objects
    last_activities: list[Any] | None = Field(
        default=None,
        validation_alias=AliasChoices("lastActivities", "last_activities"),
        serialization_alias="lastActivities",
    )  # Activity objects

    # Organization support
    org_root_id: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgRootId", "org_root_id"),
        serialization_alias="orgRootId",
    )
    org_path: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices("orgPath", "org_path"),
        serialization_alias="orgPath",
    )
    org_level: int | None = Field(
        default=None,
        validation_alias=AliasChoices("orgLevel", "org_level"),
        serialization_alias="orgLevel",
    )
    org_units: list[Any] | None = Field(
        default=None,
        validation_alias=AliasChoices("orgUnits", "org_units"),
        serialization_alias="orgUnits",
    )
    org_mrr: float | None = Field(
        default=None,
        validation_alias=AliasChoices("orgMrr", "org_mrr"),
        serialization_alias="orgMrr",
    )
    org_arr: float | None = Field(
        default=None,
        validation_alias=AliasChoices("orgArr", "org_arr"),
        serialization_alias="orgArr",
    )
    org_mrr_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("orgMrrTotal", "org_mrr_total"),
        serialization_alias="orgMrrTotal",
    )
    org_arr_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("orgArrTotal", "org_arr_total"),
        serialization_alias="orgArrTotal",
    )
    org_health_total: int | None = Field(
        default=None,
        validation_alias=AliasChoices("orgHealthTotal", "org_health_total"),
        serialization_alias="orgHealthTotal",
    )

    # Custom fields
    custom: dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(populate_by_name=True)
