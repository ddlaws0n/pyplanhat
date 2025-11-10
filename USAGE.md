# PyPlanhat SDK - Usage Guide

This guide provides comprehensive examples for using the PyPlanhat SDK to interact with the Planhat API.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Working with Companies](#working-with-companies)
- [Working with End Users](#working-with-end-users)
- [Working with Conversations](#working-with-conversations)
- [Error Handling](#error-handling)
- [Async vs Sync](#async-vs-sync)
- [Best Practices](#best-practices)

## Installation

Install PyPlanhat using pip:

```bash
pip install pyplanhat
```

## Quick Start

### Async Example (Recommended)

```python
import asyncio
from pyplanhat import AsyncPyPlanhat, Company

async def main():
    async with AsyncPyPlanhat(api_key="your-api-key") as client:
        # List all companies
        companies = await client.companies.list()
        for company in companies:
            print(f"{company.name} - {company.status}")

asyncio.run(main())
```

### Sync Example

```python
from pyplanhat import PyPlanhat, Company

with PyPlanhat(api_key="your-api-key") as client:
    # List all companies
    companies = client.companies.list()
    for company in companies:
        print(f"{company.name} - {company.status}")
```

## Authentication

### Using API Key Directly

```python
from pyplanhat import AsyncPyPlanhat

async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # Your code here
    pass
```

### Using Environment Variables

Set your API key in environment variables:

```bash
export PLANHAT_API_KEY="your-api-key"
export PLANHAT_API_BASE_URL="https://api.planhat.com"  # optional
```

Then use the client without passing credentials:

```python
from pyplanhat import AsyncPyPlanhat

async with AsyncPyPlanhat() as client:
    # Your code here - API key loaded from environment
    pass
```

## Working with Companies

### List All Companies

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    companies = await client.companies.list()

    for company in companies:
        print(f"Company: {company.name}")
        print(f"  ID: {company.id}")
        print(f"  Status: {company.status}")
        print(f"  MRR: ${company.mrr}")
        print(f"  Health Score: {company.h}")
```

### Get a Specific Company

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    company = await client.companies.get("company-id-123")

    print(f"Company: {company.name}")
    print(f"Phase: {company.phase}")
    print(f"ARR: ${company.arr}")
```

### Create a New Company

```python
from pyplanhat import AsyncPyPlanhat, Company

async with AsyncPyPlanhat(api_key="your-api-key") as client:
    new_company = Company(
        name="Acme Corporation",
        external_id="acme-123",
        status="prospect",
        description="Leading provider of innovative solutions",
        country="US",
        city="San Francisco",
        custom={
            "industry": "Technology",
            "employee_count": 500,
            "deal_size": "enterprise"
        }
    )

    created = await client.companies.create(new_company)
    print(f"Created company with ID: {created.id}")
```

### Update a Company

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # Get existing company
    company = await client.companies.get("company-id-123")

    # Update fields
    company.status = "customer"
    company.phase = "onboarding"
    company.custom["onboarding_date"] = "2024-01-15"

    # Save changes
    updated = await client.companies.update(company.id, company)
    print(f"Updated company: {updated.name}")
```

### Delete a Company

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    await client.companies.delete("company-id-123")
    print("Company deleted successfully")
```

## Working with End Users

### List All End Users

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # List all end users
    all_users = await client.endusers.list()

    # List end users for a specific company
    company_users = await client.endusers.list(company_id="company-id-123")

    for user in company_users:
        print(f"User: {user.name} ({user.email})")
        print(f"  Position: {user.position}")
        print(f"  Primary: {user.primary}")
```

### Get a Specific End User

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    user = await client.endusers.get("user-id-456")

    print(f"User: {user.first_name} {user.last_name}")
    print(f"Email: {user.email}")
    print(f"Position: {user.position}")
    print(f"NPS Score: {user.nps}")
```

### Create a New End User

```python
from pyplanhat import AsyncPyPlanhat, EndUser

async with AsyncPyPlanhat(api_key="your-api-key") as client:
    new_user = EndUser(
        company_id="company-id-123",
        email="john.doe@example.com",
        first_name="John",
        last_name="Doe",
        position="CTO",
        phone="+1-555-0123",
        primary=True,
        tags=["decision-maker", "technical"],
        custom={
            "department": "Engineering",
            "seniority": "executive"
        }
    )

    created = await client.endusers.create(new_user)
    print(f"Created user with ID: {created.id}")
```

### Update an End User

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # Get existing user
    user = await client.endusers.get("user-id-456")

    # Update fields
    user.position = "VP of Engineering"
    user.tags.append("influencer")
    user.custom["last_contact"] = "2024-01-15"

    # Save changes
    updated = await client.endusers.update(user.id, user)
    print(f"Updated user: {updated.email}")
```

### Delete an End User

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    await client.endusers.delete("user-id-456")
    print("User deleted successfully")
```

## Working with Conversations

### List All Conversations

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # List all conversations
    all_conversations = await client.conversations.list()

    # List conversations for a specific company
    company_conversations = await client.conversations.list(company_id="company-id-123")

    for conv in company_conversations:
        print(f"Conversation: {conv.subject}")
        print(f"  Type: {conv.type}")
        print(f"  Date: {conv.date}")
        print(f"  Starred: {conv.starred}")
```

### Get a Specific Conversation

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    conversation = await client.conversations.get("conv-id-789")

    print(f"Subject: {conversation.subject}")
    print(f"Type: {conversation.type}")
    print(f"Description: {conversation.description}")
    print(f"Participants: {len(conversation.users or [])}")
```

### Create a New Conversation

```python
from pyplanhat import AsyncPyPlanhat, Conversation

async with AsyncPyPlanhat(api_key="your-api-key") as client:
    new_conversation = Conversation(
        company_id="company-id-123",
        type="email",
        subject="Q4 Business Review",
        description="Discussed quarterly performance and 2024 goals",
        date="2024-01-15T14:00:00Z",
        tags=["quarterly-review", "strategic"],
        starred=True,
        users=[
            {"id": "user-1", "name": "Account Manager", "isOwner": True},
            {"id": "user-2", "name": "Customer Success"}
        ],
        custom={
            "meeting_duration": 60,
            "outcome": "positive"
        }
    )

    created = await client.conversations.create(new_conversation)
    print(f"Created conversation with ID: {created.id}")
```

### Update a Conversation

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    # Get existing conversation
    conversation = await client.conversations.get("conv-id-789")

    # Update fields
    conversation.starred = True
    conversation.tags.append("follow-up-needed")
    conversation.custom["follow_up_date"] = "2024-02-01"

    # Save changes
    updated = await client.conversations.update(conversation.id, conversation)
    print(f"Updated conversation: {updated.subject}")
```

### Delete a Conversation

```python
async with AsyncPyPlanhat(api_key="your-api-key") as client:
    await client.conversations.delete("conv-id-789")
    print("Conversation deleted successfully")
```

## Error Handling

PyPlanhat provides specific exception types for different error scenarios:

```python
from pyplanhat import (
    AsyncPyPlanhat,
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    ServerError,
    APIConnectionError,
)

async with AsyncPyPlanhat(api_key="your-api-key") as client:
    try:
        company = await client.companies.get("company-id-123")
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
        print(f"Status code: {e.status_code}")
    except InvalidRequestError as e:
        print(f"Invalid request: {e}")
        print(f"Status code: {e.status_code}")
        print(f"Response: {e.response_body}")
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        print("Wait before retrying")
    except ServerError as e:
        print(f"Server error: {e}")
        print(f"Status code: {e.status_code}")
    except APIConnectionError as e:
        print(f"Connection error: {e}")
```

### Exception Hierarchy

```
PyPlanhatError (base exception)
├── APIConnectionError (network/timeout issues)
└── APIError (HTTP errors)
    ├── AuthenticationError (401/403)
    ├── InvalidRequestError (400/404)
    ├── RateLimitError (429)
    └── ServerError (5xx)
```

## Async vs Sync

PyPlanhat provides both async and sync APIs. The async API is recommended for better performance, especially when making multiple API calls.

### Async API (Recommended)

```python
import asyncio
from pyplanhat import AsyncPyPlanhat

async def main():
    async with AsyncPyPlanhat(api_key="your-api-key") as client:
        # Make multiple calls concurrently
        companies_task = client.companies.list()
        users_task = client.endusers.list()
        conversations_task = client.conversations.list()

        companies, users, conversations = await asyncio.gather(
            companies_task,
            users_task,
            conversations_task
        )

        print(f"Companies: {len(companies)}")
        print(f"Users: {len(users)}")
        print(f"Conversations: {len(conversations)}")

asyncio.run(main())
```

### Sync API

```python
from pyplanhat import PyPlanhat

with PyPlanhat(api_key="your-api-key") as client:
    # Synchronous calls
    companies = client.companies.list()
    users = client.endusers.list()
    conversations = client.conversations.list()

    print(f"Companies: {len(companies)}")
    print(f"Users: {len(users)}")
    print(f"Conversations: {len(conversations)}")
```

## Best Practices

### 1. Use Context Managers

Always use `async with` or `with` to ensure proper cleanup:

```python
# ✅ Good - automatic cleanup
async with AsyncPyPlanhat(api_key="key") as client:
    companies = await client.companies.list()

# ❌ Bad - manual cleanup required
client = AsyncPyPlanhat(api_key="key")
companies = await client.companies.list()
await client.close()  # Easy to forget!
```

### 2. Handle Errors Appropriately

Always catch and handle exceptions:

```python
from pyplanhat import InvalidRequestError

try:
    company = await client.companies.get("invalid-id")
except InvalidRequestError as e:
    if e.status_code == 404:
        print("Company not found")
    else:
        print(f"Error: {e}")
```

### 3. Use Environment Variables for Credentials

Never hardcode API keys:

```python
# ✅ Good
async with AsyncPyPlanhat() as client:  # Loads from PLANHAT_API_KEY env var
    pass

# ❌ Bad
async with AsyncPyPlanhat(api_key="hardcoded-key") as client:
    pass
```

### 4. Leverage Type Hints

PyPlanhat is fully typed. Use type hints for better IDE support:

```python
from pyplanhat import AsyncPyPlanhat, Company

async def get_company_name(client: AsyncPyPlanhat, company_id: str) -> str:
    company: Company = await client.companies.get(company_id)
    return company.name
```

### 5. Use Custom Fields for Extended Data

Store additional data in the `custom` field:

```python
company = Company(
    name="Acme Corp",
    custom={
        "industry": "Technology",
        "deal_size": "enterprise",
        "lead_source": "referral",
        "account_tier": "platinum"
    }
)
```

### 6. Batch Operations with Async

When performing multiple operations, use `asyncio.gather()` for concurrency:

```python
import asyncio

async with AsyncPyPlanhat(api_key="key") as client:
    # Create multiple companies concurrently
    companies = [
        Company(name="Company A"),
        Company(name="Company B"),
        Company(name="Company C"),
    ]

    tasks = [client.companies.create(c) for c in companies]
    created_companies = await asyncio.gather(*tasks)

    print(f"Created {len(created_companies)} companies")
```

### 7. Respect Rate Limits

Handle rate limit errors gracefully:

```python
import asyncio
from pyplanhat import RateLimitError

async def create_with_retry(client, company, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await client.companies.create(company)
        except RateLimitError:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                raise
```

## Advanced Examples

### Bulk Operations

```python
from pyplanhat import AsyncPyPlanhat, Company

async def bulk_create_companies(companies_data: list[dict]) -> list[Company]:
    async with AsyncPyPlanhat() as client:
        companies = [Company(**data) for data in companies_data]

        # Create all companies concurrently
        tasks = [client.companies.create(c) for c in companies]
        created = await asyncio.gather(*tasks)

        return created

# Usage
companies_data = [
    {"name": "Company A", "status": "prospect"},
    {"name": "Company B", "status": "customer"},
    {"name": "Company C", "status": "prospect"},
]

created_companies = await bulk_create_companies(companies_data)
```

### Filtering and Processing

```python
async with AsyncPyPlanhat() as client:
    # Get all companies
    all_companies = await client.companies.list()

    # Filter for high-value customers
    high_value = [
        c for c in all_companies
        if c.status == "customer" and c.mrr and c.mrr > 5000
    ]

    print(f"Found {len(high_value)} high-value customers")

    # Calculate total ARR
    total_arr = sum(c.arr or 0 for c in high_value)
    print(f"Total ARR: ${total_arr:,.2f}")
```

### Working with Relationships

```python
async with AsyncPyPlanhat() as client:
    # Get a company
    company = await client.companies.get("company-id-123")

    # Get all end users for this company
    users = await client.endusers.list(company_id=company.id)

    # Get all conversations for this company
    conversations = await client.conversations.list(company_id=company.id)

    print(f"Company: {company.name}")
    print(f"  Users: {len(users)}")
    print(f"  Conversations: {len(conversations)}")

    # Find primary contact
    primary_contact = next((u for u in users if u.primary), None)
    if primary_contact:
        print(f"  Primary Contact: {primary_contact.email}")
```

## Support

For issues, questions, or contributions, please visit:
- GitHub: https://github.com/ddlaws0n/pyplanhat
- PyPI: https://pypi.org/project/pyplanhat/

## License

MIT License - see LICENSE file for details.
