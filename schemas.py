"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (kept for reference)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# National Museum of Sciences of Hungary schemas

class Exhibit(BaseModel):
    """
    Exhibits on display at the museum
    Collection name: "exhibit"
    """
    title: str = Field(..., description="Exhibit title")
    summary: str = Field(..., description="Short description")
    image_url: Optional[str] = Field(None, description="Cover image URL")
    tags: List[str] = Field(default_factory=list, description="Topics/tags")
    location: Optional[str] = Field(None, description="Gallery or floor")
    featured: bool = Field(False, description="Featured on homepage")

class Event(BaseModel):
    """
    Events, talks, and workshops
    Collection name: "event"
    """
    name: str
    date: str = Field(..., description="ISO date string (YYYY-MM-DD)")
    time: Optional[str] = Field(None, description="Start time")
    description: str
    image_url: Optional[str] = None
    ticket_required: bool = Field(True)

class NewsletterSubscription(BaseModel):
    """
    Newsletter sign-ups
    Collection name: "newslettersubscription"
    """
    email: EmailStr
    name: Optional[str] = None
    consent: bool = Field(True, description="User consent to receive emails")

class ContactMessage(BaseModel):
    """
    Visitor contact messages
    Collection name: "contactmessage"
    """
    name: str
    email: EmailStr
    subject: str
    message: str
